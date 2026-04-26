import pygame
import random
import os
import time
from persistence import save_score, load_settings

WIDTH  = 400
HEIGHT = 600

# Скорости врагов по уровню сложности
DIFFICULTY_SPEED = {
    "easy":   (4, 6),
    "medium": (6, 9),
    "hard":   (9, 12),
}


# ================= PLAYER =================
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect  = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 80)
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Не выходим за границы экрана
        self.rect.left  = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)


# ================= COIN =================
class Coin(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.base_image = image
        self.reset()

    def reset(self):
        # Случайный вес монеты (1, 2 или 3) — влияет на размер и очки
        self.value = random.choice([1, 2, 3])
        size = 30 + self.value * 10
        self.image = pygame.transform.scale(self.base_image, (size, size))
        self.rect  = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-400, -50)
        self.speed  = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()


# ================= OIL SPILL =================
class OilSpill(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (20, 20, 20, 200), (0, 10, 50, 30))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-500, -100)
        self.speed  = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()


# ================= TRAFFIC CAR =================
class TrafficCar(pygame.sprite.Sprite):
    def __init__(self, image, difficulty="medium"):
        super().__init__()
        self.image = image
        self.rect  = self.image.get_rect()
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-600, -100)

        # Скорость зависит от уровня сложности
        lo, hi = DIFFICULTY_SPEED.get(self.difficulty, (6, 9))
        self.speed = random.randint(lo, hi)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()


# ================= POWER-UP =================
class PowerUp(pygame.sprite.Sprite):
    COLORS = {
        "nitro":  (50,  50,  255),
        "shield": (0,   220, 220),
        "repair": (50,  200, 50),
    }

    def __init__(self):
        super().__init__()
        self.type = random.choice(["nitro", "shield", "repair"])

        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.COLORS[self.type], (0, 0, 32, 32), border_radius=6)

        # Буква на значке
        font = pygame.font.SysFont("Verdana", 18, bold=True)
        letter = font.render(self.type[0].upper(), True, (255, 255, 255))
        self.image.blit(letter, letter.get_rect(center=(16, 16)))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 32)
        self.rect.y = random.randint(-500, -100)

        self.spawn_time = time.time()
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        # Исчезает если вышел за экран или прошло 7 секунд
        if self.rect.top > HEIGHT or time.time() - self.spawn_time > 7:
            self.kill()


