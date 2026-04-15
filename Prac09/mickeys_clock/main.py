import pygame
import os
from clock import prepare_hand, get_angles

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Hello Kitty Clock ")
CENTER = (400, 400)

bg_path = os.path.join(IMAGES_DIR, 'mainclock.png')
bg = pygame.image.load(bg_path).convert_alpha()
bg = pygame.transform.scale(bg, (800, 800))

m_path = os.path.join(IMAGES_DIR, 'hour.jpg.jpeg')
s_path = os.path.join(IMAGES_DIR, 'second.jpg.jpeg')

m_img_raw = pygame.image.load(m_path).convert_alpha()
s_img_raw = pygame.image.load(s_path).convert_alpha()

m_hand = prepare_hand(m_img_raw)
s_hand = prepare_hand(s_img_raw)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    h_ang, m_ang, s_ang = get_angles()

    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    rot_m = pygame.transform.rotate(m_hand, m_ang)
    rect_m = rot_m.get_rect(center=CENTER)
    screen.blit(rot_m, rect_m)

    rot_s = pygame.transform.rotate(s_hand, s_ang)
    rect_s = rot_s.get_rect(center=CENTER)
    screen.blit(rot_s, rect_s)

    nose_rect = pygame.Rect(CENTER[0] - 40, CENTER[1] - 30, 80, 50) 
    pygame.draw.ellipse(screen, (255, 223, 0), nose_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()