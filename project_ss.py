import pygame
import os
from random import randint

pygame.init()

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

ss_display = pygame.display.set_mode([800, 800])

pygame.display.set_caption('Simple Shooter')

# Add Icon
pygame.display.set_icon(
pygame.image.load(os.path.join('assets', '32x32_project_ss.png'))
)

def ss_bad_ai(px, py, bx, by, mode='a', difficulty='normal'):
    ss_bad_ai_temp = randint(0,3)
    if ss_bad_ai_temp == 0:
        if by > 30:
            del ss_bad_ai_temp
            return 'n'
        else:
            del ss_bad_ai_temp
            return 's'
    elif ss_bad_ai_temp == 1:
        if by < 600:
            del ss_bad_ai_temp
            return 'e'
        else:
            del ss_bad_ai_temp
            return 'w'
    elif ss_bad_ai_temp == 2:
        if by < 500:
            del ss_bad_ai_temp
            return 's'
        else:
            del ss_bad_ai_temp
            return 'n'
    elif ss_bad_ai_temp == 3:
        if by > 30:
            del ss_bad_ai_temp
            return 'w'
        else:
            del ss_bad_ai_temp
            return 'e'

def ss_print(string='Test', x=0, y=0, colour=black):
    ss_display.blit(pygame.font.SysFont("arial", 25).render(string, True, colour), (x, y))


def ss_rect(x, y, width, height, colour=black):
    if x <= 0:
        x = 1
    if y <= 0:
        y = 1
    if width <= 0:
        width = 1
    if height <= 0:
        height = 1
    pygame.draw.rect(ss_display, colour, (x, y, width, height))


def ss_clear():
    ss_display.fill(white)


def ss_init():
    ss_clear()
    ss_print('This is a simple shooter')
    # TODO: complete this description
    ss_initial = True
    while ss_initial:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.display.quit()
                    pygame.quit()
                    #quit()
                elif event.key == pygame.K_SPACE:
                    ss_initial = False
        pygame.display.update()


def ss_bullet(x, y, colour = blue):
    ss_rect(x, y, 10, 2, colour)


def ss_player(x, y):
    ss_rect(x, y, 20, 40)
    ss_rect(x+20, y+10, 5, 5)


def ss():
    while True:
        ss_init()
        ss_run = True
        ss_pos = [0, 0]
        ss_bad_pos = [500, 500]
        ss_bullets = []
        ss_bad_bullets = []
        ss_cooldown = 0
        ss_bad_cooldown = 0
        ss_score = 0
        ss_bad_move_cooldown = 0
        while ss_run:
            ss_clear()
            clock.tick(0)
            ss_rect(0, 600, 800, 200, black)  # Ground
            ss_fire = False
            for event in pygame.event.get():  # Input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.display.quit()
                        pygame.quit()
                        #quit()
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    #quit()
            ss_keys = pygame.key.get_pressed()
            if ss_keys[pygame.K_w]:  # Up
                if ss_pos[1] > 0:
                    ss_pos[1] -= 4
            if ss_keys[pygame.K_d]:  # Right
                if ss_pos[0] < 780:
                    ss_pos[0] += 3
            if ss_keys[pygame.K_a]:  # Left
                if ss_pos[0] > 0:
                    ss_pos[0] -= 3
            if ss_keys[pygame.K_s]:  # Down
                if ss_pos[1] < 560:
                    ss_pos[1] += 2
            if ss_keys[pygame.K_SPACE]:
                ss_fire = True
            if ss_keys[pygame.K_p]:
                ss_pause = True
                while ss_pause:
                    ss_clear()
                    ss_print('Paused')
                    ss_print('To unpause press x', 1, 30)
                    ss_print(str(randint(10**50, 10**51)), 1, 100)
                    pygame.display.update()
                    ss_keys = pygame.key.get_pressed()
                    if ss_keys[pygame.K_x]:
                        ss_pause = False
                    for event in pygame.event.get():  # Input
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.display.quit()
                                pygame.quit()
                        if event.type == pygame.QUIT:
                            pygame.display.quit()
                            pygame.quit()
                            #quit()
            # Gravity
            if ss_pos[1] < 560:
                ss_pos[1] += 1
            # Fire
            if ss_cooldown%5 == 0:
                if ss_fire == True:
                    if ss_cooldown < 90:
                        ss_print('Pew', ss_pos[0]+20, ss_pos[1])
                        ss_bullets.append([ss_pos[0]+20, ss_pos[1]+10])
                        ss_cooldown += 20
            if ss_cooldown > 0:
                ss_cooldown -= 1

                #TODO

            # Bullets Move
            ss_bullets_temp = []
            ss_temp = True
            for i in ss_bullets:
                ss_bullet(i[0],i[1])
                if i[0] in range(500, 520):
                    if i[1] in range(500, 540):
                        ss_score +=1
                        ss_temp = False
                if i[0] < 700 and ss_temp:
                        ss_bullets_temp.append([i[0]+10,i[1]])
                ss_temp = True
                # Bullets Despawn
            del ss_temp

            ss_bullets = ss_bullets_temp
            del ss_bullets_temp

            # Bullet cooldowm
            ss_rect(700, 790, 100, 10, white)
            ss_rect(700, 790, ss_cooldown, 10, red)

            # Enemy
            ss_rect(ss_bad_pos[0], ss_bad_pos[1], 20, 40)

            # Bad
            ss_bullets_temp = []
            ss_temp = True
            for i in ss_bad_bullets:
                ss_bullet(i[0], i[1], red)
                if i[0] in range(ss_pos[0], ss_pos[0]+20):
                    if i[1] in range(ss_pos[1], ss_pos[1]+40):
                        ss_score -= 10
                        ss_temp = False
                if i[0] > 0 and ss_temp:
                    ss_bullets_temp.append([i[0]-10,i[1]])
                ss_temp = True
            ss_bad_bullets = ss_bullets_temp
            del ss_temp
            del ss_bullets_temp

            # Enemy Moves
            if ss_bad_move_cooldown == 0:
                ss_temp_direction = ss_bad_ai(0, 0, ss_bad_pos[0], ss_bad_pos[1])
                ss_bad_move_cooldown +=30
            if ss_score >= 100:
                if ss_temp_direction == 'n':
                    ss_bad_pos = [ss_bad_pos[0], ss_bad_pos[1]-1]
                elif ss_temp_direction == 'e':
                    ss_bad_pos = [ss_bad_pos[0]+1, ss_bad_pos[1]]
                elif ss_temp_direction == 's':
                    ss_bad_pos = [ss_bad_pos[0], ss_bad_pos[1]+1]
                elif ss_temp_direction == 'w':
                    ss_bad_pos = [ss_bad_pos[0]-1, ss_bad_pos[1]]

            if ss_bad_cooldown == 0:
                ss_bad_bullets.append([randint(600,800),randint(0,600)])
                ss_bad_cooldown += 10

            if ss_bad_cooldown > 0:
                ss_bad_cooldown -= 1

            if ss_bad_move_cooldown > 0:
                ss_bad_move_cooldown -= 1

            ss_print(str(ss_score))
            ss_player(ss_pos[0], ss_pos[1])
            pygame.display.update()


try:
    ss()
except KeyboardInterrupt:
    pygame.display.quit()
    pygame.quit()
    #quit()
