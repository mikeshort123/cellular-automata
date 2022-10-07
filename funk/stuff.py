import numpy as np

class Grid:

    def __init__(self, w, h):
        self.W, self.H = w, h
        self.state = np.zeros((w, h))
        self.next_state = np.zeros((w, h))

    def __getitem__(self, key):
        x, y = key

        if x < 0 or y < 0:
            return 0
        try:
            return self.state[x, y]
        except IndexError:
            return 0

    def __setitem__(self, key, value):
        self.next_state[key] = value

    def update(self, check):

        for i in range(self.W):
            for j in range(self.H):

                self[i, j] = check(self, i, j)

        self.state = self.next_state
        self.next_state = np.zeros(self.state.shape)




def check(state, x, y):
    total = get_surrounded_total(state, x, y, radius = 1)
    if state[x, y] == 0:
       if total == 3:
           return 1
       else:
           return 0
    else:
       if 2 <= total < 4:
           return 1
       else:
           return 0

def get_surrounded_total(state, x, y, radius = 1):

    total = 0

    offsets = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]

    for dx, dy in offsets:
        total += state[x+dx, y+dy]

    return total
