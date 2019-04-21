# Import Modules
import pygame
# # # from pygame.sprite import Group, groupcollide

# Import local files
from car import Car
from background import Background
from undrivable import Undrivable

# Let's get started
pygame.init()

# Screen dimensions
screen_size = (600, 500)
screen = pygame.display.set_mode(screen_size)

# Declare your shit images, objects
player_1 = Car("Uber")
background = Background(screen, "Atlanta_1_base.png")
foreground = Background(screen, "Atlanta_1_trafficlights.png")

#############
# Game Loop #
#############
game_on = True
while game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == 274:
                background.move('up', True)
                foreground.move('up', True)
                player_1.current_view = player_1.car_back
            elif event.key == 273:
                background.move('down', True)
                foreground.move('down', True)
                player_1.current_view = player_1.car_front
            elif event.key == 275:
                background.move('right', True)
                foreground.move('right', True)
                player_1.current_view =  player_1.car_right
            elif event.key == 276:
                background.move('left', True)
                foreground.move('left', True)
                player_1.current_view =  player_1.car_left
        elif event.type == pygame.KEYUP:
            if event.key == 274:
                background.move('up', False)
                foreground.move('up', False)
            elif event.key == 273:
                background.move('down', False)
                foreground.move('down', False)
            elif event.key == 275:
                background.move('right', False)
                foreground.move('right', False)
            elif event.key == 276:
                background.move('left', False)
                foreground.move('left', False)

    # Redraw what's ben done
    background.draw_background()
    foreground.draw_background()
    screen.blit(player_1.current_view, [player_1.x, player_1.y])
    player_1.image_selector(screen, player_1.current_view)
    
    pygame.display.update()