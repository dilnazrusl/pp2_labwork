import pygame
import random

CELL = 30
WIDTH, HEIGHT = 600, 600


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, color):
        self.body = [Point(10, 10)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1
        self.color = color
        self.alive = True
        self.shield = False

    def move(self):
        head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)

        # collision
        if head.x < 0 or head.y < 0 or head.x >= WIDTH//CELL or head.y >= HEIGHT//CELL:
            if self.shield:
                self.shield = False
            else:
                self.alive = False

        for seg in self.body:
            if head.x == seg.x and head.y == seg.y:
                if self.shield:
                    self.shield = False
                else:
                    self.alive = False

        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])


class Food:
    def __init__(self):
        self.value = random.choice([1, 2, 3])
        self.pos = Point(random.randint(0, 19), random.randint(0, 19))
        self.spawn_time = pygame.time.get_ticks()

    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 5000


class Poison:
    def __init__(self):
        self.pos = Point(random.randint(0, 19), random.randint(0, 19))


class PowerUp:
    def __init__(self):
        self.type = random.choice(["speed", "slow", "shield"])
        self.pos = Point(random.randint(0, 19), random.randint(0, 19))
        self.spawn_time = pygame.time.get_ticks()


def run_game(screen, settings, username, db):
    clock = pygame.time.Clock()

    snake = Snake(settings["snake_color"])
    food = Food()
    poison = Poison()
    power = None

    speed = 5

    while snake.alive:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx, snake.dy = 1, 0
                if event.key == pygame.K_LEFT:
                    snake.dx, snake.dy = -1, 0
                if event.key == pygame.K_UP:
                    snake.dx, snake.dy = 0, -1
                if event.key == pygame.K_DOWN:
                    snake.dx, snake.dy = 0, 1

        snake.move()
        head = snake.body[0]

        # food
        if head.x == food.pos.x and head.y == food.pos.y:
            snake.score += food.value
            snake.grow()
            food = Food()

        if food.expired():
            food = Food()

        # poison
        if head.x == poison.pos.x and head.y == poison.pos.y:
            if len(snake.body) <= 2:
                snake.alive = False
            else:
                snake.body = snake.body[:-2]
            poison = Poison()

        # power
        if power is None and random.random() < 0.01:
            power = PowerUp()

        if power:
            if pygame.time.get_ticks() - power.spawn_time > 8000:
                power = None
            elif head.x == power.pos.x and head.y == power.pos.y:
                if power.type == "speed":
                    speed = 10
                elif power.type == "slow":
                    speed = 3
                elif power.type == "shield":
                    snake.shield = True
                power = None

        # draw
        for seg in snake.body:
            pygame.draw.rect(screen, snake.color, (seg.x*CELL, seg.y*CELL, CELL, CELL))

        pygame.draw.rect(screen, (0,255,0), (food.pos.x*CELL, food.pos.y*CELL, CELL, CELL))
        pygame.draw.rect(screen, (150,0,0), (poison.pos.x*CELL, poison.pos.y*CELL, CELL, CELL))

        if power:
            pygame.draw.rect(screen, (0,0,255), (power.pos.x*CELL, power.pos.y*CELL, CELL, CELL))

        pygame.display.flip()
        clock.tick(speed)

    db.save_score(username, snake.score, snake.level)
    return snake.score