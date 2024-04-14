import pygame
from datetime import datetime
import math

pygame.init()
screen = pygame.display.set_mode((1680, 1050))
clock = pygame.time.Clock()

def change_image(image, t):
    image_rotate = pygame.transform.rotate(image,360-t*6)
    return image_rotate
main_image = pygame.image.load('mainclock.png')
minute_arm = pygame.image.load('rightarm.png')
second_arm = pygame.image.load('leftarm.png')

def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
minute_angle = 360
second_angle = 360

t = datetime.now()

minute, second = t.minute, t.second
minutes = change_image(minute_arm, minute)
secundes = change_image(second_arm, second)
w,h = secundes.get_size()
w1,h1 = minutes.get_size()
while True:
    screen.blit(main_image,(0, 0))
    screen.blit(main_image, (840-main_image.get_width()/2,525-main_image.get_height()/2))
    blitRotate(screen, secundes, (840, 525), (w/2, h/2), second_angle)
    blitRotate(screen, minutes, (840, 525), (w1/2, h1/2), minute_angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    second_angle -=6
    minute_angle -=1/10
    pygame.display.flip()
    clock.tick(1)