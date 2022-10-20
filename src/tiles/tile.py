from abc import ABC, abstractmethod

class Tile(ABC):


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
