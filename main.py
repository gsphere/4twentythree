# PURPOSE OF THIS SCRIPT

# USE PYGAME TO CREATE THE STANDARD GAME OF LIFE / CELLULAR AUTOMATA
# STATIC SIZE OF WINDOW
# BLACK AND WHITE
# *MOUSEWHEEL SCROLL WOULD BE NEAT
# CLICK TO DRAW
# SPACE TO PAUSE
# - / = SHOULD CHANGE SPEED OF SIMULATION
#
#
# USE NUMPY ARRAY TO REPRESENT THE SCREEN
# USE TEXT TO SHOW THE POSITION OF THE MOUSE
#

import pygame as pg
import numpy as np
from pygame import surfarray

WIDTH = 1200
HEIGHT = 900
WHITE = (255,255,255)
current_mouse_pos = (0,0)

debug_flag = False




screen = pg.display.set_mode((WIDTH, HEIGHT))
surface = np.zeros((*screen.get_size(), 3), np.int32)
clock = pg.time.Clock()

directions = ((1,0), (1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1))

def step():
    surface[ current_mouse_pos[0], current_mouse_pos[1] ] = WHITE

    # manipulate the surface
    # in the following way
    #
    # new array containing neighbor count
    # calculated by each point added to all 8 directions in the new array

    occupied = surface[  surface == WHITE  ]
    if debug_flag:
        pass

    # mask = (surface != WHITE) & (neighbors == 2)

    surfarray.blit_array(screen, surface)
    pass


def main():
    global current_mouse_pos, debug_flag

    running = True
    paused = False


    fps = 60
    surfarray.blit_array(screen, surface)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    paused = not paused
                if event.key == pg.K_d:
                    debug_flag = not debug_flag

        current_mouse_pos = pg.mouse.get_pos()
        if not paused:
            step()

            # draw everything not on the array
            mouse_font = pg.font.Font(None, size=40)
            mouse_font_img = mouse_font.render(current_mouse_pos.__str__() +
                                               paused.__str__(), 0,
                                               "white")
            mouse_font_rect = mouse_font_img.get_rect()
            mouse_font_rect.topleft = (10,10)


            screen.blit(mouse_font_img, mouse_font_rect)

        pg.display.flip()

        dt = clock.tick((not paused) * fps)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()