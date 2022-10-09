import numpy as np
import json

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

def json_to_object(data):
    m = {
        "PartA" : PartA,
        "Sequence" : Sequence,
        "Iff" : Iff,
        "Return" : Return
    }
    return m[data['type']].build_from_json(data)

class Sequence:

    def __init__(self, stuff):
        self.c = stuff

    def __call__(self, state, x, y, vars):

        for w in self.c:
            x = w(state, x, y, vars)
            if x is not None:
                return x

    @staticmethod
    def build_from_json(data):
        l = [json_to_object(item) for item in data['stuff']]
        return Sequence(l)


class Iff:

    class Condition:

        def __init__(self, var, lower, upper):
            self.var = var
            self.lower = lower
            self.upper = upper

        def __call__(self, vars):
            return self.lower <= vars[self.var] < self.upper

        @staticmethod
        def build_from_json(data):
            var = data['var']
            lower = data['lower']
            upper = data['upper']
            return Iff.Condition(var, lower, upper)

    def __init__(self, cond, tt, ff):
        self.cond = cond
        self.tt = tt
        self.ff = ff

    def __call__(self, state, x, y, vars):
        if self.cond(vars):
            return self.tt(state, x, y, vars)
        else:
            return self.ff(state, x, y, vars)

    @staticmethod
    def build_from_json(data):
        cond = Iff.Condition.build_from_json(data['condition'])
        tt = json_to_object(data['tt'])
        ff = json_to_object(data['ff'])
        return Iff(cond, tt, ff)

class Return:

    def __init__(self, value):
        self.value = value

    def __call__(self, state, x, y, vars):
        return self.value

    @staticmethod
    def build_from_json(data):
        value = data['value']
        return Return(value)

class PartA:

    def __init__(self, radius):
        self.radius = radius

    def __call__(self, state, x, y, vars):
        vars['total'] = get_surrounded_total(state, x, y, radius = self.radius)

    @staticmethod
    def build_from_json(data):
        radius = data['radius']
        return PartA(radius)


def make_update_function():

    #r = Sequence([
    #    PartA(1),
    #    Iff(
    #        lambda vars : vars['value'] == 0,
    #        Iff(
    #            lambda vars : vars['total'] == 3,
    #            Return(1),
    #            Return(0)
    #        ),
    #        Iff(
    #            lambda vars : 3 <= vars['total'] < 5,
    #            Return(1),
    #            Return(0)
    #        )
    #    )
    #])

    with open("def.json") as f:
        data = json.load(f)
    r = json_to_object(data)

    def update(state, x, y):
        vars = {'value' : state[x, y]}
        return r(state, x, y, vars)

    return update
