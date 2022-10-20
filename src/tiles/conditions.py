import pygame

from .tile import Tile
from src.stuff.tileSlot import TileSlot

class Equals(Tile):

    def __init__(self):
        self.left_slot = TileSlot(
            16,
            32,
            (180, 0, 0)
        )

        self.right_slot = TileSlot(
            16,
            32,
            (180, 0, 0)
        )

    def render(self, renderer, x, y):

        pygame.draw.rect(renderer.display, (255,0,0), (x, y, self.get_width(), self.get_height()))

        self.left_slot.render(renderer, x+5, y+5)
        ls_offset = x+self.left_slot.get_width()

        words = renderer.font.render('=', True, (0, 0, 0))
        renderer.display.blit(words, (ls_offset + 5, y + 5))

        self.right_slot.render(renderer, ls_offset + 24, y + 5)



    def get_width(self):
        return 29 + self.left_slot.get_width() + self.right_slot.get_width()

    def get_height(self):
        return 42
