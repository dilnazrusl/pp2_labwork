import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))#создаём окно размером 1200x700
WHITE = (0, 0, 0)#задаём цвета (RGB):
RED = (0, 0, 255)

done = False


clock = pygame.time.Clock()#онтролирует FPS (скорость игры)

circle_start_w = 600
circle_start_h = 350
#это центр мяча:

while not done:#игра работает бесконечно
    
    keys = pygame.key.get_pressed()#считываем ВСЕ нажатые клавиши
    pygame.draw.circle(screen, RED, (circle_start_w, circle_start_h), 25)# можем сделать квадрат rect
    for event in pygame.event.get():#если нажали крестик → игра закрывается
        if event.type == pygame.QUIT:
            done = True
    if keys[pygame.K_UP]:#если нажата стрелка вверх
        if (circle_start_h > 38):#проверка границы (чтобы не выйти за экран)
            circle_start_h -= 10 #двигаем вверх (уменьшаем y)
    if keys[pygame.K_DOWN]:
        if (circle_start_h < 662):
            circle_start_h += 10 #увеличиваем y → вниз
    if keys[pygame.K_LEFT]:
        if (circle_start_w > 38):
            circle_start_w -= 10 #уменьшаем x
    if keys[pygame.K_RIGHT]:
        if (circle_start_w < 1162):
            circle_start_w += 10 #увеличиваем x
    
    screen.fill(WHITE) #screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (circle_start_w, circle_start_h), 25)
    pygame.display.flip() #показывает изменения
    clock.tick(60)  