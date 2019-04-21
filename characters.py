import pygame
import random
import time
BLACK = (0,0,0)
BLUE = (0, 0, 255)
WIDTH = 400
HEIGHT = 400

###############################
#### FIRST ROUND MATERIALS ####
###############################
class Intro(pygame.sprite.Sprite):
    logo_2 = pygame.image.load('title_2.png')
    logo_4 = pygame.image.load('title_4.png')
    instructions_1 = pygame.image.load('instructions_1.png')
    instructions_2 = pygame.image.load('instructions_2.png')
    logo_animation_list = [logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_2,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4,logo_4]
    counter = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        logo = pygame.image.load('title_2.png').convert()
        self.current_view = Intro.logo_2.convert()
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH/5)
        self.rect.y = (HEIGHT/4)

    def update(self): # any code here will happen every time the game loop updates
        self.current_view = Intro.logo_animation_list[Intro.counter]
        Intro.counter = (Intro.counter + 1) % len(Intro.logo_animation_list)
        self.image = self.current_view.convert_alpha()

class Intro_Instruct(pygame.sprite.Sprite):
    instructions_1 = pygame.image.load('instructions_1.png')
    instructions_2 = pygame.image.load('instructions_2.png')
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        title = pygame.image.load('instructions_1.png').convert_alpha()
        self.current_view = Intro.instructions_1.convert_alpha()
        self.image = self.current_view
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH/8)
        self.rect.y = (HEIGHT- (HEIGHT/4))

    def update(self): # any code here will happen every time the game loop updates
        # Grabbing keyboard input and modifying direction/orientation
        keystate = pygame.key.get_pressed()
        if (keystate[pygame.K_LEFT] or keystate[pygame.K_RIGHT] or keystate[pygame.K_UP] or keystate[pygame.K_DOWN]):
        # if event.key == pygame.ANYKEYPRESS:
            self.current_view = Intro.instructions_2.convert_alpha()
            self.image = self.current_view

        # Intro.counter = (Intro.counter + 1) % len(Intro.logo_animation_list)
        self.image = self.current_view
        # # self.image.set_colorkey(BLACK)

class Player_Round_1(pygame.sprite.Sprite):
    # Car's different assets
    car_no = pygame.image.load("pixel.png")
    mort_front_1 = pygame.image.load('old_man_mort_down_1.png')
    mort_front_2 = pygame.image.load('old_man_mort_down_2.png')
    mort_front_3 = pygame.image.load('old_man_mort_down_3.png')
    mort_images_front = [mort_front_1, mort_front_2, mort_front_3]
    mort_back_1 = pygame.image.load('old_man_mort_up_1.png')
    mort_back_2 = pygame.image.load('old_man_mort_up_2.png')
    mort_back_3 = pygame.image.load('old_man_mort_up_3.png')
    mort_images_back = [mort_back_1, mort_back_2, mort_back_3]
    mort_left_1 = pygame.image.load('old_man_mort_left_1.png')
    mort_left_2 = pygame.image.load('old_man_mort_left_2.png')
    mort_left_3 = pygame.image.load('old_man_mort_left_3.png')
    mort_images_left = [mort_left_1, mort_left_2, mort_left_3]
    mort_right_1 = pygame.image.load('old_man_mort_right_1.png')
    mort_right_2 = pygame.image.load('old_man_mort_right_2.png')
    mort_right_3 = pygame.image.load('old_man_mort_right_3.png')
    mort_images_right = [mort_right_1, mort_right_2, mort_right_3]
    counter = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Setting intial condition for Old Man Mort, before we start moving
        self.current_view = Player_Round_1.mort_back_1.convert()
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)
        # Setting boundaries
        self.rect = self.image.get_rect()
        # Start off on the center of the screen
        self.rect.center = (WIDTH / 2, (HEIGHT / 2) + 32)
        self.speed_x = 0
        self.speed_y = 0

    def update(self): # any code here will happen every time the game loop updates
        # Grabbing keyboard input and modifying direction/orientation
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -1
            self.speed_y = 0
        elif keystate[pygame.K_RIGHT]:
            self.speed_x = 1
            self.speed_y = 0
        elif keystate[pygame.K_DOWN]:
            self.speed_x = 0
            self.speed_y = 1
        elif keystate[pygame.K_UP]:
            self.speed_x = 0
            self.speed_y = -1
        # Making the walls the boundaries
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        # You did the math, now update the speeds
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Change orientation? Update the image (and animate!)
        if self.speed_x < 0:
            self.current_view = Player_Round_1.mort_images_left[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_left)
        elif self.speed_x > 0:
            self.current_view = Player_Round_1.mort_images_right[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_right)
        if self.speed_y < 0:
            self.current_view = Player_Round_1.mort_images_back[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_back)
        elif self.speed_y > 0:
            self.current_view = Player_Round_1.mort_images_front[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_front)
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)
class Pedestrians_Round_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        car_left = pygame.image.load('car_left.png')
        self.image = car_left
        self.image.set_colorkey(BLACK)
        # Setting boundaries
        self.rect = self.image.get_rect()
        # Spawning attributes for Round One Car (top center of window)
        self.rect.x = (WIDTH / 2 - 32)
        self.rect.y = (32)

