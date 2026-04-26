import pygame

#CONSTANTS
WIDTH, HEIGHT = 1200, 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

# MODES
LINE = 1
RECT = 2
CIRCLE = 3
SQUARE = 4
RT_TRIANGLE = 5
EQ_TRIANGLE = 6
RHOMBUS = 7


def draw_line(screen, points, color, width):
    for i in range(len(points) - 1):
        pygame.draw.line(screen, color, points[i], points[i + 1], width)


def draw_rectangle(screen, start, end, color, width):
    rect = pygame.Rect(
        min(start[0], end[0]),
        min(start[1], end[1]),
        abs(start[0] - end[0]),
        abs(start[1] - end[1])
    )
    pygame.draw.rect(screen, color, rect, width)


def draw_circle(screen, start, end, color, width):
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5 / 2)
    pygame.draw.circle(screen, color, center, radius, width)


# КВАДРАТ
def draw_square(screen, start, end, color, width):
    side = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], side, side)
    pygame.draw.rect(screen, color, rect, width)


#ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК
def draw_right_triangle(screen, start, end, color, width):
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    pygame.draw.polygon(screen, color, points, width)


# РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК
def draw_equilateral_triangle(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end

    top = ((x1 + x2) // 2, min(y1, y2))
    left = (min(x1, x2), max(y1, y2))
    right = (max(x1, x2), max(y1, y2))

    pygame.draw.polygon(screen, color, [top, left, right], width)


# РОМБ
def draw_rhombus(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(screen, color, points, width)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint - Improved")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # STATE
    drawing = False
    mode = LINE
    color = COLORS['blue']
    radius = 5

    points = []
    shapes = []

    start_pos = None

    #COLOR BUTTONS
    red_btn = pygame.Rect(20, 150, 30, 30)
    green_btn = pygame.Rect(20, 200, 30, 30)
    blue_btn = pygame.Rect(20, 250, 30, 30)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #KEYBOARD
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_l:
                    mode = LINE
                elif event.key == pygame.K_z:
                    mode = RECT
                elif event.key == pygame.K_x:
                    mode = CIRCLE
                elif event.key == pygame.K_s:
                    mode = SQUARE
                elif event.key == pygame.K_t:
                    mode = RT_TRIANGLE
                elif event.key == pygame.K_e:
                    mode = EQ_TRIANGLE
                elif event.key == pygame.K_r:
                    mode = RHOMBUS
                elif event.key == pygame.K_c:
                    color = BLACK  # eraser
                elif event.key == pygame.K_a:
                    shapes.clear()

            # MOUSE DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    points = [event.pos]

                    if red_btn.collidepoint(event.pos):
                        color = COLORS['red']
                        drawing = False
                    elif green_btn.collidepoint(event.pos):
                        color = COLORS['green']
                        drawing = False
                    elif blue_btn.collidepoint(event.pos):
                        color = COLORS['blue']
                        drawing = False

            #MOUSE UP 
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False

                    if mode == LINE:
                        shapes.append(("line", points.copy(), color, radius))
                    else:
                        shapes.append((mode, start_pos, event.pos, color, radius))

            #MOUSE MOVE
            if event.type == pygame.MOUSEMOTION:
                if drawing and mode == LINE:
                    points.append(event.pos)

        #DRAW SAVED SHAPES
        for shape in shapes:
            if shape[0] == "line":
                _, pts, col, rad = shape
                draw_line(screen, pts, col, rad)
            elif shape[0] == RECT:
                _, s, e, col, rad = shape
                draw_rectangle(screen, s, e, col, rad)
            elif shape[0] == CIRCLE:
                _, s, e, col, rad = shape
                draw_circle(screen, s, e, col, rad)
            elif shape[0] == SQUARE:
                _, s, e, col, rad = shape
                draw_square(screen, s, e, col, rad)
            elif shape[0] == RT_TRIANGLE:
                _, s, e, col, rad = shape
                draw_right_triangle(screen, s, e, col, rad)
            elif shape[0] == EQ_TRIANGLE:
                _, s, e, col, rad = shape
                draw_equilateral_triangle(screen, s, e, col, rad)
            elif shape[0] == RHOMBUS:
                _, s, e, col, rad = shape
                draw_rhombus(screen, s, e, col, rad)

        #DRAW CURRENT SHAPE
        if drawing:
            end = pygame.mouse.get_pos()
            if mode == LINE:
                draw_line(screen, points, color, radius)
            elif mode == RECT:
                draw_rectangle(screen, start_pos, end, color, radius)
            elif mode == CIRCLE:
                draw_circle(screen, start_pos, end, color, radius)
            elif mode == SQUARE:
                draw_square(screen, start_pos, end, color, radius)
            elif mode == RT_TRIANGLE:
                draw_right_triangle(screen, start_pos, end, color, radius)
            elif mode == EQ_TRIANGLE:
                draw_equilateral_triangle(screen, start_pos, end, color, radius)
            elif mode == RHOMBUS:
                draw_rhombus(screen, start_pos, end, color, radius)

        # UI
        mode_name = {
            LINE: "Line",
            RECT: "Rectangle",
            CIRCLE: "Circle",
            SQUARE: "Square",
            RT_TRIANGLE: "Right Triangle",
            EQ_TRIANGLE: "Equilateral Triangle",
            RHOMBUS: "Rhombus"
        }[mode]

        text = font.render(
            "L-Line Z-Rect X-Circle S-Square T-RightTri E-EquiTri R-Rhombus C-Eraser A-Clear",
            True, WHITE
        )

        screen.blit(font.render(f"Mode: {mode_name}", True, WHITE), (10, 10))
        screen.blit(text, (10, 40))

        # COLOR BUTTONS
        pygame.draw.rect(screen, COLORS['red'], red_btn)
        pygame.draw.rect(screen, COLORS['green'], green_btn)
        pygame.draw.rect(screen, COLORS['blue'], blue_btn)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


main()