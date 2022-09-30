import pygame
import sys

def main():

    pygame.init()

    WIDTH, HEIGHT = 640, 640
    ZOOM = 400

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    board_width = 640
    s_scl = WIDTH // board_width
    max_depth = HEIGHT // s_scl

    #30, 90, 110
    rule = 90

    row = 0
    state = 1 << (board_width//2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(board_width):

            v = (state >> i) & 1
            c = (0,0,0) if v == 0 else (255, 255, 255)
            pygame.draw.rect(display, c, (i*s_scl, row*s_scl, s_scl, s_scl))

        if row <= max_depth:

            state = calc_next_state(rule, state, board_width)
            row += 1


        pygame.display.update()
        clock.tick(60)


def calc_next_state(rule, current_state, board_width):

    shifted_state = current_state << 1

    next_state = 0

    for i in range(board_width):
        pattern = (shifted_state >> i) & 7
        case = ((rule >> pattern) & 1) << i
        next_state += case

    return next_state



if __name__ == '__main__': main()
