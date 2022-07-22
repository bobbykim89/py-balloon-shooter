import pygame

pygame.init() ## Initialization (required)

## Config screen size
screen_width = 480 ## Horizontal width
screen_height = 640 ## Vertical
screen = pygame.display.set_mode((screen_width, screen_height))

## Config screen title
pygame.display.set_caption("Balloon Shooter") ## Name of game

## Event loop
running = True # Check if game is running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## Emit on click on close btn
            running = False ## game is not running

## shutdown pygame
pygame.quit()