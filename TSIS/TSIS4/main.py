import pygame
import sys
import os
from config import *
from db import init_db, get_or_create_player, save_result, get_leaderboard, get_best
from game import Game, load_settings, save_settings

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font_big  = pygame.font.SysFont(None, 48)
font_med  = pygame.font.SysFont(None, 32)
font_small = pygame.font.SysFont(None, 26)

# --------------------------------------------------------------------------- helpers

def draw_text(text, x, y, color=WHITE, fnt=None):
    if fnt is None:
        fnt = font_med
    img = fnt.render(text, True, color)
    screen.blit(img, (x, y))


def draw_button(text, x, y, w=200, h=44, color=GRAY):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, border_radius=6)
    pygame.draw.rect(screen, WHITE, rect, 2, border_radius=6)
    img = font_med.render(text, True, WHITE)
    tx  = x + (w - img.get_width()) // 2
    ty  = y + (h - img.get_height()) // 2
    screen.blit(img, (tx, ty))
    return rect


def draw_centered(text, y, color=WHITE, fnt=None):
    if fnt is None:
        fnt = font_med
    img = fnt.render(text, True, color)
    screen.blit(img, ((WIDTH - img.get_width()) // 2, y))

# --------------------------------------------------------------------------- screens

def menu_screen():
    username = ""
    active   = True  # input box active

    while True:
        screen.fill(BLACK)

        draw_centered(" SNAKE  ", 40, GREEN, font_big)
        draw_text("Enter your name:", 150, 130, WHITE, font_med)

        # input box
        box = pygame.Rect(150, 162, 300, 36)
        pygame.draw.rect(screen, WHITE, box, 2, border_radius=4)
        draw_text(username, 158, 170, WHITE, font_med)

        play_btn = draw_button("  PLAY",        150, 230, 300, 44)
        lb_btn   = draw_button("  LEADERBOARD", 150, 286, 300, 44)
        set_btn  = draw_button("  SETTINGS",    150, 342, 300, 44)
        quit_btn = draw_button("  QUIT",         150, 398, 300, 44)

        # error hint
        if not username:
            draw_text("(type a name to play)", 170, 455, GRAY, font_small)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif e.key == pygame.K_RETURN:
                    if username.strip():
                        pid = get_or_create_player(username.strip())
                        return username.strip(), pid
                else:
                    if len(username) < 20:
                        username += e.unicode

            if e.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(e.pos) and username.strip():
                    pid = get_or_create_player(username.strip())
                    return username.strip(), pid
                if lb_btn.collidepoint(e.pos):
                    leaderboard_screen()
                if set_btn.collidepoint(e.pos):
                    settings_screen()
                if quit_btn.collidepoint(e.pos):
                    pygame.quit()
                    sys.exit()


def leaderboard_screen():
    data = get_leaderboard()

    while True:
        screen.fill(BLACK)
        draw_centered("  LEADERBOARD", 20, YELLOW, font_big)

        # header
        hdr_y = 80
        draw_text("#",    50,  hdr_y, GRAY, font_small)
        draw_text("NAME", 80,  hdr_y, GRAY, font_small)
        draw_text("SCORE",250, hdr_y, GRAY, font_small)
        draw_text("LVL",  330, hdr_y, GRAY, font_small)
        draw_text("DATE", 380, hdr_y, GRAY, font_small)
        pygame.draw.line(screen, GRAY, (40, hdr_y + 20), (560, hdr_y + 20), 1)

        y = hdr_y + 30
        for i, (name, score, lvl, date) in enumerate(data):
            row_color = YELLOW if i == 0 else WHITE
            date_str  = date.strftime("%d.%m.%y") if date else "—"
            draw_text(str(i + 1),  50,  y, row_color, font_small)
            draw_text(name[:15],   80,  y, row_color, font_small)
            draw_text(str(score),  250, y, row_color, font_small)
            draw_text(str(lvl),    330, y, row_color, font_small)
            draw_text(date_str,    380, y, row_color, font_small)
            y += 28

        back = draw_button("◀  BACK", 200, 530, 200, 44)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if back.collidepoint(e.pos):
                    return


def settings_screen():
    settings = load_settings()

    color_options = {
        "Green":  [0, 200, 0],
        "Blue":   [0, 120, 255],
        "Yellow": [255, 220, 0],
        "White":  [255, 255, 255],
        "Orange": [255, 140, 0],
        "Purple": [150, 0, 200],
    }
    color_names = list(color_options.keys())

    # find current color index
    cur_idx = 0
    for i, (name, val) in enumerate(color_options.items()):
        if settings.get("snake_color") == val:
            cur_idx = i
            break

    while True:
        screen.fill(BLACK)
        draw_centered("⚙  SETTINGS", 40, WHITE, font_big)

        # sound toggle
        s_label = "Sound:  ON" if settings.get("sound", True) else "Sound:  OFF"
        s_color  = GREEN if settings.get("sound", True) else RED
        sound_btn = draw_button(s_label, 150, 150, 300, 44, s_color)

        # grid toggle
        g_label = "Grid:  ON" if settings.get("grid", False) else "Grid:  OFF"
        g_color  = GREEN if settings.get("grid", False) else GRAY
        grid_btn = draw_button(g_label, 150, 210, 300, 44, g_color)

        # snake color
        draw_text("Snake color:", 150, 278, WHITE, font_med)
        prev_btn = draw_button("<", 150, 308, 44, 44)
        next_btn = draw_button(">", 410, 308, 44, 44)

        cur_name  = color_names[cur_idx]
        swatch_c  = tuple(color_options[cur_name])
        pygame.draw.rect(screen, swatch_c, (206, 308, 200, 44), border_radius=4)
        draw_text(cur_name, 206 + (200 - font_med.size(cur_name)[0]) // 2, 318,
                  BLACK if sum(swatch_c) > 400 else WHITE, font_med)

        save_btn = draw_button("  SAVE & BACK", 150, 420, 300, 44, GREEN)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if sound_btn.collidepoint(e.pos):
                    settings["sound"] = not settings.get("sound", True)

                if grid_btn.collidepoint(e.pos):
                    settings["grid"] = not settings.get("grid", False)

                if prev_btn.collidepoint(e.pos):
                    cur_idx = (cur_idx - 1) % len(color_names)
                    settings["snake_color"] = color_options[color_names[cur_idx]]

                if next_btn.collidepoint(e.pos):
                    cur_idx = (cur_idx + 1) % len(color_names)
                    settings["snake_color"] = color_options[color_names[cur_idx]]

                if save_btn.collidepoint(e.pos):
                    save_settings(settings)
                    return


def gameover_screen(score, level, best):
    while True:
        screen.fill(BLACK)

        draw_centered("GAME OVER", 100, RED, font_big)

        draw_centered(f"Score:  {score}",  200, WHITE,  font_med)
        draw_centered(f"Level:  {level}",  240, WHITE,  font_med)
        draw_centered(f"Best:   {best}",   280, YELLOW, font_med)

        if score >= best and score > 0:
            draw_centered(" New personal best!", 320, GREEN, font_small)

        retry = draw_button(" RETRY",     120, 390, 160, 44)
        menu  = draw_button(" MAIN MENU", 320, 390, 160, 44)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if retry.collidepoint(e.pos):
                    return "retry"
                if menu.collidepoint(e.pos):
                    return "menu"

# --------------------------------------------------------------------------- main

def main():
    init_db()
    name, pid = menu_screen()
    best = get_best(pid)

    while True:
        game = Game(screen, pid, best)

        # game loop
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                game.handle_input(e)

            game.update()
            game.draw()
            pygame.display.flip()
            clock.tick(60)

            if game.over:
                running = False

        # save to DB
        save_result(pid, game.score, game.level)

        if game.score > best:
            best = game.score

        result = gameover_screen(game.score, game.level, best)

        if result == "menu":
            name, pid = menu_screen()
            best = get_best(pid)
        # else "retry" → loop again with same pid


if __name__ == "__main__":
    main()