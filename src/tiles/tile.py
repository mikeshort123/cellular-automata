from abc import ABC, abstractmethod

class Tile(ABC):

    BLANK_SLOT_W = 16
    BLANK_SLOT_H = 32

    PADDING = 5
    PADDING_2 = PADDING * 2


    @abstractmethod
    def render(self, renderer, x, y):
        ...

    @abstractmethod
    def get_width(self):
        ...

    @abstractmethod
    def get_height(self):
        ...

THANG = 0
CONDITION = 1
VALUE = 2
