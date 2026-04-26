import pygame
from collections import deque

# ---------- BASIC DRAW FUNCTIONS ----------

def draw_line(surface, start, end, color, width):
    pygame.draw.line(surface, color, start, end, width)


def draw_rect(surface, start, end, color, width):
    rect = pygame.Rect(
        min(start[0], end[0]),
        min(start[1], end[1]),
        abs(start[0] - end[0]),
        abs(start[1] - end[1])
    )
    pygame.draw.rect(surface, color, rect, width)


def draw_circle(surface, start, end, color, width):
    center = ((start[0]+end[0])//2, (start[1]+end[1])//2)
    radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5/2)
    pygame.draw.circle(surface, color, center, radius, width)


def draw_square(surface, start, end, color, width):
    side = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
    rect = pygame.Rect(start[0], start[1], side, side)
    pygame.draw.rect(surface, color, rect, width)


def draw_right_triangle(surface, start, end, color, width):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, width)


def draw_equilateral_triangle(surface, start, end, color, width):
    x1,y1 = start
    x2,y2 = end
    top = ((x1+x2)//2, min(y1,y2))
    left = (min(x1,x2), max(y1,y2))
    right = (max(x1,x2), max(y1,y2))
    pygame.draw.polygon(surface, color, [top,left,right], width)


def draw_rhombus(surface, start, end, color, width):
    x1,y1 = start
    x2,y2 = end
    cx = (x1+x2)//2
    cy = (y1+y2)//2
    points = [(cx,y1),(x2,cy),(cx,y2),(x1,cy)]
    pygame.draw.polygon(surface, color, points, width)


# ---------- FLOOD FILL ----------

def flood_fill(surface, start_pos, fill_color):
    width, height = surface.get_size()
    target_color = surface.get_at(start_pos)

    if target_color == fill_color:
        return

    queue = deque([start_pos])

    while queue:
        x,y = queue.popleft()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x,y)) != target_color:
            continue

        surface.set_at((x,y), fill_color)

        queue.append((x+1,y))
        queue.append((x-1,y))
        queue.append((x,y+1))
        queue.append((x,y-1))
