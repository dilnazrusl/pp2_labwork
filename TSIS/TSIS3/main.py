import pygame
from racer import RacerGame
from ui import Button, show_leaderboard_screen, show_settings_screen
from persistence import load_settings

pygame.init()

WIDTH  = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 3 Racer")

settings = load_settings()


# ================= USERNAME =================
def get_username():
    font_label = pygame.font.SysFont("Verdana", 25)
    font_input = pygame.font.SysFont("Verdana", 30)
    username = ""

    while True:
        screen.fill((20, 20, 40))

        label = font_label.render("Enter your name:", True, (200, 200, 200))
        screen.blit(label, label.get_rect(centerx=200, y=200))

        # Поле ввода
        pygame.draw.rect(screen, (60, 60, 80), (60, 245, 280, 45), border_radius=8)
        pygame.draw.rect(screen, (120, 120, 180), (60, 245, 280, 45), 2, border_radius=8)

        name_text = font_input.render(username + "|", True, (0, 255, 120))
        screen.blit(name_text, name_text.get_rect(center=(200, 268)))

        hint = font_label.render("Press Enter to confirm", True, (120, 120, 140))
        screen.blit(hint, hint.get_rect(centerx=200, y=310))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip() != "":
                    return username.strip()
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return None
                else:
                    if len(username) < 12:
                        username += event.unicode


# ================= MAIN MENU =================
def main_menu():
    font_title = pygame.font.SysFont("Verdana", 38, bold=True)

    play_btn        = Button("Play",        100, 200, 200, 52, color=(34, 120, 34))
    leaderboard_btn = Button("Leaderboard", 100, 270, 200, 52)
    settings_btn    = Button("Settings",    100, 340, 200, 52)
    quit_btn        = Button("Quit",        100, 410, 200, 52, color=(140, 30, 30))

    while True:
        screen.fill((15, 15, 30))

        title = font_title.render("RACER", True, (255, 220, 0))
        screen.blit(title, title.get_rect(centerx=200, y=100))

        subtitle = pygame.font.SysFont("Verdana", 18).render("TSIS 3 Edition", True, (160, 160, 200))
        screen.blit(subtitle, subtitle.get_rect(centerx=200, y=150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if play_btn.is_clicked(event):
                # Перезагружаем настройки перед каждой игрой
                current_settings = load_settings()
                username = get_username()
                if username:
                    game = RacerGame(screen, username, current_settings)
                    game.run()

            if leaderboard_btn.is_clicked(event):
                show_leaderboard_screen(screen)

            if settings_btn.is_clicked(event):
                show_settings_screen(screen)

            if quit_btn.is_clicked(event):
                return "quit"

        play_btn.draw(screen)
        leaderboard_btn.draw(screen)
        settings_btn.draw(screen)
        quit_btn.draw(screen)

        pygame.display.update()


# ================= START =================
running = True
while running:
    state = main_menu()
    if state == "quit":
        running = False

pygame.quit()