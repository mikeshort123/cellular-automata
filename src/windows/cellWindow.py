import pygame

from src.cells.grid import Grid

class CellWindow:

    def __init__(self):

        grid = Grid(100, 100)

    def render(self, renderer, colours, scl):

        def draw_cell(v, x, y):

            pygame.draw.rect(renderer.display, colours[v], (x*scl, y*scl, scl, scl))

        grid.apply_to_cells(draw_cell)

    def update(self, f):

        grid.update(f)
