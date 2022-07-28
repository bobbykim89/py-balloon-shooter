import pygame

############################################################
## Basic Initialization
pygame.init() ## Initialization (required)

## Config screen size
screen_width = 480 ## Horizontal width
screen_height = 640 ## Vertical
screen = pygame.display.set_mode((screen_width, screen_height))

## Config screen title
pygame.display.set_caption("Run away from poo") ## Name of game

## FPS
clock = pygame.time.Clock()
############################################################

## 1. Play game initialization (Background, game image, coordinate, font)
# Create background
background = pygame.image.load('background.png')

# Create character
character =pygame.image.load('character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Movement coordinate
to_x = 0
character_speed = 10

## Event loop
running = True # Check if game is running
while running:
    dt = clock.tick(60) # set game FPS

    ## 2. Process Event (Key events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Emit on click on close btn
            running = False ## game is not running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    ## 3. Define game char location
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ## 4. Process Collision

    ## 5. Draw on screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() ## Refresh game screen

pygame.quit()