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
       if 3 <= total < 5:
           return 1
       else:
           return 0

def get_surrounded_total(state, x, y, radius = 1):

    total = 0

    for dx in range(-radius, radius+1):
        for dy in range(-radius, radius+1):

            total += state[x+dx, y+dy]

    return total

class Rule:

    def __init__(self, c):
        self.c = c

    def __call__(self, state, x, y, vars):

        for w in self.c:
            x = w(state, x, y, vars)
            if x is not None:
                return x

class Iff:

    def __init__(self, cond, tt, ff):
        self.cond = cond
        self.tt = tt
        self.ff = ff

    def __call__(self, state, x, y, vars):
        if self.cond(vars):
            self.tt(state, x, y, vars)
        else:
            self.ff(state, x, y, vars)

def partA(state, x, y, vars):
    vars['total'] = get_surrounded_total(state, x, y, radius = 1)

def partB(state, x, y, vars):
    if vars['value'] == 0:
       if vars['total'] == 3:
           return 1
       else:
           return 0
    else:
       if 3 <= vars['total'] < 5:
           return 1
       else:
           return 0

def make_update_function():
    r = Rule([
        partA,
        partB
    ])

    def update(state, x, y):
        vars = {'value' : state[x, y]}
        return r(state, x, y, vars)

    return update
