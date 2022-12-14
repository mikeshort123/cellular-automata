import pygame

class Renderer():

    def __init__(self, w, h):

        self.generate_screen(w, h)
        Renderer.load_font()


    def generate_screen(self, w, h):

        self.display = pygame.display.set_mode((w, h), pygame.RESIZABLE)


    def draw_image(self, img, x, y):

        self.display.blit(img, (x,y))

    def clear_background(self):

        pygame.draw.rect(self.display, (0, 0, 0), (0, 0, self.display.get_width(), self.display.get_height()))

    @staticmethod
    def load_font():
        Renderer.font = pygame.font.Font('freesansbold.ttf', 32)

    @staticmethod
    def make_surface(w, h):
        return pygame.Surface((w, h), flags=pygame.SRCALPHA)
