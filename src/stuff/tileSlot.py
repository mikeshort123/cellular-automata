from src.utils.renderer import Renderer

class TileSlot:

    def __init__(self, w, h, c):

        self.w = w
        self.h = h
        self.c = c

        self.tile = None


    def render(self):
        if self.tile:
            return self.tile.render()
        else:
            surface = Renderer.make_surface(self.w, self.h)
            surface.fill(self.c)
            return surface


    def get_width(self):
        return self.tile.get_width() if self.tile else self.w


    def get_height(self):
        return self.tile.get_height() if self.tile else self.h


    def add(self, tile):
        self.tile = tile

    def get_json(self):
        return self.tile.save_to_json() if self.tile else '{}'


class StatementSlot(TileSlot):

    def generate_update_function(self):
        return self.tile.generate_update_function()

class ConditionSlot(TileSlot):

    def generate_check_function(self):
        return self.tile.generate_check_function()

class ValueSlot(TileSlot):

    def generate_get_function(self):
        return self.tile.generate_get_function()
