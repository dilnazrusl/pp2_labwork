import pygame
import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 1300, 750
TOOLBAR_WIDTH = 200
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
DARKGRAY = (150,150,150)

COLORS = [
    (0,0,0),(255,0,0),(0,255,0),(0,0,255),
    (255,255,0),(255,0,255),(0,255,255)
]

# MODES
PENCIL = 1
LINE = 2
RECT = 3
CIRCLE = 4
SQUARE = 5
RT_TRI = 6
EQ_TRI = 7
RHOMBUS = 8
FILL = 9
TEXT = 10
ERASER = 11

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Advanced Paint")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

canvas = pygame.Surface((WIDTH-TOOLBAR_WIDTH, HEIGHT))
canvas.fill(WHITE)

mode = PENCIL
color = BLACK
brush_size = 5

drawing = False
start_pos = None
last_pos = None

text_mode = False
text_input = ""
text_pos = (0,0)


def draw_button(rect, text, active=False):
    pygame.draw.rect(screen, DARKGRAY if active else GRAY, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    txt = font.render(text, True, BLACK)
    screen.blit(txt, (rect.x+5, rect.y+5))


running = True
while running:
    screen.fill(GRAY)
    screen.blit(canvas, (TOOLBAR_WIDTH,0))

    # --- TOOLBAR ---
    y = 20
    buttons = {}

    tool_names = [
        ("Pencil",PENCIL),
        ("Line",LINE),
        ("Rect",RECT),
        ("Circle",CIRCLE),
        ("Square",SQUARE),
        ("R.Tri",RT_TRI),
        ("E.Tri",EQ_TRI),
        ("Rhombus",RHOMBUS),
        ("Fill",FILL),
        ("Text",TEXT),
        ("Eraser",ERASER)
    ]

    for name, m in tool_names:
        rect = pygame.Rect(20,y,160,30)
        draw_button(rect,name,mode==m)
        buttons[m]=rect
        y+=40

    clear_rect = pygame.Rect(20,y+10,160,30)
    draw_button(clear_rect,"Clear All")

    # Color palette
    y+=60
    color_rects=[]
    for col in COLORS:
        rect = pygame.Rect(20,y,30,30)
        pygame.draw.rect(screen,col,rect)
        pygame.draw.rect(screen,BLACK,rect,2)
        color_rects.append((rect,col))
        y+=40

    # Brush size buttons
    size_buttons=[]
    sizes=[2,5,10]
    y+=10
    for s in sizes:
        rect = pygame.Rect(20,y,50,30)
        draw_button(rect,f"{s}px",brush_size==s)
        size_buttons.append((rect,s))
        y+=40

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my = event.pos

            # Toolbar clicks
            if mx < TOOLBAR_WIDTH:
                for m,rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        mode=m

                if clear_rect.collidepoint(event.pos):
                    canvas.fill(WHITE)

                for rect,col in color_rects:
                    if rect.collidepoint(event.pos):
                        color=col

                for rect,s in size_buttons:
                    if rect.collidepoint(event.pos):
                        brush_size=s
            else:
                drawing=True
                start_pos=(mx-TOOLBAR_WIDTH,my)
                last_pos=start_pos

                if mode==FILL:
                    flood_fill(canvas,start_pos,color)

                if mode==TEXT:
                    text_mode=True
                    text_input=""
                    text_pos=start_pos

        if event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            if mx>=TOOLBAR_WIDTH:
                end=(event.pos[0]-TOOLBAR_WIDTH,event.pos[1])

                if mode==LINE:
                    draw_line(canvas,start_pos,end,color,brush_size)
                elif mode==RECT:
                    draw_rect(canvas,start_pos,end,color,brush_size)
                elif mode==CIRCLE:
                    draw_circle(canvas,start_pos,end,color,brush_size)
                elif mode==SQUARE:
                    draw_square(canvas,start_pos,end,color,brush_size)
                elif mode==RT_TRI:
                    draw_right_triangle(canvas,start_pos,end,color,brush_size)
                elif mode==EQ_TRI:
                    draw_equilateral_triangle(canvas,start_pos,end,color,brush_size)
                elif mode==RHOMBUS:
                    draw_rhombus(canvas,start_pos,end,color,brush_size)

        if event.type==pygame.MOUSEMOTION and drawing:
            mx,my=event.pos
            if mx>=TOOLBAR_WIDTH:
                current=(mx-TOOLBAR_WIDTH,my)

                if mode==PENCIL:
                    draw_line(canvas,last_pos,current,color,brush_size)
                    last_pos=current

                if mode==ERASER:
                    draw_line(canvas,last_pos,current,WHITE,brush_size)
                    last_pos=current

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_s and pygame.key.get_mods()&pygame.KMOD_CTRL:
                timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                pygame.image.save(canvas,f"painting_{timestamp}.png")

            if text_mode:
                if event.key==pygame.K_RETURN:
                    txt=font.render(text_input,True,color)
                    canvas.blit(txt,text_pos)
                    text_mode=False
                elif event.key==pygame.K_ESCAPE:
                    text_mode=False
                elif event.key==pygame.K_BACKSPACE:
                    text_input=text_input[:-1]
                else:
                    text_input+=event.unicode

    if text_mode:
        txt=font.render(text_input,True,color)
        screen.blit(txt,(text_pos[0]+TOOLBAR_WIDTH,text_pos[1]))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
