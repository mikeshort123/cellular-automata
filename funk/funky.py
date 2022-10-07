import pygame
import sys
import numpy as np
import stuff

def main():

    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
    SCL = 10
    BOARD_WIDTH, BOARD_HEIGHT = SCREEN_WIDTH // SCL, SCREEN_HEIGHT // SCL

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    state = stuff.Grid(BOARD_WIDTH, BOARD_HEIGHT)

    running = False

    update_function = stuff.make_update_function()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    state.update(update_function)

                if event.key == 13:
                    running = not running


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // SCL, pos[1] // SCL
            state.state[x, y] = 1
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // SCL, pos[1] // SCL
            state.state[x, y] = 0

        if running:
            state.update(update_function)


        for i in range(state.W):
            for j in range(state.H):
                c = (255, 255, 255) if state[i, j] == 1 else (0, 0, 0)
                pygame.draw.rect(display, c, (i*SCL, j*SCL, SCL, SCL))




        pygame.display.update()
        clock.tick(60)







if __name__ == '__main__': main()
