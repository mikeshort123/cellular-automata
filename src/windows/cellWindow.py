import pygame

from src.cells.grid import Grid

class CellWindow:

    def __init__(self, handler, x, y):

        self.grid = Grid(x, y)
        self.running = False
        self.update_function = None

        handler.register_event('KEYDOWN_mb1', self.increment_cell)
        handler.register_event('KEYDOWN_mb3', self.reset_cell)

    def render(self, renderer, colours, scl):

        def draw_cell(v, x, y):

            pygame.draw.rect(renderer.display, colours[int(v)], (x*scl, y*scl, scl, scl))

        self.grid.apply_to_cells(draw_cell)

    def tick(self):

        if self.running:
            self.grid.update(self.update_function)


    def increment_cell(self):

        x, y = self.get_screen_mouse_pos()
        v = self.grid.get(x, y)
        v += 1
        v %= 4
        self.grid.set_current(x, y, v)

    def reset_cell(self):

        x, y = self.get_screen_mouse_pos()
        self.grid.set_current(x, y, 0)


    def get_screen_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return x // 10, y // 10
