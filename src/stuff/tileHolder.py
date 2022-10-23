import pygame

class TileHolder:

    def __init__(self, x, y, tile):
        self.x = x
        self.y = y

        self.tile = tile

    def render(self, renderer):
        img = self.tile.render()
        img = pygame.transform.scale(img, (img.get_width()//3, img.get_height()//3))
        renderer.draw_image(img, self.x, self.y)
