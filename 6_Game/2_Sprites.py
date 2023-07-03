import pygame
import os

pygame.init()

screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

game_path = os.path.dirname(__file__)

pygame.display.set_caption("ROY - SHOOTING GAME")

background = pygame.image.load(f"{game_path}/images/background.png")

# Character
char = pygame.image.load(f"{game_path}/images/character.png")
char_size = char.get_rect().size
char_w = char_size[0]
char_h = char_size[1]
char_x = screen_width/2 - char_w/2
char_y = screen_height - char_h



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rendering
    screen.blit(background, (0,0))
    screen.blit(char, (char_x, char_y))

    pygame.display.update()

pygame.quit()