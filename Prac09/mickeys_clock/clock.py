import pygame
import datetime

def prepare_hand(image):
    w, h = image.get_size()
    new_surf = pygame.Surface((w, h * 2), pygame.SRCALPHA)
    new_surf.blit(image, (0, 0))
    return new_surf

def get_angles():
    now = datetime.datetime.now()
    
    s_angle = -now.second * 6
    m_angle = -now.minute * 6
    h_angle = -((now.hour % 12) * 30 + now.minute / 2)
    
    return h_angle, m_angle, s_angle