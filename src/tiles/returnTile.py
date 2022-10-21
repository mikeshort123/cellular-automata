import pygame

from .tile import Tile
from src.stuff.tileSlot import TileSlot
from src.utils.renderer import Renderer

class Return(Tile):

    def __init__(self):
        self.slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (0, 180, 180))

        self.words = Renderer.font.render('RETURN', True, (0, 0, 0))

    def render(self, renderer, x, y):

        mp = self.get_height()//2

        pygame.draw.rect(renderer.display, (0,255,255), (x, y, self.get_width(), self.get_height()))

        renderer.display.blit(self.words, (x + Tile.PADDING, y + mp - self.words.get_height()//2))

        self.slot.render(renderer, x+self.words.get_width()+Tile.PADDING_2, y + mp - self.slot.get_height()//2)

    def get_width(self):
        return Tile.PADDING * 3 + self.words.get_width() + self.slot.get_width()

    def get_height(self):
        return Tile.PADDING_2 + self.slot.get_height()
