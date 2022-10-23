import json

from src.stuff.tileHolder import TileHolder
from src.tiles.tile import Tile

from src.tiles.iff import Iff
from src.tiles.returnTile import Return
from src.tiles.conditions import Equals
from src.tiles.conditions import Clamp
from src.tiles.values import Const
from src.tiles.values import Value
from src.tiles.values import Neighbours


class TileWindow:

    def __init__(self, handler):

        Tile.register_tile(Iff, 'iff')
        Tile.register_tile(Return, 'return')
        Tile.register_tile(Equals, 'equals')
        Tile.register_tile(Clamp, 'clamp')
        Tile.register_tile(Const, 'constant')
        Tile.register_tile(Value, 'value')
        Tile.register_tile(Neighbours, 'neighbours')


        with open('res/wireworld.json') as f:
            data = json.load(f)

        iff_1 = Tile.whatever(data)

        self.update_function = iff_1.generate_update_function()


        self.tiles = [
            TileHolder(100, 100, iff_1)
        ]

        #with open('res/life.json', 'w') as f:
        #    f.write(iff_1.save_to_json())


    def tick(self):
        return

    def render(self, renderer):
        for tile in self.tiles:
            tile.render(renderer)
