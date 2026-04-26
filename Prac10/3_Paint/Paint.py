import pygame

# --- CONSTANTS ---
WIDTH, HEIGHT = 1200, 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

# MODES Это просто номера режимов рисования.
LINE = 1
RECT = 2
CIRCLE = 3


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


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint - Improved")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # --- STATE ---
    drawing = False
    mode = LINE
    color = COLORS['blue']
    radius = 5

    points = []
    shapes = []

    start_pos = None

    # --- COLOR BUTTONS ---
    red_btn = pygame.Rect(20, 150, 30, 30)
    green_btn = pygame.Rect(20, 200, 30, 30)
    blue_btn = pygame.Rect(20, 250, 30, 30)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- KEYBOARD ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_l:
                    mode = LINE
                elif event.key == pygame.K_z:
                    mode = RECT
                elif event.key == pygame.K_x:
                    mode = CIRCLE
                elif event.key == pygame.K_c:
                    color = BLACK  # eraser
                elif event.key == pygame.K_a:
                    shapes.clear()

            # --- MOUSE DOWN ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True #Когда ты нажимаешь мышь:
                    start_pos = event.pos #event.pos — координаты курсора.
                    points = [event.pos]

                    # color buttons
                    if red_btn.collidepoint(event.pos):
                        color = COLORS['red']
                        drawing = False
                    elif green_btn.collidepoint(event.pos):
                        color = COLORS['green']
                        drawing = False
                    elif blue_btn.collidepoint(event.pos):
                        color = COLORS['blue']
                        drawing = False

            #  MOUSE UP Если кнопка зажата → программа записывает новые точки.
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False

                    if mode == LINE: #Фигура сохраняется в список shapes. shapes = []  список всех нарисованных фигур.
                        shapes.append(("line", points.copy(), color, radius))
                    else:
                        shapes.append((mode, start_pos, event.pos, color, radius)) #Фигура сохраняется.

            # --- MOUSE MOVE ---
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode == LINE:
                        points.append(event.pos)

        # --- DRAW SAVED SHAPES ---
        for shape in shapes:
            if shape[0] == "line":
                _, pts, col, rad = shape
                draw_line(screen, pts, col, rad)
            elif shape[0] == RECT:
                _, start, end, col, rad = shape
                draw_rectangle(screen, start, end, col, rad)
            elif shape[0] == CIRCLE:
                _, start, end, col, rad = shape
                draw_circle(screen, start, end, col, rad)

        # --- DRAW CURRENT SHAPE ---
        if drawing:
            if mode == LINE:
                draw_line(screen, points, color, radius)
            elif mode == RECT:
                draw_rectangle(screen, start_pos, pygame.mouse.get_pos(), color, radius)
            elif mode == CIRCLE:
                draw_circle(screen, start_pos, pygame.mouse.get_pos(), color, radius)

        # --- UI TEXT ---
        mode_name = {LINE: "Line", RECT: "Rectangle", CIRCLE: "Circle"}[mode]
        color_name = "Eraser" if color == BLACK else [k for k, v in COLORS.items() if v == color][0]

        text1 = font.render(f"Mode: {mode_name}", True, WHITE)
        text2 = font.render(f"Color: {color_name}", True, WHITE)
        text3 = font.render("L-Line | Z-Rect | X-Circle | C-Eraser | A-Clear", True, WHITE)

        screen.blit(text1, (10, 10))
        screen.blit(text2, (10, 40))
        screen.blit(text3, (10, 70))

        # --- DRAW COLOR BUTTONS ---
        pygame.draw.rect(screen, COLORS['red'], red_btn)
        pygame.draw.rect(screen, COLORS['green'], green_btn)
        pygame.draw.rect(screen, COLORS['blue'], blue_btn)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


main()