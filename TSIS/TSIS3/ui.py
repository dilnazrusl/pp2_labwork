import pygame
import os
from persistence import load_leaderboard, load_settings, save_settings

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")


# ================= BUTTON CLASS =================
class Button:
    def __init__(self, text, x, y, width, height, color=(100, 100, 100), text_color=(255, 255, 255)):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("Verdana", 22)
        self.color = color
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
        label = self.font.render(self.text, True, self.text_color)
        screen.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False


# ================= LEADERBOARD SCREEN =================
def show_leaderboard_screen(screen):
    leaderboard = load_leaderboard()
    font_title = pygame.font.SysFont("Verdana", 30)
    font = pygame.font.SysFont("Verdana", 20)
    back_btn = Button("Back", 140, 530, 120, 40)

    running = True
    while running:
        screen.fill((10, 10, 30))

        title = font_title.render("TOP 10 LEADERBOARD", True, (255, 220, 0))
        screen.blit(title, title.get_rect(centerx=200, y=30))

        y = 80
        for i, entry in enumerate(leaderboard[:10]):
            color = (255, 255, 100) if i == 0 else (200, 200, 200)
            text = font.render(
                f"{i+1}. {entry['name']}  —  {entry['score']} pts  —  {entry['distance']} m",
                True, color
            )
            screen.blit(text, (20, y))
            y += 40

        back_btn.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if back_btn.is_clicked(event):
                running = False


# ================= DIFFICULTY SUBMENU =================
def show_difficulty_screen(screen, settings):
    """
    Открывает подменю выбора сложности.
    Easy:   скорость врага 4-6
    Medium: скорость врага 6-9
    Hard:   скорость врага 9-12
    Возвращает обновлённый settings.
    """
    font_title = pygame.font.SysFont("Verdana", 28)
    font_info = pygame.font.SysFont("Verdana", 17)

    easy_btn   = Button("Easy",   100, 160, 200, 55, color=(34, 139, 34))
    medium_btn = Button("Medium", 100, 240, 200, 55, color=(184, 134, 11))
    hard_btn   = Button("Hard",   100, 320, 200, 55, color=(180, 30, 30))
    back_btn   = Button("Back",   140, 420, 120, 40)

    diff_info = {
        "easy":   "Slow traffic (speed 4–6)",
        "medium": "Normal traffic (speed 6–9)",
        "hard":   "Fast traffic (speed 9–12)",
    }

    running = True
    while running:
        screen.fill((20, 20, 40))

        title = font_title.render("Choose Difficulty", True, (255, 255, 255))
        screen.blit(title, title.get_rect(centerx=200, y=80))

        current = settings.get("difficulty", "medium")
        info_text = font_info.render(f"Current: {current.capitalize()}  —  {diff_info.get(current, '')}", True, (180, 180, 180))
        screen.blit(info_text, info_text.get_rect(centerx=200, y=130))

        easy_btn.draw(screen)
        medium_btn.draw(screen)
        hard_btn.draw(screen)
        back_btn.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return settings
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return settings

            if easy_btn.is_clicked(event):
                settings["difficulty"] = "easy"
                save_settings(settings)
                return settings

            if medium_btn.is_clicked(event):
                settings["difficulty"] = "medium"
                save_settings(settings)
                return settings

            if hard_btn.is_clicked(event):
                settings["difficulty"] = "hard"
                save_settings(settings)
                return settings

            if back_btn.is_clicked(event):
                return settings

    return settings


# ================= SETTINGS SCREEN =================
def show_settings_screen(screen):
    settings = load_settings()

    font_title = pygame.font.SysFont("Verdana", 28)
    font_info  = pygame.font.SysFont("Verdana", 17)

    # Кнопки
    sound_btn  = Button("Toggle Sound",  90, 160, 220, 55)
    color_btn  = Button("Car Color",     90, 240, 220, 55)
    diff_btn   = Button("Difficulty",    90, 320, 220, 55)
    back_btn   = Button("Back",         140, 430, 120, 40)

    # Отслеживаем текущий трек музыки (1 или 2)
    # Синхронизируем с settings["music_track"]
    if "music_track" not in settings:
        settings["music_track"] = 1

    def get_music_filename():
        if settings["music_track"] == 1:
            return "background.wav"
        else:
            return "background_2.wav"

    def apply_music():
        """Применяем текущий трек (или тишину если sound выключен)"""
        if settings["sound"]:
            try:
                path = os.path.join(ASSETS, get_music_filename())
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(-1)
            except Exception:
                pass
        else:
            pygame.mixer.music.stop()

    running = True
    while running:
        screen.fill((25, 25, 45))

        # Заголовок
        title = font_title.render("Settings", True, (255, 255, 255))
        screen.blit(title, title.get_rect(centerx=200, y=60))

        # --- Информация о текущих настройках ---
        # Звук
        sound_status = "ON" if settings["sound"] else "OFF"
        track_name   = get_music_filename()
        s_text = font_info.render(f"Sound: {sound_status}  |  Track: {track_name}", True, (160, 220, 160))
        screen.blit(s_text, s_text.get_rect(centerx=200, y=130))

        # Цвет машины
        car_color = settings.get("car_color", "default")
        if car_color == "default":
            car_label = "Player car: Blue (Player.png)"
        else:
            car_label = "Player car: Red (Enemy.png)"
        c_text = font_info.render(car_label, True, (160, 200, 255))
        screen.blit(c_text, c_text.get_rect(centerx=200, y=218))

        # Сложность
        diff = settings.get("difficulty", "medium")
        d_text = font_info.render(f"Difficulty: {diff.capitalize()}", True, (255, 200, 100))
        screen.blit(d_text, d_text.get_rect(centerx=200, y=298))

        # Рисуем кнопки
        sound_btn.draw(screen)
        color_btn.draw(screen)
        diff_btn.draw(screen)
        back_btn.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_settings(settings)
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                save_settings(settings)
                return

            # --- Toggle Sound ---
            if sound_btn.is_clicked(event):
                if settings["sound"]:
                    # Звук был включён — выключаем
                    settings["sound"] = False
                    pygame.mixer.music.stop()
                else:
                    # Звук был выключен — включаем текущий трек
                    settings["sound"] = True
                    apply_music()

            # --- Car Color ---
            if color_btn.is_clicked(event):
                # Переключаем: default (синяя) ↔ red (красная)
                if settings.get("car_color", "default") == "default":
                    settings["car_color"] = "red"
                else:
                    settings["car_color"] = "default"

            # --- Difficulty (открываем подменю) ---
            if diff_btn.is_clicked(event):
                settings = show_difficulty_screen(screen, settings)

            # --- Back ---
            if back_btn.is_clicked(event):
                save_settings(settings)
                running = False

    save_settings(settings)