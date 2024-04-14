import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640

# color palette
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)

done = False

LMBpressed = False

prevX = 0
prevY = 0

currX = 0
currY = 0

draw_mode = 'rectangle'  # Default draw mode
current_color = colorBLACK  # Default color

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(x1, y1, x2, y2):
    center = ((x1 + x2) // 2, (y1 + y2) // 2)
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5) // 2
    return center, radius

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos

        if event.type == pygame.MOUSEMOTION:
            currX, currY = event.pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if draw_mode == 'rectangle':
                pygame.draw.rect(base_layer, current_color, calculate_rect(prevX, prevY, currX, currY), 2)
            elif draw_mode == 'circle':
                pygame.draw.circle(base_layer, current_color, calculate_circle(prevX, prevY, currX, currY)[0], calculate_circle(prevX, prevY, currX, currY)[1], 2)
            elif draw_mode == 'eraser':
                pygame.draw.rect(base_layer, colorWHITE, calculate_rect(prevX, prevY, currX, currY))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                draw_mode = 'rectangle'
            elif event.key == pygame.K_c:
                draw_mode = 'circle'
            elif event.key == pygame.K_e:
                draw_mode = 'eraser'
            elif event.key == pygame.K_1:
                current_color = colorRED
            elif event.key == pygame.K_2:
                current_color = colorGREEN
            elif event.key == pygame.K_3:
                current_color = colorBLUE

    screen.blit(base_layer, (0, 0))
    if LMBpressed:
        if draw_mode == 'rectangle':
            pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), 2)
        elif draw_mode == 'circle':
            pygame.draw.circle(screen, current_color, calculate_circle(prevX, prevY, currX, currY)[0], calculate_circle(prevX, prevY, currX, currY)[1], 2)
        elif draw_mode == 'eraser':
            pygame.draw.rect(screen, colorWHITE, calculate_rect(prevX, prevY, currX, currY))

    pygame.display.flip()