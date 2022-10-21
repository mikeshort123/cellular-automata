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
