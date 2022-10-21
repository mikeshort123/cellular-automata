import pygame

from src.stuff.tileHolder import TileHolder
from src.tiles.iff import Iff
from src.tiles.returnTile import Return
from src.tiles.conditions import Equals
from src.tiles.conditions import Clamp
from src.tiles.values import Const
from src.tiles.values import Value
from src.tiles.values import Neighbours

class TileWindow:

    def __init__(self):

        iff_1 = Iff()
        iff_2 = Iff()
        iff_3 = Iff()

        iff_1.tt_slot.add(iff_2)
        iff_1.ff_slot.add(iff_3)

        eq_1 = Equals()
        eq_2 = Equals()
        clamp_1 = Clamp()

        iff_1.cond_slot.add(eq_1)
        iff_2.cond_slot.add(eq_2)
        iff_3.cond_slot.add(clamp_1)

        return_1 = Return()
        return_2 = Return()
        return_3 = Return()
        return_4 = Return()

        iff_2.tt_slot.add(return_1)
        iff_2.ff_slot.add(return_2)
        iff_3.tt_slot.add(return_3)
        iff_3.ff_slot.add(return_4)

        return_1.slot.add(Const(1))
        return_2.slot.add(Const(0))
        return_3.slot.add(Const(1))
        return_4.slot.add(Const(0))

        eq_1.left_slot.add(Value())
        eq_1.right_slot.add(Const(0))

        neighbours_1 = Neighbours()
        neighbours_1.slot.add(Const(1))
        eq_2.left_slot.add(neighbours_1)
        eq_2.right_slot.add(Const(3))

        neighbours_2 = Neighbours()
        neighbours_2.slot.add(Const(1))
        clamp_1.mid_slot.add(neighbours_2)
        clamp_1.left_slot.add(Const(2))
        clamp_1.right_slot.add(Const(4))


        self.tiles = [
            TileHolder(100, 100, iff_1)
        ]


    def tick(self, handler):
        return

    def render(self, renderer):
        for tile in self.tiles:
            tile.render(renderer)
