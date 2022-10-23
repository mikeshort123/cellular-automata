import pygame, sys

from src.utils.handler import Handler
from src.utils.renderer import Renderer
from src.windows.tileWindow import TileWindow
from src.windows.cellWindow import CellWindow

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

        tw = TileWindow(handler)
        cw = CellWindow(handler, 64, 48)

        active = False

        colours = [
            (0, 0, 0),
            (255, 255, 0),
            (0, 0, 255),
            (255, 0, 0)
        ]

        cw.update_function = tw.update_function


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.VIDEORESIZE:
                    renderer.generate_screen(event.w, event.h)

                if event.type == pygame.KEYDOWN:

                    if event.key == 32:
                        active = not active

                    if event.key == 13:
                        cw.running = not cw.running


                handler.handle_event(event)

            renderer.clear_background()

            if active:
                cw.tick()
                cw.render(renderer, colours, 10)

            else:
                tw.tick()
                tw.render(renderer)


            pygame.display.update()
            clock.tick(60)




if __name__ == "__main__": main()
