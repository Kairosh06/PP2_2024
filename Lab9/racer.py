import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

N = 5
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("C:\\Users\\Kairosh\\Desktop\\Lab9\\images\\AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\\Users\\Kairosh\\Desktop\\Lab9\\images\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\\Users\\Kairosh\\Desktop\\Lab9\\images\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("C:\\Users\\Kairosh\\Desktop\\Lab9\\images\\coin.png")
        self.image = pygame.transform.scale(original_image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, SCREEN_WIDTH - 25), 0)
        self.collected = False
        self.speed = SPEED
        self.weight = random.randint(1, 3)  # Случайный вес монеты от 1 до 3

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 600:
            self.reset()

    def reset(self):
        self.rect.topleft = (random.randint(0, SCREEN_WIDTH - 25), 0)
        self.collected = False

                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_EVENT, 4000) 

collected_coins_counter = 0

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == COIN_EVENT:
            new_coin = Coin()
            coins.add(new_coin)
            if collected_coins_counter % N == 0 and collected_coins_counter != 0:
                SPEED += 0.5

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    collected_coins_text = font_small.render(f"Collected Coins: {collected_coins_counter}", True, BLACK)  
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(collected_coins_text, (200, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect)
        coin.move()

        if pygame.sprite.collide_rect(coin, P1):
            collected_coins_counter += 1
            SCORE += coin.weight
            coins.remove(coin) 
            coin.reset() 

    #To be run if collision occurs between Player and Enemy
    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound("C:\\Users\\Kairosh\\Desktop\\Lab9\\images\\crash.wav").play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)