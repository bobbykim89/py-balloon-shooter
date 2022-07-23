import pygame

pygame.init() ## Initialization (required)

## Config screen size
screen_width = 480 ## Horizontal width
screen_height = 640 ## Vertical
screen = pygame.display.set_mode((screen_width, screen_height))

## Config screen title
pygame.display.set_caption("Balloon Shooter") ## Name of game

## FPS
clock = pygame.time.Clock()

## Import background image
background = pygame.image.load("background.png")

## Import sprite(character)
character  = pygame.image.load("character.png")
character_size = character.get_rect().size # Get image size
character_width = character_size[0] ## horizontal size of character
character_height = character_size[1] ## vertical size of character
character_x_pos = (screen_width / 2) - (character_width / 2) ## place character in middle of horizontal screen width
character_y_pos = screen_height - character_height ## place character in bottom of screen vertical height

## Coordinates for character movement
to_x = 0
to_y = 0

## movement speed
character_speed = 0.6

## Event loop
running = True # Check if game is running
while running:
    dt = clock.tick(60) # set game FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Emit on click on close btn
            running = False ## game is not running
        
        if event.type == pygame.KEYDOWN: # Check if key is pressed
            if event.key == pygame.K_LEFT: # move character to left
                to_x -= character_speed # to_x = to_x - character_speed
            elif event.key == pygame.K_RIGHT: # move character to right
                to_x += character_speed # to_x = to_x + character_speed
            elif event.key == pygame.K_UP: # move char upward
                to_y -= character_speed # to_y = to_y - character_speed
            elif event.key == pygame.K_DOWN: # move char downward
                to_y += character_speed # to_y = to_y + character_speed
        if event.type == pygame.KEYUP: # stop on key up
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: ## key up for left right
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # horizontal position constraint
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # vertical position constraint
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # screen.fill((0, 0, 255)) ## Fill bg with rgb color
    screen.blit(background, (0, 0)) ## Apply background

    screen.blit(character, (character_x_pos, character_y_pos)) ## draw a character in location

    pygame.display.update() ## Refresh game screen

## shutdown pygame
pygame.quit()