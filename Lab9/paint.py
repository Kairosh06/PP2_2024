import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640

# Colors
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# Definition of figures
Figure_Square = 0
Figure_Right_Triangle = 1
Figure_equilateral_triangle = 2
Figure_Rhombus = 3

# Setting initial figure
current_figure = Figure_Square

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

done = False

LMBpressed = False

prevX = 0
prevY = 0

currX = 0
currY = 0

# Function to calculate square coordinates
def calculate_square(x1, y1, x2, y2):
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    side_length = max(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(min_x, min_y, side_length, side_length)

# Function to calculate right triangle coordinates
def calculate_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2)]

# Function to calculate equilateral triangle coordinates
def calculate_equilateral_triangle(x1, y1, x2, y2):
    return [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)]

# Function to calculate rhombus coordinates
def calculate_rhombus(x1, y1, x2, y2):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return [(center_x, y1), (x1, center_y), (center_x, y2), (x2, center_y)]

# Function to draw different figures based on their type
def draw_figure(screen, figure_type, color, start_pos, end_pos):
    if figure_type == Figure_Square:
        pygame.draw.rect(screen, color, calculate_square(start_pos[0], start_pos[1], end_pos[0], end_pos[1]), 2)
    elif figure_type == Figure_Right_Triangle:
        pygame.draw.polygon(screen, color, calculate_right_triangle(start_pos[0], start_pos[1], end_pos[0], end_pos[1]), 2)
    elif figure_type == Figure_equilateral_triangle:
        pygame.draw.polygon(screen, color, calculate_equilateral_triangle(start_pos[0], start_pos[1], end_pos[0], end_pos[1]), 2)
    elif figure_type == Figure_Rhombus:
        pygame.draw.polygon(screen, color, calculate_rhombus(start_pos[0], start_pos[1], end_pos[0], end_pos[1]), 2)

# Function to draw buttons for selecting figures
def draw_buttons():
    font = pygame.font.SysFont('Arial', 20)
    button_labels = ["Square", "Right Triangle", "Equilateral Triangle", "Rhombus"]
    for i, label in enumerate(button_labels):
        button_rect = pygame.Rect(10, 10 + i * 50, 150, 40)
        pygame.draw.rect(screen, colorWHITE, button_rect)
        pygame.draw.rect(screen, colorBLACK, button_rect, 2)
        text_surface = font.render(label, True, colorBLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

            # Check if button is clicked
            button_labels = ["Square", "Right Triangle", "Equilateral Triangle", "Rhombus"]
            for i, _ in enumerate(button_labels):
                button_rect = pygame.Rect(10, 10 + i * 50, 150, 40)
                if button_rect.collidepoint(event.pos):
                    current_figure = i
                    break

        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False
            draw_figure(screen, current_figure, colorYELLOW, (prevX, prevY), (currX, currY))
            base_layer.blit(screen, (0, 0))

    if LMBpressed:
        screen.blit(base_layer, (0, 0))
        draw_figure(screen, current_figure, colorYELLOW, (prevX, prevY), (currX, currY))

    draw_buttons()

    pygame.display.flip()