# ================= RACER GAME =================
class RacerGame:
    def __init__(self, screen, username, settings):
        self.screen   = screen
        self.username = username
        self.settings = settings

        self.clock = pygame.time.Clock()
        self.FPS   = 60

        BASE   = os.path.dirname(os.path.abspath(__file__))
        ASSETS = os.path.join(BASE, "assets")

        # --- Загрузка ресурсов ---
        self.bg        = pygame.image.load(os.path.join(ASSETS, "AnimatedStreet.png"))
        self.player_img = pygame.image.load(os.path.join(ASSETS, "Player.png"))
        self.enemy_img  = pygame.image.load(os.path.join(ASSETS, "Enemy.png"))
        self.coin_img   = pygame.image.load(os.path.join(ASSETS, "dollar.png")).convert_alpha()

        self.crash_sound = pygame.mixer.Sound(os.path.join(ASSETS, "crash.wav"))

        # --- Музыка (с учётом настроек) ---
        if self.settings.get("sound", True):
            track = "background_2.wav" if self.settings.get("music_track", 1) == 2 else "background.wav"
            try:
                pygame.mixer.music.load(os.path.join(ASSETS, track))
                pygame.mixer.music.play(-1)
            except Exception:
                pass

        # --- Цвет машины ---
        # Если пользователь выбрал "red" — машинки меняются местами
        if self.settings.get("car_color", "default") == "red":
            # Меняем изображения местами и переворачиваем по вертикали,
            # чтобы обе машинки ехали «носом вперёд» как задумано
            self.player_img = pygame.transform.flip(self.enemy_img, False, True)
            self.enemy_img  = pygame.transform.flip(
                pygame.image.load(os.path.join(ASSETS, "Player.png")), False, True
            )

        # --- Спрайты ---
        self.difficulty = self.settings.get("difficulty", "medium")

        self.player  = Player(self.player_img)
        self.coins   = pygame.sprite.Group(Coin(self.coin_img), Coin(self.coin_img))
        self.oils    = pygame.sprite.Group(OilSpill(), OilSpill())
        self.traffic = pygame.sprite.Group(TrafficCar(self.enemy_img, self.difficulty))
        self.powers  = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group(
            self.player,
            *self.coins,
            *self.oils,
            *self.traffic,
        )

        # --- Игровые переменные ---
        self.coin_score  = 0
        self.distance    = 0.0

        self.active_power = None
        self.power_timer  = 0.0

        self.font_ui  = pygame.font.SysFont("Verdana", 18)
        self.font_big = pygame.font.SysFont("Verdana", 55)

    # -------- ОСНОВНОЙ ЦИКЛ --------
    def run(self):
        running = True

        while running:
            self.clock.tick(self.FPS)
            self.distance += 0.1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Обновляем все спрайты
            self.all_sprites.update()
            self.powers.update()

            # --- Монеты ---
            for coin in self.coins:
                if self.player.rect.colliderect(coin.rect):
                    self.coin_score += coin.value
                    coin.reset()

                    # Ускорение врагов каждые 5 очков
                    if self.coin_score % 5 == 0:
                        for car in self.traffic:
                            car.speed = min(car.speed + 1, 15)

            # --- Масло ---
            for oil in self.oils:
                if self.player.rect.colliderect(oil.rect):
                    # Занос: машину сдвигает в случайную сторону
                    self.player.rect.x += random.choice([-50, 50])
                    self.player.rect.left  = max(0, self.player.rect.left)
                    self.player.rect.right = min(WIDTH, self.player.rect.right)
                    oil.reset()

            # --- Трафик ---
            for car in self.traffic:
                if self.player.rect.colliderect(car.rect):
                    if self.active_power == "shield":
                        # Щит поглощает удар
                        self.active_power = None
                        car.reset()
                    else:
                        return self.game_over()

            # --- Power-up спавн ---
            if random.randint(1, 200) == 1:
                self.powers.add(PowerUp())

            # --- Сбор power-up ---
            for power in list(self.powers):
                if self.player.rect.colliderect(power.rect):
                    self.active_power = power.type
                    self.power_timer  = time.time()

                    if self.active_power == "repair":
                        # Repair: центрируем машину и сбрасываем масло
                        self.player.rect.centerx = WIDTH // 2
                        for oil in self.oils:
                            oil.reset()
                        self.active_power = None  # мгновенный эффект

                    power.kill()

            # --- Эффект Nitro ---
            if self.active_power == "nitro":
                self.player.speed = 11
                if time.time() - self.power_timer > 4:
                    self.active_power = None
                    self.player.speed = 6
            elif self.active_power != "nitro":
                if self.player.speed == 11:
                    self.player.speed = 6

            # --- Масштабирование сложности: новые машины ---
            if int(self.distance) % 300 == 0 and int(self.distance) > 0:
                new_car = TrafficCar(self.enemy_img, self.difficulty)
                self.traffic.add(new_car)
                self.all_sprites.add(new_car)

            # --- Рисование ---
            self.screen.blit(self.bg, (0, 0))
            self.all_sprites.draw(self.screen)
            self.powers.draw(self.screen)

            self._draw_hud()

            pygame.display.update()

    # -------- HUD --------
    def _draw_hud(self):
        # Фон HUD (полупрозрачная полоска)
        hud = pygame.Surface((WIDTH, 80), pygame.SRCALPHA)
        hud.fill((0, 0, 0, 120))
        self.screen.blit(hud, (0, 0))

        self.screen.blit(
            self.font_ui.render(f"Coins: {self.coin_score}", True, (255, 230, 0)),
            (10, 8)
        )
        self.screen.blit(
            self.font_ui.render(f"Dist: {int(self.distance)} m", True, (200, 230, 255)),
            (10, 30)
        )
        self.screen.blit(
            self.font_ui.render(f"Diff: {self.difficulty.capitalize()}", True, (200, 200, 200)),
            (10, 52)
        )

        # Активный power-up
        if self.active_power:
            remaining = ""
            if self.active_power == "nitro":
                secs = max(0, 4 - (time.time() - self.power_timer))
                remaining = f" {secs:.1f}s"
            color = {"nitro": (100, 100, 255), "shield": (0, 220, 220)}.get(self.active_power, (100, 255, 100))
            self.screen.blit(
                self.font_ui.render(f"Power: {self.active_power.upper()}{remaining}", True, color),
                (200, 8)
            )

    # -------- GAME OVER --------
    def game_over(self):
        pygame.mixer.music.stop()
        self.crash_sound.play()
        time.sleep(0.5)

        score = self.coin_score * 10 + int(self.distance)
        save_score(self.username, score, int(self.distance))

        # Красный экран с надписью
        self.screen.fill((200, 0, 0))

        text = self.font_big.render("GAME OVER", True, (0, 0, 0))
        self.screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))

        font_med = pygame.font.SysFont("Verdana", 24)
        self.screen.blit(
            font_med.render(f"Score: {score}", True, (255, 255, 255)),
            font_med.render(f"Score: {score}", True, (255, 255, 255)).get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        )
        self.screen.blit(
            font_med.render(f"Distance: {int(self.distance)} m", True, (255, 255, 255)),
            font_med.render(f"Distance: {int(self.distance)} m", True, (255, 255, 255)).get_rect(center=(WIDTH // 2, HEIGHT // 2 + 55))
        )

        pygame.display.update()
        pygame.time.delay(3000)