

class TileHolder:

    def __init__(self, x, y, tile):
        self.x = x
        self.y = y

        self.tile = tile

    def render(self, renderer):
        self.tile.render(renderer, self.x, self.y)
