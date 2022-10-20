import pygame

class Renderer():

    def __init__(self, w, h):

        self.generate_screen(w, h)


    def generate_screen(self, w, h):

        self.display = pygame.display.set_mode((w, h), pygame.RESIZABLE)


    def draw_image(self, img, x, y):

        self.display.blit(img, (x,y))

    def clear_background(self):

        pygame.draw.rect(self.display, (0, 0, 0), (0, 0, self.display.get_width(), self.display.get_height()))
