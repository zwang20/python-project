import pygame
from sge import *

pygame.init()

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

game_display = pygame.display.set_mode([800, 800])

# TODO: set caption
# TODO: set icon

pygame.mouse.set_visible(False) # Disable Mouse
bullets = [] # x, y, vector x, vextor y
cooldown = 0 # Init cooldown

# Main loop
while True:

    # init
    clock.tick(30) # Frames per second
    sge_clear(game_display) # Clear
    sge_print(game_display, str(int(10*clock.get_fps())/10))
    fire = False

    # Input
    for event in pygame.event.get():  # Input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # Quit
                    pygame.display.quit()
                    pygame.quit()
                    # quit()
            if event.type == pygame.QUIT: # Quit
                pygame.display.quit()
                pygame.quit()
                # quit()
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
            fire = True

    # mouse
    sge_rect(game_display, mouse_pos[0]-8, mouse_pos[1]-1, 16, 2, red)
    sge_rect(game_display, mouse_pos[0]-1, mouse_pos[1]-8, 2, 16, red)

    # temp ratios
    temp = (((((mouse_pos[0]-400)**2)+((mouse_pos[1]-400)**2))**0.5)/10)

    # temp ZeroDivision error
    if temp == 0:
        temp = 0.1

    # Fire
    if fire and cooldown < 100 and cooldown%4 == 0:
        bullets.append(
            [400, 400, (mouse_pos[0]-400)/temp, (mouse_pos[1]-400)/temp])
        cooldown +=10
    del temp

    # Cooldown
    if cooldown > 0:
            cooldown -= 1

    # Cooldown bar
    sge_rect(game_display, 700, 790, 100, 10, white)
    sge_rect(game_display, 700, 790, cooldown, 10, red)

    bullets_temp = []
    for bullet in bullets:
        bullets_temp.append(
            [bullet[0]+bullet[2], bullet[1]+bullet[3], bullet[2], bullet[3]])
        sge_line(game_display, black,
            (bullet[0], bullet[1]), (bullet[0]-bullet[2], bullet[1]-bullet[3]),
                 2)
    bullets = bullets_temp
    del bullets_temp
    while len(bullets) > 100:
        del bullets[0]


    pygame.display.update() # update
    # This should be the last thing in the loop
