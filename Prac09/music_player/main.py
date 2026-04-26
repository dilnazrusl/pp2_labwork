import pygame
import sys
from player import MusicPlayer #MusicPlayer — твой класс из другого файла

pygame.init()
#интерфейс (кнопки через клавиатуру + вывод текста)
# Window settings
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Music Player")

font = pygame.font.SysFont(None, 36) #шрифт для текста в окне
clock = pygame.time.Clock() #ограничение скорости цикла

# Create player
player = MusicPlayer("music") #ты передаёшь папку "music"

running = True

while running:#игра работает постоянно
    screen.fill((30, 30, 30)) #тёмно-серый фон

    for event in pygame.event.get():#проверка всех действий
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:#если нажали клавишу
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

    # Display current track показывает имя файла
    track_text = font.render(
        f"Current Track: {player.get_current_track_name()}",
        True,
        (255, 255, 255)
    )

    # Display playback position сколько секунд играет музыка
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

    pygame.display.flip()#обновление
    clock.tick(30)

pygame.quit()
sys.exit()