###############################
#### LATER ROUND MATERIALS ####
###############################

class Buildings(pygame.sprite.Sprite):
    building_1 = pygame.image.load('building_1.png')
    building_2 = pygame.image.load('building_2.png')
    existing_x_coords = []
    existing_x_right_coords = []
    shitty_list_of_x_ranges = []
    existing_y_coords = []
    existing_y_bottom_coords = []
    shitty_list_of_y_ranges = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        for record in Buildings.existing_x_coords:
            right_bound = record + 48
            Buildings.existing_x_right_coords.append(right_bound)
        for coord_1 in Buildings.existing_x_coords:
            for coord_2 in Buildings.existing_x_right_coords:
                for i in (range(coord_1, coord_2)):
                    Buildings.shitty_list_of_x_ranges.append(i)

        for record in Buildings.existing_y_coords:
            bottom_bound = record + 80
            Buildings.existing_y_bottom_coords.append(bottom_bound)
        for coord_1 in Buildings.existing_y_coords:
            for coord_2 in Buildings.existing_y_bottom_coords:
                for i in (range(coord_1, coord_2)):
                    Buildings.shitty_list_of_y_ranges.append(i)
        print("Here are your shitty ranges: %s" % Buildings.shitty_list_of_x_ranges)
        self.image = random.choice((Buildings.building_1, Buildings.building_2)).convert_alpha()
        # Setting boundaries
        self.rect = self.image.get_rect()
        # Spawning attributes for buildings are random on the page
        self.rect.x = random.randrange(48, WIDTH - 48)
        self.rect.y = random.randrange(80, HEIGHT -80 )
        for record in Buildings.existing_x_coords:
            for range_x in list(range(record, (record + 48))):
                if self.rect.x != range_x:
                    self.rect.x = random.randrange(48, WIDTH - 48)
                else: 
                    self.rect.x = (WIDTH - 48)
        for record in Buildings.existing_y_coords:
            for range_y in list(range(record, (record + 80))):
                if self.rect.y != range_y:
                    self.rect.y = random.randrange(80, HEIGHT)
                else: 
                    self.rect.y = (HEIGHT)
        Buildings.existing_x_coords.append(self.rect.x)
        Buildings.existing_y_coords.append(self.rect.y)
        print("Building x coords: %s" % Buildings.existing_x_coords)





