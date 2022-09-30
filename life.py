import pygame
import sys
import numpy as np

def main():

    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640
    SCL = 10
    BOARD_WIDTH, BOARD_HEIGHT = SCREEN_WIDTH // SCL, SCREEN_HEIGHT // SCL

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    state = np.zeros((BOARD_WIDTH, BOARD_HEIGHT))

    running = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    state = update(state)

                if event.key == 13:
                    running = not running


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // SCL, pos[1] // SCL
            state[x, y] = 1
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // SCL, pos[1] // SCL
            state[x, y] = 0

        if running:
            state = update(state)

        for i, row in enumerate(state):
            for j, value in enumerate(row):
                c = (255, 255, 255) if value == 1 else (0, 0, 0)
                pygame.draw.rect(display, c, (i*SCL, j*SCL, SCL, SCL))




        pygame.display.update()
        clock.tick(60)

def update(state):

    def get_value(state, x, y):
        try:
            return state[x,y]
        except IndexError:
            return 0

    next_state = np.zeros(state.shape)

    for i, row in enumerate(state):
        for j, value in enumerate(row):

            total = 0

            offsets = [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1)
            ]

            for dx, dy in offsets:
                total += get_value(state, i+dx, j+dy)


            if value == 0:
                next_state[i, j] = 1 if total == 3 else 0

            else:
                next_state[i, j] = 1 if 2 <= total < 4 else 0

    return next_state


if __name__ == '__main__': main()
