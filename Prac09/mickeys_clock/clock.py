import pygame
import datetime
# берём текущее время (datetime)

def prepare_hand(image):#функция готовит изображение стрелки
    w, h = image.get_size()#берём ширину и высоту картинки стрелки
    new_surf = pygame.Surface((w, h * 2), pygame.SRCALPHA)#создаём новую поверхность (чтобы стрелка правильно вращалась)
    new_surf.blit(image, (0, 0))
    return new_surf

def get_angles():
    now = datetime.datetime.now()
    #минус - потому что pygame крутит по часовой в другую сторону
    s_angle = -now.minute * 6
    m_angle = -((now.hour % 12) * 30 + now.minute / 2)
    h_angle = -((now.hour % 12) * 30 + now.minute / 2)
    
    return h_angle, m_angle, s_angle