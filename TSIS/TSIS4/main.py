import pygame
import json
import db
from game import run_game

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont(None, 40)

# load settings
with open("settings.json") as f:
    settings = json.load(f)

username = ""
state = "menu"


def draw_text(text, y):
    img = font.render(text, True, (255,255,255))
    screen.blit(img, (100, y))


running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = "game"
                else:
                    username += event.unicode

        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                state = "menu"

    if state == "menu":
        draw_text("Enter name:", 100)
        draw_text(username, 150)
        draw_text("Press Enter to Play", 200)

    elif state == "game":
        run_game(screen, settings, username, db)
        state = "leaderboard"

    elif state == "leaderboard":
        data = db.get_top10()
        y = 100
        for row in data:
            draw_text(f"{row[0]} {row[1]}", y)
            y += 40

    pygame.display.flip()

pygame.quit()