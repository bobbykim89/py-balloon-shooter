import pygame

############################################################
## Basic Initialization
pygame.init() ## Initialization (required)

## Config screen size
screen_width = 480 ## Horizontal width
screen_height = 640 ## Vertical
screen = pygame.display.set_mode((screen_width, screen_height))

## Config screen title
pygame.display.set_caption("Balloon Shooter") ## Name of game

## FPS
clock = pygame.time.Clock()
############################################################

## 1. Play game initialization (Background, game image, coordinate, font)

## Event loop
running = True # Check if game is running
while running:
    dt = clock.tick(60) # set game FPS

    ## 2. Process Event (Key events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Emit on click on close btn
            running = False ## game is not running
        
    ## 3. Define game char location

    ## 4. Process Collision

    ## 5. Draw on screen

    pygame.display.update() ## Refresh game screen

pygame.quit()