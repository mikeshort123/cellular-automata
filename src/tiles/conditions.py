from .tile import Tile
from src.stuff.tileSlot import TileSlot
from src.utils.renderer import Renderer

class Equals(Tile):

    def __init__(self):
        self.left_slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (180, 0, 0))
        self.right_slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (180, 0, 0))

        self.words = Renderer.font.render('=', True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        mp = self.get_height()//2
        offset = Tile.PADDING

        surface.fill((255,0,0))

        surface.blit(self.left_slot.render(), (offset, mp - self.left_slot.get_height()//2))
        offset += self.left_slot.get_width() + Tile.PADDING

        surface.blit(self.words, (offset, mp - self.words.get_height()//2))
        offset += self.words.get_width() + Tile.PADDING

        surface.blit(self.right_slot.render(), (offset, mp - self.right_slot.get_height()//2))

        return surface

    def get_width(self):
        return Tile.PADDING * 4 + self.left_slot.get_width() + self.words.get_width() + self.right_slot.get_width()

    def get_height(self):
        return Tile.PADDING_2 + max(self.left_slot.get_height(), self.right_slot.get_height())


class Clamp(Tile):

    def __init__(self):
        self.left_slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (180, 0, 0))
        self.mid_slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (180, 0, 0))
        self.right_slot = TileSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (180, 0, 0))

        self.l_words = Renderer.font.render('<=', True, (0, 0, 0))
        self.r_words = Renderer.font.render('<', True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        mp = self.get_height()//2
        offset = Tile.PADDING

        surface.fill((255,0,0))

        surface.blit(self.left_slot.render(), (offset, mp - self.left_slot.get_height()//2))
        offset += self.left_slot.get_width() + Tile.PADDING

        surface.blit(self.l_words, (offset, mp - self.l_words.get_height()//2))
        offset += self.l_words.get_width() + Tile.PADDING

        surface.blit(self.mid_slot.render(), (offset, mp - self.mid_slot.get_height()//2))
        offset += self.mid_slot.get_width() + Tile.PADDING

        surface.blit(self.r_words, (offset, mp - self.r_words.get_height()//2))
        offset += self.r_words.get_width() + Tile.PADDING

        surface.blit(self.right_slot.render(), (offset, mp - self.right_slot.get_height()//2))

        return surface

    def get_width(self):
        return Tile.PADDING * 6 + self.left_slot.get_width() + self.l_words.get_width() + self.mid_slot.get_width() + self.r_words.get_width() + self.right_slot.get_width()

    def get_height(self):
        return Tile.PADDING_2 + max(self.left_slot.get_height(), self.mid_slot.get_height(), self.right_slot.get_height())