class Player(pygame.sprite.Sprite):
    # Car's different assets
    car_no = pygame.image.load("pixel.png")
    car_front = pygame.image.load('car_front.png')
    car_back = pygame.image.load('car_back.png')
    car_left = pygame.image.load('car_left.png')
    car_right = pygame.image.load('car_right.png')
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Setting intial condition for car, before we start moving
        self.current_view = Player.car_right.convert()
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)
        # Setting boundaries
        self.rect = self.image.get_rect()
        # Start off on the center of the screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_x = 0
        self.speed_y = 0
    def update(self): # any code here will happen every time the game loop updates
        # Grabbing keyboard input and modifying direction/orientation
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if ((self.rect.x in Buildings.shitty_list_of_x_ranges) and (self.rect.y in Buildings.shitty_list_of_y_ranges)):
                self.speed_x = 0
                self.speed_y = 0
                self.current_view =  Player.car_left
                print("OH FUCK, we have a match! player.rect.x coords = %d" % (self.rect.x))                         
            else:
                self.speed_x = -5
                self.speed_y = 0
                self.current_view =  Player.car_left
                print("We don't have a match! player.rect.x coords = %d" % (self.rect.x))
        if ((keystate[pygame.K_RIGHT]) and (self.rect.x not in (Buildings.existing_x_right_coords))):
            self.speed_x = 5
            self.speed_y = 0
            self.current_view =  Player.car_right
        if ((keystate[pygame.K_RIGHT]) and (self.rect.x in (Buildings.existing_x_right_coords))):
            self.speed_x = 0
            self.speed_y = 0
            self.current_view =  Player.car_right
        if keystate[pygame.K_DOWN]:
            self.speed_x = 0
            self.speed_y = 5
            self.current_view =  Player.car_front
        if keystate[pygame.K_UP]:
            self.speed_x = 0
            self.speed_y = -5
            self.current_view =  Player.car_back
        # Making the walls the boundaries
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        # You did the math, now update the speeds
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Change orientation? Update the image
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)

class Old_People(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.current_view = Player_Round_1.mort_front_1.convert()
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)

        # Setting boundaries
        self.rect = self.image.get_rect()
        # Spawning attributes for Ian is random on the page
        self.rect.x = random.randrange(16, WIDTH - 16)
        self.rect.y = random.randrange(16, HEIGHT -16 )
        self.speed_x = random.randrange(1, 2) * random.choice((-1,1))
        self.speed_y = random.randrange(1, 2) * random.choice((-1,1))
    def update(self):
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
        # Run off the screen and you respawn
        if ((self.rect.bottom > HEIGHT) or (self.rect.top < 0)) or ((self.rect.right > WIDTH) or (self.rect.left < 0)):
            # Making the walls the boundaries
            if self.rect.right > WIDTH -8 :
                self.speed_x = self.speed_x * -1
            if self.rect.left < 8:
                self.speed_x = self.speed_x * -1
            if self.rect.top < 8:
                self.speed_y = self.speed_y * -1
            if self.rect.bottom > HEIGHT -8:
                self.speed_y = self.speed_y * -1
            # You did the math, now update the speeds
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        if (self.speed_x < 0) and (True):
        # if (self.speed_x < 0) and (self.speed_x > self.speed_y):
            self.current_view = Player_Round_1.mort_images_left[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_left)
        elif (self.speed_x > 0) and (True):
        # elif (self.speed_x > 0) and (self.speed_x > self.speed_y):
            self.current_view = Player_Round_1.mort_images_right[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_right)
        if (self.speed_y < 0) and (self.speed_y > self.speed_x):
            self.current_view = Player_Round_1.mort_images_back[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_back)
        elif (self.speed_y > 0) and (self.speed_y > self.speed_x):
            self.current_view = Player_Round_1.mort_images_front[Player_Round_1.counter]
            Player_Round_1.counter = (Player_Round_1.counter + 1) % len(Player_Round_1.mort_images_front)
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)

