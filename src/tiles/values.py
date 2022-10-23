from .tile import Tile
from src.stuff.tileSlot import ValueSlot
from src.utils.renderer import Renderer

class Const(Tile):

    def __init__(self, value):
        self.value = value

        self.words = Renderer.font.render(str(self.value), True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        surface.fill((0,120,255))
        surface.blit(self.words, (Tile.PADDING, 0))

        return surface

    def get_width(self):
        return Tile.PADDING_2 + self.words.get_width()

    def get_height(self):
        return Tile.BLANK_SLOT_H

    @staticmethod
    def build_from_json(data):
        v = data['value']
        return Const(v)

    def save_to_json(self):
        return f'{{"type" : "constant", "value" : {self.value}}}'

    def generate_get_function(self):

        def get(state, x, y):

            return self.value

        return get


class Value(Tile):

    def __init__(self):
        self.words = Renderer.font.render('VALUE', True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        surface.fill((170,0,210))
        surface.blit(self.words, (Tile.PADDING, 0))

        return surface

    def get_width(self):
        return Tile.PADDING_2 + self.words.get_width()

    def get_height(self):
        return Tile.BLANK_SLOT_H

    @staticmethod
    def build_from_json(data):
        return Value()

    def save_to_json(self):
        return f'{{"type" : "value"}}'


    def generate_get_function(self):

        def get(state, x, y):

            return state.get(x, y)

        return get


class Neighbours(Tile):

    def __init__(self):
        self.slot = ValueSlot(Tile.BLANK_SLOT_W, Tile.BLANK_SLOT_H, (100, 0, 130))

        self.words = Renderer.font.render('NEIGHBOURING', True, (0, 0, 0))

    def render(self):

        surface = Renderer.make_surface(self.get_width(), self.get_height())

        mp = self.get_height()//2

        surface.fill((170,0,210))

        surface.blit(self.words, (Tile.PADDING, mp - self.words.get_height()//2))

        surface.blit(self.slot.render(), (self.words.get_width() + Tile.PADDING_2, mp - self.slot.get_height()//2))

        return surface


    def get_width(self):
        return Tile.PADDING*3 + self.words.get_width() + self.slot.get_width()

    def get_height(self):
        return Tile.PADDING_2 + self.slot.get_height()

    @staticmethod
    def build_from_json(data):
        neighbours = Neighbours()
        if data['value']: neighbours.slot.add(Tile.whatever(data['value']))
        return neighbours

    def save_to_json(self):
        return f'{{"type" : "neighbours", "value" : {self.slot.get_json()}}}'

    def generate_get_function(self):

        target = self.slot.generate_get_function()

        def get(state, x, y):

            offsets = (
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1)
            )

            return sum([1 for dx, dy in offsets if state.get(x+dx, y+dy) == target(state, x, y)])

        return get
