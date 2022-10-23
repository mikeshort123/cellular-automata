from abc import ABC, abstractmethod

class Tile(ABC):

    BLANK_SLOT_W = 16
    BLANK_SLOT_H = 32

    PADDING = 5
    PADDING_2 = PADDING * 2

    generator_table = {}

    @staticmethod
    def whatever(data):

        tile = Tile.generator_table.get(data['type'])
        if tile is None: print(data)
        return tile.build_from_json(data)

    @staticmethod
    def register_tile(tile, name):
        Tile.generator_table[name] = tile

    @abstractmethod
    def render(self):
        ...

    @abstractmethod
    def get_width(self):
        ...

    @abstractmethod
    def get_height(self):
        ...

    @staticmethod
    @abstractmethod
    def build_from_json(data):
        ...

    @abstractmethod
    def save_to_json():
        ...