class Pedestrians(pygame.sprite.Sprite):
    lisa_front_1 = pygame.image.load('pedestrian_lisa_front_1.png')
    lisa_front_2 = pygame.image.load('pedestrian_lisa_front_2.png')
    lisa_front_3 = pygame.image.load('pedestrian_lisa_front_3.png')
    lisa_images_front = [lisa_front_1, lisa_front_2, lisa_front_3]
    lisa_back_1 = pygame.image.load('pedestrian_lisa_back_1.png')
    lisa_back_2 = pygame.image.load('pedestrian_lisa_back_2.png')
    lisa_back_3 = pygame.image.load('pedestrian_lisa_back_3.png')
    lisa_images_back = [lisa_back_1, lisa_back_2, lisa_back_3]
    lisa_left_1 = pygame.image.load('pedestrian_lisa_left_1.png')
    lisa_left_2 = pygame.image.load('pedestrian_lisa_left_2.png')
    lisa_left_3 = pygame.image.load('pedestrian_lisa_left_3.png')
    lisa_images_left = [lisa_left_1, lisa_left_2, lisa_left_3]
    lisa_right_1 = pygame.image.load('pedestrian_lisa_right_1.png')
    lisa_right_2 = pygame.image.load('pedestrian_lisa_right_2.png')
    lisa_right_3 = pygame.image.load('pedestrian_lisa_right_3.png')
    lisa_images_right = [lisa_right_1, lisa_right_2, lisa_right_3]
    counter = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        lisa = pygame.image.load('pedestrian_lisa.png').convert()
        # ian = pygame.image.load('pedestrian_ian.png').convert()
        # self.image = random.choice((lisa, lisa))
        self.current_view = Pedestrians.lisa_front_1.convert()
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)
        # Setting boundaries
        self.rect = self.image.get_rect()
        # Spawning attributes for Lisa is random on the page
        self.rect.x = random.randrange(16, WIDTH - 16)
        self.rect.y = random.randrange(16, HEIGHT -16 )
        self.speed_x = random.randrange(1, 3) * random.choice((-1,1))
        self.speed_y = random.randrange(1, 3) * random.choice((-1,1))
    def update(self):
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
        # Run off the screen and you respawn
        if ((self.rect.bottom > HEIGHT) or (self.rect.top < 0)) or ((self.rect.right > WIDTH) or (self.rect.left < 0)):
            # Making the walls the boundaries
            if self.rect.right > WIDTH -8 :
                self.speed_x = self.speed_x * -1
            if self.rect.left < 8:
                self.speed_x = self.speed_x * -1
            if self.rect.top < 8:
                self.speed_y = self.speed_y * -1
            if self.rect.bottom > HEIGHT -8:
                self.speed_y = self.speed_y * -1
            # You did the math, now update the speeds
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        if (self.speed_x < 0) and (True):
        # if (self.speed_x < 0) and (self.speed_x > self.speed_y):
            self.current_view = Pedestrians.lisa_images_left[Pedestrians.counter]
            Pedestrians.counter = (Pedestrians.counter + 1) % len(Pedestrians.lisa_images_left)
        elif (self.speed_x > 0) and (True):
        # elif (self.speed_x > 0) and (self.speed_x > self.speed_y):
            self.current_view = Pedestrians.lisa_images_right[Pedestrians.counter]
            Pedestrians.counter = (Pedestrians.counter + 1) % len(Pedestrians.lisa_images_right)
        if (self.speed_y < 0) and (self.speed_y > self.speed_x):
            self.current_view = Pedestrians.lisa_images_back[Pedestrians.counter]
            Pedestrians.counter = (Pedestrians.counter + 1) % len(Pedestrians.lisa_images_back)
        elif (self.speed_y > 0) and (self.speed_y > self.speed_x):
            self.current_view = Pedestrians.lisa_images_front[Pedestrians.counter]
            Pedestrians.counter = (Pedestrians.counter + 1) % len(Pedestrians.lisa_images_front)
        self.image = self.current_view.convert()
        self.image.set_colorkey(BLACK)