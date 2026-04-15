import pygame
import sys
from player import MusicPlayer

pygame.init()

# Window settings
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Music Player")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Create player
player = MusicPlayer("music")

running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    # Display current track
    track_text = font.render(
        f"Current Track: {player.get_current_track_name()}",
        True,
        (255, 255, 255)
    )

    # Display playback position
    position_text = font.render(
        f"Position: {player.get_position()} sec",
        True,
        (200, 200, 200)
    )

    # Controls info
    controls_text = font.render(
        "P=Play  S=Stop  N=Next  B=Back  Q=Quit",
        True,
        (100, 200, 255)
    )

    screen.blit(track_text, (50, 100))
    screen.blit(position_text, (50, 150))
    screen.blit(controls_text, (50, 250))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
