import pygame

from .tile import Tile
from src.stuff.tileSlot import TileSlot
from src.utils.renderer import Renderer

class Iff(Tile):

    LOWER_SPACER_H = 10
    EDGE_W = 20


    def __init__(self):
        self.cond_slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (0, 180, 0))
        self.tt_slot = TileSlot(76, 10, (0, 180, 0))
        self.ff_slot = TileSlot(76, 10, (0, 180, 0))

        self.if_text = Renderer.font.render('IF', True, (0, 0, 0))
        self.else_text = Renderer.font.render('ELSE', True, (0, 0, 0))

    def render(self, renderer, x, y):

        # SIDE BAR
        pygame.draw.rect(renderer.display, (0,180,0), (x+Tile.PADDING, y, Iff.EDGE_W-Tile.PADDING, self.get_height()))

        # IF cond:
        pygame.draw.rect(renderer.display, (0,255,0), (x, y, self.if_bar_width(), self.if_bar_height()))

        mp = self.if_bar_height()//2
        renderer.display.blit(self.if_text, (x + Tile.PADDING, y + mp - self.if_text.get_height()//2))
        self.cond_slot.render(renderer, x + self.if_text.get_width() + Tile.PADDING_2, y + mp - self.cond_slot.get_height()//2)

        #TRUE:
        self.tt_slot.render(renderer, x + Iff.EDGE_W, y + self.if_bar_height())

        # ELSE:
        else_y_off = self.if_bar_height() + self.tt_slot.get_height() + Iff.LOWER_SPACER_H
        pygame.draw.rect(renderer.display, (0,255,0), (x, y + else_y_off, Tile.PADDING_2 + self.else_text.get_width(), self.else_text.get_height() + Tile.PADDING_2))
        renderer.display.blit(self.else_text, (x+Tile.PADDING, y+Tile.PADDING+else_y_off))

        #FALSE
        self.ff_slot.render(renderer, x + Iff.EDGE_W, y + self.else_text.get_height() + Tile.PADDING_2 + else_y_off)

    def if_bar_width(self):
        return Tile.PADDING * 3 + self.cond_slot.get_width() + self.if_text.get_width()

    def if_bar_height(self):
        return Tile.PADDING_2 + self.cond_slot.get_height()

    def else_bar_width(self):
        return Tile.PADDING_2 + self.else_text.get_width()

    def else_bar_height(self):
        return Tile.PADDING_2 + self.else_text.get_height()

    def get_width(self):
        return max(self.else_bar_width(), self.if_bar_width(), Iff.EDGE_W + self.tt_slot.get_width(), Iff.EDGE_W + self.ff_slot.get_width())

    def get_height(self):
        return self.if_bar_height() + self.else_bar_height() + self.tt_slot.get_height() + self.ff_slot.get_height() + 2 * Iff.LOWER_SPACER_H
