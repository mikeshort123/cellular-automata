

class TileHolder:

    def __init__(self, x, y, tile):
        self.x = x
        self.y = y

        self.tile = tile

    def render(self, renderer):
        renderer.draw_image(self.tile.render(), self.x, self.y)
