# Making the user as a car
import pygame
import os, sys
from pygame.sprite import Sprite

class Car(pygame.sprite.Sprite):

    # Bring in those image assets so we have something to look at
    car_no = pygame.image.load("pixel.png")
    car_front = pygame.image.load('car_front.png')
    car_back = pygame.image.load('car_back.png')
    car_left = pygame.image.load('car_left.png')
    car_right = pygame.image.load('car_right.png')

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        # Gotta grab a "no car" look otherwise it sticks with you the whole game
        self.current_view = Car.car_no

        # What do you look like?
        self.image = self.current_view

        # Where are your goods?
        self.rect = self.image.get_rect()
        self.rect.center = pos

    # def image_selector(self, screen, image):
    #     screen.blit(image, (self.rect.x, self.rect.y))



class Passenger(pygame.sprite.Sprite):
    
    lisa = pygame.image.load('passenger_lisa.png')

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        # what do you look like?
        self.image = Passenger.lisa
        # be healthy, set boundaries
        self.rect = self.image.get_rect()
        self.rect.center = pos


    # def checkCollision(self, sprite1, sprite2):
    #     collision = pygame.sprite.collide_rect(sprite1, sprite2)
    #     if collision == True:
    #         sys.exit()
    
    # def image_selector(self, screen, image):
    #     screen.blit(image, (self.rect.x, self.rect.y))



