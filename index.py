# Pygame sprite Example
import pygame
import random
import sys
import time
from pygame.locals import *
import characters
from characters import Pedestrians, Old_People, Player, Player_Round_1, Pedestrians_Round_1, Buildings, Intro, Intro_Instruct

pygame.font.init()


WIDTH = 400
HEIGHT = 400
FPS = 30


BLACK = (0, 0, 0)





# initialize pygame and create window
pygame.init()
# pygame.mixer.init()

def main(play_count, num_of_pedestrians_at_start, score_at_start):
    score = score_at_start
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    for building in Buildings.existing_x_coords:
        Buildings.existing_x_coords.pop()
    for building in Buildings.existing_x_right_coords:
        Buildings.existing_x_right_coords.pop()
    for building in Buildings.existing_y_coords:
        Buildings.existing_y_coords.pop()
    for building in Buildings.existing_y_bottom_coords:
        Buildings.existing_y_bottom_coords.pop()



    all_sprites = pygame.sprite.Group()
    pedestrians_round_one_group = pygame.sprite.Group()
    pedestrians_group = pygame.sprite.Group()
    old_people_group = pygame.sprite.Group()
    buildings_group = pygame.sprite.Group()

    if play_count == 0:
        player_round_one = Player_Round_1()
        # player_round_one_group = pygame.sprite.Group() # Why not
        all_sprites.add(player_round_one)

        title_logo = Intro()
        all_sprites.add(title_logo)
        intro_instr = Intro_Instruct()
        all_sprites.add(intro_instr)

        for i in range(1):
            pedestrians_round_one = Pedestrians_Round_1()
            all_sprites.add(pedestrians_round_one)
            pedestrians_round_one_group.add(pedestrians_round_one)




    num_of_pedestrians = num_of_pedestrians_at_start
    if play_count > 0:
        # Summoning the pedestrians
        for i in range(num_of_pedestrians):
            pedestrians = Pedestrians()
            all_sprites.add(pedestrians)
            pedestrians_group.add(pedestrians)

        # # Summoning the old people, starting at level 3
        if num_of_pedestrians > 8:
            for i in range(num_of_pedestrians - 8):
                old_people = Old_People()
                all_sprites.add(old_people)
                old_people_group.add(old_people)

        # # Summoning the buildings, starting at level 3
        if num_of_pedestrians > 8:
            for i in range(num_of_pedestrians - 9):
                buildings = Buildings()
                all_sprites.add(buildings)
                buildings_group.add(buildings)


        # Summoning the player's vehicle
        player = Player()
        # player_group = pygame.sprite.Group() # Why not
        all_sprites.add(player)
        
    print(play_count)

    #############
    # Game loop #
    #############

    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False


        # Update
        all_sprites.update()
##########################
        # # # First hit:
        if play_count == 0:
            hit_first_count = 0
            hit_first = pygame.sprite.spritecollide(player_round_one, pedestrians_round_one_group, True)
            if hit_first:
                hit_first_count += 1
                print(hit_first_count)
                play_count += 1
                main(play_count, num_of_pedestrians_at_start, score)
##########################
        if play_count > 0:
            # Check to see if car hit a pedestrian
            hit = pygame.sprite.spritecollide(player, pedestrians_group, True)
            if hit:
                num_of_pedestrians -= 1
                score += 5

            # Check to see if car hit an old person
            hit_old_people = pygame.sprite.spritecollide(player, old_people_group, True)
            if hit_old_people:
                score -= 10

            if play_count > 3:
                # Making the buildings the boundaries
                hit_building = pygame.sprite.spritecollide(player, buildings_group, False)
                if hit_building:
                    player.speed_x = 0
                    player.speed_y = 0



            # Render text
            word_to_spell = ("Millennials left to mow down: %i" % (num_of_pedestrians,))
            font = pygame.font.Font(None, 20)
            kill_block = font.render(word_to_spell, True, (0,0,255))

            # Render text
            word_to_score = ("Score: %i" % (score,))
            font = pygame.font.Font(None, 20)
            score_block = font.render(word_to_score, True, (0,0,255))

        # Draw / render
        background = pygame.image.load("Atlanta_mini.png")
        screen.blit(background, [0,0])
        if play_count > 0:
            screen.blit(kill_block, (10,10))
            screen.blit(score_block, (10, 35))
        all_sprites.draw(screen)

        if play_count > 0:
            if num_of_pedestrians == 0:
                player.speed_x = 0
                player.speed_y = 0
                # player.rect.y = player.rect.y
                # player.rect.x = player.rect.x

                word_to_spell_1 = ("Would you like to continue? (Y or N)")
                font = pygame.font.Font(None, 20)
                again_block = font.render(word_to_spell_1, True, (6,15,255))
                screen.blit(again_block, (WIDTH/5,(HEIGHT/2)))

                # Pause for input
                # pygame.event.clear()
                event = pygame.event.wait()

                if event.type == pygame.QUIT:
                    pygame.quit()

                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_y]:
                    play_count += 1
                    if play_count >= 2:
                        num_of_pedestrians_at_start += 2
                    # for building in Buildings.existing_x_coords:
                    #     Buildings.existing_x_coords.pop(building)
                    # for building in Buildings.existing_x_right_coords:
                    #     Buildings.existing_x_right_coords.pop(building)
                    # for building in Buildings.existing_y_coords:
                    #     Buildings.existing_y_coords.pop(building)
                    # for building in Buildings.existing_y_bottom_coords:
                    #     Buildings.existing_y_bottom_coords.pop(building)
                    main(play_count, num_of_pedestrians_at_start, score)

                elif keystate[pygame.K_n]:
                    word_to_spell_2 = ("Thanks for playing!")
                    font = pygame.font.Font(None, 20)
                    goodbye_block = font.render(word_to_spell_2, True, (6,15,255))
                    screen.blit(goodbye_block, (WIDTH/5,(HEIGHT/2)))
                    # time.sleep(2)
                    running = False
            # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

# Play the game the first time
main(0, 5, 0)