# import pygame
# from pygame.sprite import Sprite
# class Undrivable(object):

#     # car_front = pygame.image.load('car_front.png')
#     # car_back = pygame.image.load('car_back.png')
#     # car_left = pygame.image.load('car_left.png')
#     # car_right = pygame.image.load('car_right.png')
#     undrive = pygame.image.load('background_novis_undrivablesurface.png')

#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.current_view = Undrivable.undrive

#     def image_selector(self, screen, image):
#         screen.blit(image, [self.x, self.y])

# Making the background map magic
import pygame

class Undrivable(object):
    def __init__(self, screen, image):
        self.x = 0
        self.y = 0
        self.speed = 7
        self.screen = screen
        self.image = pygame.image.load(image)
        self.move_down = False
        self.move_up = False
        self.move_left = False
        self.move_right = False

    # # # draw_background?? - - - For out of bound movement
    def draw_undrivable(self):
        # pass
        if self.move_right:
            if self.x >= -1130:
                self.x -= self.speed
        elif self.move_left:
            if self.x <= 180:
                self.x += self.speed
        elif self.move_up:
            if self.y >= -1050:
                self.y -= self.speed
        elif self.move_down:
            if self.y <= 100:
                self.y += self.speed
        self.screen.blit(self.image, [self.x, self.y])        

    def move(self, direction, boogie_bool):
        if direction == "left":
            self.move_left = boogie_bool
        elif direction == "right":
            self.move_right = boogie_bool
        elif direction == "up":
            self.move_up = boogie_bool
        elif direction == "down":
            self.move_down = boogie_bool
    
    # # # ???
    def overlay_int(self, screen, image):
        screen.blit(image, [0,0])