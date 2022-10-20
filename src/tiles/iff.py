import pygame

from .tile import Tile
from src.stuff.tileSlot import TileSlot

class Iff(Tile):

    BAR_H = 52
    LOWER_SPACER_H = 10
    EDGE_W = 20

    COND_SLOT_X = 50
    COND_SLOT_Y = 5
    COND_SLOT_W = 21
    COND_SLOT_H = 42

    def __init__(self):
        self.cond_slot = TileSlot(
            Iff.COND_SLOT_W,
            Iff.COND_SLOT_H,
            (0, 180, 0)
        )

        self.tt_slot = TileSlot(76, 10, (0, 180, 0))
        self.ff_slot = TileSlot(76, 10, (0, 180, 0))

    def render(self, renderer, x, y):

        # IF cond:
        pygame.draw.rect(renderer.display, (0,255,0), (x, y, self.if_bar_width(), Iff.BAR_H))
        words = renderer.font.render('IF', True, (0, 0, 0))
        renderer.display.blit(words, (x+5, y+10))

        # COND
        self.cond_slot.render(renderer, x + Iff.COND_SLOT_X, y + Iff.COND_SLOT_Y)

        #TRUE:
        self.tt_slot.render(renderer, x + Iff.EDGE_W, y + Iff.BAR_H)

        # SIDE BAR
        pygame.draw.rect(renderer.display, (0,255,0), (x, y + Iff.BAR_H, Iff.EDGE_W, self.get_height()))

        # ELSE:
        else_y_off = Iff.BAR_H + self.tt_slot.get_height() + Iff.LOWER_SPACER_H
        pygame.draw.rect(renderer.display, (0,255,0), (x, y + else_y_off, self.if_bar_width(), Iff.BAR_H))
        words = renderer.font.render('ELSE', True, (0, 0, 0))
        renderer.display.blit(words, (x+5, y+10+else_y_off))

        #FALSE
        self.ff_slot.render(renderer, x + Iff.EDGE_W, y + Iff.BAR_H + else_y_off)

    def if_bar_width(self):
        return max(96, 65 + self.cond_slot.get_width())

    def get_width(self):
        return max(self.if_bar_width(), Iff.EDGE_W + self.tt_slot.get_width(), Iff.EDGE_W + self.ff_slot.get_width())

    def get_height(self):
        return Iff.BAR_H + self.tt_slot.get_height() + self.ff_slot.get_height() + 2 * Iff.LOWER_SPACER_H
