import numpy as np

class Grid:

    def __init__(self, w, h, default = 0):
        self.W, self.H = w, h
        self.default = default

        self.current_state = np.zeros((w, h))
        self.next_state = np.zeros((w, h))

    def get(self, x, y):

        if 0 <= x < self.W and 0 <= y < self.H:
            return self.current_state[x, y]

        return 0


    def set_next(self, x, y, value):
        self.next_state[x, y] = value

    def set_current(self, x, y, value):
        self.current_state[x, y] = value

    def update(self, check):

        for i in range(self.W):
            for j in range(self.H):

                self.set_next(i, j, check(self, i, j))


        #self.current_state = self.next_state
        #self.next_state = np.zeros_like(self.current_state)
            # skip instantiating a new array every time
        self.current_state, self.next_state = self.next_state, self.current_state
        self.next_state.fill(0)


    def apply_to_cells(self, f):

        for i in range(self.W):
            for j in range(self.H):

                f(self.get(i, j), i, j)
