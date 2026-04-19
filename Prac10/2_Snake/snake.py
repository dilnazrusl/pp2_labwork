import pygame
import random
from color_palette import *

pygame.init()

# --- SETTINGS ---
WIDTH, HEIGHT = 600, 600
CELL = 30
FPS = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()


# --- DRAW GRID ---
def draw_grid():
    for x in range(0, WIDTH, CELL):
        for y in range(0, HEIGHT, CELL):
            pygame.draw.rect(screen, colorGRAY, (x, y, CELL, CELL), 1)


# --- POINT CLASS ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# --- SNAKE CLASS ---
class Snake:
    def __init__(self):
        self.body = [Point(10, 10), Point(10, 11), Point(10, 12)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1
        self.alive = True

    def move(self):
        # move body
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # move head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        head = self.body[0]

        # --- WALL COLLISION ---
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            self.alive = False

        # --- SELF COLLISION ---
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                self.alive = False

    def draw(self):
        # draw head
        pygame.draw.rect(screen, colorRED,
                         (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))

        # draw body
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW,
                             (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_food(self, food):
        head = self.body[0]

        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 1

            # grow snake
            self.body.append(Point(head.x, head.y))

            # generate new food
            food.generate(self.body)

            # --- LEVEL SYSTEM ---
            self.level = 1 + self.score // 3


# --- FOOD CLASS ---
class Food:
    def __init__(self):
        self.pos = Point(0, 0)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN,
                         (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate(self, snake_body):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)

            # check collision with snake
            if not any(segment.x == x and segment.y == y for segment in snake_body):
                self.pos = Point(x, y)
                break


# --- INIT GAME ---
snake = Snake()
food = Food()
food.generate(snake.body)

running = True

while running:
    # --- EVENTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1

    # --- GAME LOGIC ---
    if snake.alive:
        snake.move()
        snake.check_food(food)

    # --- DRAW ---
    screen.fill(colorBLACK)
    draw_grid()

    snake.draw()
    food.draw()

    # --- UI ---
    score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
    level_text = font.render(f"Level: {snake.level}", True, colorWHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # --- GAME OVER ---
    if not snake.alive:
        game_over = font.render("GAME OVER", True, colorRED)
        screen.blit(game_over, (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.flip()

    # --- SPEED INCREASE ---
    speed = FPS + snake.level * 2
    clock.tick(speed)

pygame.quit()