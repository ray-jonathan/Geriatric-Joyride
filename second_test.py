# # Lifted from: https://stackoverflow.com/a/40338475

import pygame
from car import Car, Passenger


def main():
    pygame.init()
    clock = pygame.time.Clock()
    background = pygame.image.load("Atlanta_1_base.png")
    size =[1584, 1584]

    # Making the window the size of the background image
    screen = pygame.display.set_mode(size)
    # Where the player starts
    player = Car([300, 300])
    # Defining player keypresses as movement
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    # How fast the player can move in the X or Y direction, how fast the image onscreen loads
    fps = player.vy = player.vx = 24


    passenger = Passenger([100, 60])

    passenger_group = pygame.sprite.Group()
    passenger_group.add(passenger)

    player_group = pygame.sprite.Group()
    player_group.add(player)

# Start the game
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False


        key = pygame.key.get_pressed()
        # Left/Right travel
        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]
            if key[player.move[1]]:
                player.current_view = player.car_right
            if key[player.move[0]]:
                player.current_view = player.car_left

        # Up/Down travel
        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]
            if key[player.move[2]]:
                player.current_view = player.car_back
            if key[player.move[3]]:
                player.current_view = player.car_front


        ## first parameter takes a single sprite
        ## second parameter takes sprite groups
        ## third parameter is a do kill commad if true
        ## all group objects colliding with the first parameter object will be
        ## destroyed. The first parameter could be bullets and the second one
        ## targets although the bullet is not destroyed but can be done with
        ## simple trick bellow
        # hit = pygame.sprite.spritecollide(player, passenger_group, True)
        hit = pygame.sprite.spritecollide(player, passenger_group, True)
        if hit:
            ## if collision is detected call a function in your case destroy
            ## bullet
            pygame.quit()
            passenger.image.fill((0, 0, 0))

            

        # Put 
        screen.blit(background, [0,0])
        screen.blit(player.current_view, (player.rect.x, player.rect.y))
        # if not hit:
        #     screen.blit(passenger.image, (passenger.rect.x, passenger.rect.y))
        # player.image_selector(screen, player.current_view)


        # # Kind of already handled by the blit but probably important for collisions
        player_group.draw(screen)

        # # Necessary to bring Lisa to life
        passenger_group.draw(screen)

        pygame.display.update()
        

    pygame.quit()


if __name__ == '__main__':
    main()