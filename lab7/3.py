import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_pos = [WIDTH // 2, HEIGHT // 2] 
ball_radius = 25
ball_speed = 20  

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the ball based on arrow key input
            if event.key == pygame.K_UP:
                ball_pos[1] = max(ball_pos[1] - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_pos[1] = min(ball_pos[1] + ball_speed, HEIGHT - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_pos[0] = max(ball_pos[0] - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] = min(ball_pos[0] + ball_speed, WIDTH - ball_radius)

    # Draw everything
    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)  # Draw the ball

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()