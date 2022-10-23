import pygame

from src.cells.grid import Grid

class CellWindow:

    def __init__(self, x, y):

        self.grid = Grid(x, y)
        self.running = False
        self.update_function = None

    def render(self, renderer, colours, scl):

        def draw_cell(v, x, y):

            pygame.draw.rect(renderer.display, colours[int(v)], (x*scl, y*scl, scl, scl))

        self.grid.apply_to_cells(draw_cell)

    def tick(self):

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // 10, pos[1] // 10
            self.grid.set_current(x, y, 1)
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // 10, pos[1] // 10
            self.grid.set_current(x, y, 0)

        if self.running:
            self.grid.update(self.update_function)
