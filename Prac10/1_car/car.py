
# IMPORTS

import pygame
import random #чтобы появлялись случайные позиции
import time #чтобы делать задержки
import os
os.chdir(os.path.dirname(__file__))

# INIT

pygame.init()#Запускает все модули pygame.

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set_mode — создаёт окно
pygame.display.set_caption("Racer Game") #set_caption — название окна


# LOAD FILES (same folder!)

image_background = pygame.image.load('AnimatedStreet.png')
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
coin_image = pygame.image.load('dollar.png').convert_alpha()#.convert_alpha() — сохраняет прозрачность у монетки.

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1) #-1 означает бесконечное повторение

sound_crash = pygame.mixer.Sound('crash.wav') #Отдельный звук при аварии.


# FONTS Создаются шрифты для:

font_big = pygame.font.SysFont("Verdana", 60) #GAME OVER
font_small = pygame.font.SysFont("Verdana", 25) #счётчика монет


# GAME VARIABLES

clock = pygame.time.Clock()
FPS = 60 #FPS = 60 кадров в секунду если 90 то быстрее 

collected = 0  # coins counter


# PLAYER CLASS Создаём класс игрока.

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 #centerx — фиксирует её по центру
        self.rect.bottom = HEIGHT #bottom = HEIGHT — ставит её внизу экрана
        self.speed = 5 #увеличиваем скорость 

    def move(self): #X меняется Y = 0 (не двигается)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # keep player inside screen
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > WIDTH: #если вышла слева → вернуть на 0
            self.rect.right = WIDTH #если вышла справа → вернуть на WIDTH


# ENEMY CLASS

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect() #Она создаёт прямоугольник такого же размера, как картинка.
        self.speed = 6
        self.generate_random()

    def generate_random(self): #Враг появляется ВЫШЕ экрана.
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = -100

    def move(self):
        self.rect.move_ip(0, self.speed) # Y увеличивается → машина едет вниз. тут наоборот машинка только по у двигается 

        # if enemy leaves screen → respawn Создаётся заново сверху.
        if self.rect.top > HEIGHT:
            self.generate_random()


# COIN CLASS (RANDOM SPAWN)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_image, (40, 40))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.generate_random()

    def generate_random(self):
        # random position ABOVE screen
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = random.randint(-200, -50) #X случайный по ширине Y случайный выше экрана

    def move(self):
        self.rect.move_ip(0, self.speed)

        # if coin leaves screen → respawn
        if self.rect.top > HEIGHT: #Монетка снова появляется сверху.
            self.generate_random()


# CREATE OBJECTS

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)


# GAME LOOP

running = True
while running:

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # MOVE PLAYER
    player.move()

    # DRAW BACKGROUND Фон просто постоянно перерисовывается.
    screen.blit(image_background, (0, 0))

    # MOVE & DRAW ALL OBJECTS
    for entity in all_sprites:
        if entity != player:
            entity.move()
        screen.blit(entity.image, entity.rect)

    
    # COIN COLLISION collected увеличивается на 1
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        collected += 1
        coin.generate_random()

    
    # ENEMY COLLISION (GAME OVER) Если игрок касается врага: Воспроизводится звук
    #Экран красный
    #GAME OVER
    if pygame.sprite.spritecollideany(player, enemy_sprites):#Пересекаются ли прямоугольники (rect) игрока и врага?
        sound_crash.play()
        time.sleep(1)

        screen.fill("red")

        game_over_text = font_big.render("GAME OVER", True, "black")
        rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_over_text, rect)

        pygame.display.update()
        time.sleep(2)

        running = False

    
    # DRAW SCORE (TOP RIGHT)Это размещает текст:
    score_text = font_small.render(f"Coins: {collected}", True, "black")
    score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
