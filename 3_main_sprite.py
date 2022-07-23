import pygame

pygame.init() ## Initialization (required)

## Config screen size
screen_width = 480 ## Horizontal width
screen_height = 640 ## Vertical
screen = pygame.display.set_mode((screen_width, screen_height))

## Config screen title
pygame.display.set_caption("Balloon Shooter") ## Name of game

## Import background image
background = pygame.image.load("background.png")

## Import sprite(character)
character  = pygame.image.load("character.png")
character_size = character.get_rect().size # Get image size
character_width = character_size[0] ## horizontal size of character
character_height = character_size[1] ## vertical size of character
character_x_pos = (screen_width / 2) - (character_width / 2) ## place character in middle of horizontal screen width
character_y_pos = screen_height - character_height ## place character in bottom of screen vertical height

## Event loop
running = True # Check if game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Emit on click on close btn
            running = False ## game is not running
    
    # screen.fill((0, 0, 255)) ## Fill bg with rgb color
    screen.blit(background, (0, 0)) ## Apply background

    screen.blit(character, (character_x_pos, character_y_pos)) ## draw a character in location

    pygame.display.update() ## Refresh game screen

## shutdown pygame
pygame.quit()