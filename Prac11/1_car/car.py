# IMPORTS
import pygame
import random # случайные числа (позиции, вес монет)
import time
import os
os.chdir(os.path.dirname(__file__)) # переход в папку с файлом

# INIT
pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game") #создаётся окно:название "Racer Game"

# LOAD FILES
image_background = pygame.image.load('AnimatedStreet.png')
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
coin_image = pygame.image.load('dollar.png').convert_alpha()

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1) #играет бесконечно (-1)

sound_crash = pygame.mixer.Sound('crash.wav')

# FONTS ШРИФТЫ
font_big = pygame.font.SysFont("Verdana", 60) #большой → GAME OVER
font_small = pygame.font.SysFont("Verdana", 25) #маленький → счёт

# GAME VARIABLES FPS = 60 кадров в секунду
clock = pygame.time.Clock()
FPS = 60

collected = 0  # общий счет (с учетом веса)
LEVEL_UP_COINS = 5  # каждые N монет ускоряем врага

# PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 #машина появляется по центру снизу
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed() #подлкючаем клавишы

        if keys[pygame.K_LEFT]:#движение влево
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT]:#движение вправо
            self.rect.move_ip(self.speed, 0)

        # границы экрана не даём выйти за  край
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 6  # начальная скорость
        self.generate_random()

    def generate_random(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w) #случайная позиция по горизонтали
        self.rect.top = -100

    def move(self): #движение вниз
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:#вышел за экран and появляется заново
            self.generate_random()


# COIN CLASS (С ВЕСОМ)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # случайный вес монеты
        self.value = random.choice([1, 2, 3]) #Каждый раз случайно выбирается 

        # меняем размер в зависимости от веса
        size = 30 + self.value * 10
        self.image = pygame.transform.scale(coin_image, (size, size))

        self.rect = self.image.get_rect()
        self.speed = 5

        self.generate_random()

    def generate_random(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = random.randint(-200, -50)#self.rect.top = random.randint(-200, -50)

    def move(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            # пересоздаем монету с новым весом
            self.__init__()


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        if entity != player:
            entity.move()
        screen.blit(entity.image, entity.rect)

    #СТОЛКНОВЕНИЕ С МОНЕТОЙ
    if pygame.sprite.spritecollideany(player, coin_sprites):
        collected += coin.value  # учитываем вес
        coin.__init__()  # новая монета

        # УСКОРЕНИЕ ВРАГА
        if collected % LEVEL_UP_COINS == 0:
            enemy.speed += 1  # увеличиваем скорость

    # СТОЛКНОВЕНИЕ С ВРАГОМ
    if pygame.sprite.spritecollideany(player, enemy_sprites):#проверяет столкновение
        sound_crash.play()
        time.sleep(1)

        screen.fill("red") #красный экран

        game_over_text = font_big.render("GAME OVER", True, "black") #отображаем счёт
        rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_over_text, rect)

        pygame.display.update()
        time.sleep(2)

        running = False

    # СЧЕТ (ПРАВЫЙ ВЕРХ)
    score_text = font_small.render(f"Coins: {collected}", True, "black")
    score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()