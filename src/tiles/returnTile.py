from .tile import Tile
from src.stuff.tileSlot import TileSlot
from src.stuff.tileSlot import ValueSlot
from src.utils.renderer import Renderer

class Return(Tile):

    def __init__(self):
        self.slot = ValueSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (0, 180, 180))

        self.words = Renderer.font.render('RETURN', True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        mp = self.get_height()//2

        surface.fill((0,255,255))

        surface.blit(self.words, (Tile.PADDING, mp - self.words.get_height()//2))

        surface.blit(self.slot.render(), (self.words.get_width()+Tile.PADDING_2, mp - self.slot.get_height()//2))

        return surface

    def get_width(self):
        return Tile.PADDING * 3 + self.words.get_width() + self.slot.get_width()

    def get_height(self):
        return Tile.PADDING_2 + self.slot.get_height()

    @staticmethod
    def build_from_json(data):
        r = Return()
        if data['value']: r.slot.add(Tile.whatever(data['value']))
        return r

    def save_to_json(self):
        return f'{{"type" : "return", "value" : {self.slot.get_json()}}}'

    def generate_update_function(self):

        val = self.slot.generate_get_function()

        def update(state, x, y):

            return val(state, x, y)

        return update
