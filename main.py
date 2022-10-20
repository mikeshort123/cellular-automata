import pygame, sys

from src.utils.handler import Handler
from src.utils.renderer import Renderer
from src.windows.tile_window import TileWindow

def main():
    game = Main(640,480)
    game.run()


class Main():

    def __init__(self,x,y):

        pygame.init()

        self.MAXX = x
        self.MAXY = y

    def run(self):

        clock = pygame.time.Clock()

        handler = Handler()
        renderer = Renderer(self.MAXX, self.MAXY)

        w = TileWindow()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.VIDEORESIZE:
                    renderer.generate_screen(event.w, event.h)


                handler.handle_event(event)

            renderer.clear_background()

            w.tick(handler)
            w.render(renderer)


            handler.reset()
            pygame.display.update()
            clock.tick(60)




if __name__ == "__main__": main()
