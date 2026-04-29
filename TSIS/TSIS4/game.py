import pygame
import random
import json
import os
from config import *

SETTINGS_FILE = "settings.json"


# ---------------- SETTINGS ----------------

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        default = {"snake_color": [0, 200, 0], "grid": False, "sound": True}
        save_settings(default)
        return default
    with open(SETTINGS_FILE) as f:
        return json.load(f)


def save_settings(s):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(s, f, indent=2)


# ---------------- GAME ----------------

class Game:
    def __init__(self, screen, pid, best):
        self.screen = screen
        self.pid = pid
        self.best = best
        self.font = pygame.font.SysFont(None, 26)

        self.settings = load_settings()

        # 🎵 --------- BACKGROUND MUSIC ----------
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.music_path = os.path.join(BASE_DIR, "assets", "vibe.wav")
        self.music_loaded = False

        if os.path.exists(self.music_path):
            try:
                pygame.mixer.music.load(self.music_path)
                self.music_loaded = True
            except pygame.error as e:
                print("MUSIC ERROR:", e)
                self.music_loaded = False

        # старт музыки если включена
        if self.music_loaded and self.settings.get("sound", True):
            pygame.mixer.music.play(-1)  # БЕСКОНЕЧНО

        self.reset()

    # -----------------------------------------

    def reset(self):
        cx, cy = COLS // 2, ROWS // 2
        self.snake = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.dir = (1, 0)
        self.next_dir = (1, 0)
        self.score = 0
        self.level = 1
        self.eaten = 0
        self.speed = 8
        self.over = False
        self.last_move = 0

        self.food = self.free_cell()

    # -----------------------------------------

    def free_cell(self):
        while True:
            x = random.randint(0, COLS - 1)
            y = random.randint(0, ROWS - 1)
            if (x, y) not in self.snake:
                return (x, y)

    # -----------------------------------------

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.dir != (0, 1):
                self.next_dir = (0, -1)
            elif event.key == pygame.K_DOWN and self.dir != (0, -1):
                self.next_dir = (0, 1)
            elif event.key == pygame.K_LEFT and self.dir != (1, 0):
                self.next_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and self.dir != (-1, 0):
                self.next_dir = (1, 0)

    # -----------------------------------------

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_move < 1000 // self.speed:
            return
        self.last_move = now

        # обновляем настройки каждый кадр (чтобы Sound ON/OFF работал сразу)
        self.settings = load_settings()

        # 🎵 управление фоновой музыкой
        if self.music_loaded:
            if self.settings.get("sound", True):
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()

        self.dir = self.next_dir
        hx, hy = self.snake[0]
        dx, dy = self.dir
        nx, ny = hx + dx, hy + dy

        # столкновение со стеной
        if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS:
            self.over = True
            return

        # столкновение с собой
        if (nx, ny) in self.snake:
            self.over = True
            return

        self.snake.insert(0, (nx, ny))

        # еда
        if (nx, ny) == self.food:
            self.score += 1
            self.eaten += 1

            if self.eaten % 5 == 0:
                self.level += 1
                self.speed += 1

            self.food = self.free_cell()
        else:
            self.snake.pop()

    # -----------------------------------------

    def draw(self):
        s = self.settings
        self.screen.fill(BLACK)

        # grid
        if s.get("grid", False):
            for gx in range(0, WIDTH, CELL):
                pygame.draw.line(self.screen, (30, 30, 30), (gx, 0), (gx, HEIGHT))
            for gy in range(0, HEIGHT, CELL):
                pygame.draw.line(self.screen, (30, 30, 30), (0, gy), (WIDTH, gy))

        # food
        pygame.draw.rect(
            self.screen,
            RED,
            (self.food[0] * CELL, self.food[1] * CELL, CELL, CELL)
        )

        # snake
        sc = tuple(s.get("snake_color", [0, 200, 0]))
        for i, (x, y) in enumerate(self.snake):
            color = WHITE if i == 0 else sc
            pygame.draw.rect(
                self.screen,
                color,
                (x * CELL, y * CELL, CELL, CELL)
            )

        # HUD
        hud = self.font.render(
            f"Score: {self.score}   Level: {self.level}   Best: {self.best}",
            True, WHITE
        )
        self.screen.blit(hud, (5, 5))
