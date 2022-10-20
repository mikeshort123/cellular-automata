import pygame

class TileSlot:

    def __init__(self, w, h, c):

        self.w = w
        self.h = h
        self.c = c

        self.tile = None


    def render(self, renderer, x, y):
        if self.tile:
            self.tile.render(renderer, x, y)
        else:
            pygame.draw.rect(renderer.display, self.c, (x, y, self.w, self.h))


    def get_width(self):
        return self.tile.get_width() if self.tile else self.w


    def get_height(self):
        return self.tile.get_height() if self.tile else self.h


    def add(self, tile):
        self.tile = tile
