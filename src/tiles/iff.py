from .tile import Tile
from src.stuff.tileSlot import StatementSlot
from src.stuff.tileSlot import ConditionSlot
from src.utils.renderer import Renderer

class Iff(Tile):

    LOWER_SPACER_H = 10
    EDGE_W = 20


    def __init__(self):
        self.cond_slot = ConditionSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (0, 180, 0))
        self.tt_slot = StatementSlot(76, 10, (0, 180, 0))
        self.ff_slot = StatementSlot(76, 10, (0, 180, 0))

        self.if_text = Renderer.font.render('IF', True, (0, 0, 0))
        self.else_text = Renderer.font.render('ELSE', True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        # SIDE BAR
        surface.fill((0,180,0), rect = (Tile.PADDING, 0, Iff.EDGE_W-Tile.PADDING, self.get_height()))

        # IF cond:
        surface.fill((0,255,0), rect = (0, 0, self.if_bar_width(), self.if_bar_height()))

        mp = self.if_bar_height()//2
        surface.blit(self.if_text, (Tile.PADDING, mp - self.if_text.get_height()//2))
        surface.blit(self.cond_slot.render(), (self.if_text.get_width() + Tile.PADDING_2, mp - self.cond_slot.get_height()//2))

        #TRUE:
        surface.blit(self.tt_slot.render(), (Iff.EDGE_W, self.if_bar_height()))

        # ELSE:
        else_y_off = self.if_bar_height() + self.tt_slot.get_height() + Iff.LOWER_SPACER_H
        surface.fill((0,255,0), rect = (0, else_y_off, Tile.PADDING_2 + self.else_text.get_width(), self.else_text.get_height() + Tile.PADDING_2))
        surface.blit(self.else_text, (Tile.PADDING, Tile.PADDING+else_y_off))

        #FALSE
        surface.blit(self.ff_slot.render(), (Iff.EDGE_W, self.else_text.get_height() + Tile.PADDING_2 + else_y_off))

        return surface

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

    @staticmethod
    def build_from_json(data):
        iff = Iff()
        if data['condition']: iff.cond_slot.add(Tile.whatever(data['condition']))
        if data['tt']: iff.tt_slot.add(Tile.whatever(data['tt']))
        if data['ff']: iff.ff_slot.add(Tile.whatever(data['ff']))
        return iff

    def save_to_json(self):
        return f'{{"type" : "iff", "condition" : {self.cond_slot.get_json()}, "tt" : {self.tt_slot.get_json()}, "ff" : {self.ff_slot.get_json()}}}'

    def generate_update_function(self):

        cond = self.cond_slot.generate_check_function()
        tt = self.tt_slot.generate_update_function()
        ff = self.ff_slot.generate_update_function()

        def update(state, x, y):

            if cond(state, x, y):
                return tt(state, x, y)

            else:
                return ff(state, x, y)

        return update
