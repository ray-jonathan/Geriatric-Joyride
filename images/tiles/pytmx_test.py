# # # import pytmx
# # # tmxdata = pytmx.TiledMap("Atlanta_1.tmx")

# # from pytmx.util_pygame import load_pygame
# # tiled_map = load_pygame('Atlanta_1.tmx')

# import time
# import pygame
# import pytmx


# class TiledMap():
# # This is creating the surface on which you make the draw updates """
#     def __init__(self):
#         self.gameMap = pytmx.load_pygame("Atlanta_1.tmx", pixelalpha=True)
#         self.mapwidth = self.gameMap.tilewidth * self.gameMap.width
#         self.mapheight = self.gameMap.tileheight * self.gameMap.height

#     def render(self, surface):
#         for layer in self.gameMap.visible_layers:
#             if isinstance(layer, pytmx.TiledTileLayer):
#                 for x, y, gid in layer:
#                     tile = self.gameMap.get_tile_image_by_gid(gid)
#                     if tile:
#                         surface.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

#     def make_map(self):
#         mapSurface = pygame.Surface((self.mapwidth, self.mapheight))
#         self.render(mapSurface)
#         return mapSurface

# pygame.init()


# class Display():
# # This is the class that makes the changes that you want to display. You would add most of your changes here. """

#     def __init__(self):

#         self.displayRunning = True
#         self.displayWindow = pygame.display.set_mode((1584, 1584))
#         self.clock = pygame.time.Clock()

#     def update(self):

#         pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
#         pygame.display.update()

#     def loadMap(self):

#         self.map = TiledMap()
#         self.map_img = self.map.make_map()
#         self.map_rect = self.map_img.get_rect()

#     def displayLoop(self):

#         self.clock.tick()
#         self.update()
#         self.loadMap()

# # Here is the start of the main driver


# runDisplay = Display()

# runDisplay.update()
# runDisplay.loadMap()
# time.sleep(60)

import pygame
from pytmx import load_pygame
import random


white = (255,255,255)


#create window
screenSize = (800,600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("GameName")
screen.fill(white)


gameMap = load_pygame("Atlanta_1.tmx")


#creates list of single tiles in first layer
images = []

for y in range(50):
    for x in range(50):
        image = gameMap.get_tile_image(x,y,0)
        images.append(image)

#blit all tiles onto the screen
i = 0 #runs from 0 to 2600

for y in range(50):
    for x in range(50):
        screen.blit(images[i],(x * 32, y * 32))
        i += 1



#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()