import pygame

from .tile import Tile
from src.stuff.tileSlot import TileSlot

class Return(Tile):

    TEXT_LENGTH = 145

    def __init__(self):
        self.slot = TileSlot(
            16,
            32,
            (0, 180, 180)
        )

    def render(self, renderer, x, y):

        pygame.draw.rect(renderer.display, (0,255,255), (x, y, self.get_width(), self.get_height()))

        words = renderer.font.render('RETURN', True, (0, 0, 0))
        renderer.display.blit(words, (x + 5, y + 5))

        self.slot.render(renderer, x+Return.TEXT_LENGTH, y+5)

    def get_width(self):
        return 10 + Return.TEXT_LENGTH + self.slot.get_width()

    def get_height(self):
        return 42
