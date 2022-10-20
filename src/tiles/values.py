import pygame

from .tile import Tile

class Const(Tile):

    def __init__(self, value):
        self.value = value

    def render(self, renderer, x, y):

        pygame.draw.rect(renderer.display, (0,120,255), (x, y, self.get_width(), self.get_height()))

        words = renderer.font.render(str(self.value), True, (0, 0, 0))
        renderer.display.blit(words, (x+4, y))



    def get_width(self):
        return 24

    def get_height(self):
        return 32
