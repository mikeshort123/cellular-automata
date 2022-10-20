import pygame

from src.stuff.tileHolder import TileHolder
from src.tiles.iff import Iff
from src.tiles.returnTile import Return
from src.tiles.conditions import Equals
from src.tiles.values import Const

class TileWindow:

    def __init__(self):

        iff_1 = Iff()
        iff_2 = Iff()
        return_1 = Return()
        return_2 = Return()
        cond_1 = Equals()
        const_1 = Const(1)
        const_2 = Const(2)

        iff_1.cond_slot.add(cond_1)
        iff_1.tt_slot.add(return_1)
        iff_1.ff_slot.add(return_2)
        return_1.slot.add(const_1)
        cond_1.right_slot.add(const_2)

        self.tiles = [
            TileHolder(100, 100, iff_1),
            TileHolder(500, 100, iff_2)
        ]


    def tick(self, handler):
        return

    def render(self, renderer):
        for tile in self.tiles:
            tile.render(renderer)
