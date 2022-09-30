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

    state = np.zeros((BOARD_WIDTH, BOARD_HEIGHT, 4))

    running = False

    direction = 0



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

                if event.unicode == '1':
                    direction += 1
                    direction %= 4
                    print(direction)


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // SCL, pos[1] // SCL
            #state[x, y, direction] = 1
            state[x, y] = [1]*4
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // SCL, pos[1] // SCL
            #state[x, y, direction] = 0
            state[x, y] = [0]*4

        if running:
            state = update(state)

        for i, row in enumerate(state):
            for j, value in enumerate(row):
                s = np.sum(value) * 63
                c = (s, s, s)
                pygame.draw.rect(display, c, (i*SCL, j*SCL, SCL, SCL))




        pygame.display.update()
        clock.tick(60)

def update(state):

    def get_value(state, x, y, d):
        if x < 0 or y < 0:
            return 0
        try:
            return state[x,y,d]
        except IndexError:
            return 0

    next_state = np.zeros(state.shape)

    for i, row in enumerate(state):
        for j, value in enumerate(row):

            if get_value(state, i-1, j, 0) == 1:
                next_state[i, j, 0] = 1

            if get_value(state, i, j-1, 1) == 1:
                next_state[i, j, 1] = 1

            if get_value(state, i+1, j, 2) == 1:
                next_state[i, j, 2] = 1

            if get_value(state, i, j+1, 3) == 1:
                next_state[i, j, 3] = 1

    next_state_2 = np.zeros(state.shape)

    for i, row in enumerate(next_state):
        for j, (r, d, l, u) in enumerate(row):
            if r and l and not d and not u:
                next_state_2[i, j, 1] = 1
                next_state_2[i, j, 3] = 1

            elif d and u and not r and not l:
                next_state_2[i, j, 0] = 1
                next_state_2[i, j, 2] = 1

            else:
                next_state_2[i, j] = [r,d,l,u]

            if i == 0 and next_state_2[i, j, 2]:
                next_state_2[i, j, 0] = 1

            if i == state.shape[0]-1 and next_state_2[i, j, 0]:
                next_state_2[i, j, 2] = 1

            if j == 0 and next_state_2[i, j, 3]:
                next_state_2[i, j, 1] = 1

            if j == state.shape[1]-1 and next_state_2[i, j, 1]:
                next_state_2[i, j, 3] = 1


    return next_state_2


if __name__ == '__main__': main()
