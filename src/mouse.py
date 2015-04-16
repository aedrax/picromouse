"""

MICROMOUSE ALGORITHM
Python Edition

Written by Sam Roth
Last revised: 14 APRIL 2015

"""


class Cell:

    weight = 0

    def get_weight(self):
        return self.weight


class Mouse:

    x = 0
    y = 0

    n_distance = 0
    e_distance = 0
    s_distance = 0
    w_distance = 0

    def __init__(self):
        print "Hello world!"

    def get_coordinates(self):
        return [self.x, self.y]

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_data(self, n, e, s, w):
        self.n_distance = sensor_read(n)
        self.e_distance = sensor_read(e)
        self.s_distance = sensor_read(s)
        self.w_distance = sensor_read(w)


class Maze:

    map = []

    def __init__(self, size):

        for i in range(((size - 1) / 2) + 1):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            for j in list(reversed(range(half, full))):
                cell = Cell()
                cell.weight = j
                row.append(cell)
            for j in range(half, full):
                cell = Cell()
                cell.weight = j
                row.append(cell)
            self.map.append(row)

        for i in list(reversed(range((size/2)))):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            for j in list(reversed(range(half, full))):
                cell = Cell()
                cell.weight = j
                row.append(cell)
            for j in range(half, full):
                cell = Cell()
                cell.weight = j
                row.append(cell)
            self.map.append(row)


def sensor_read(sensor):
    return 0


def begin():

    mouse = Mouse()
    mouse.set_coordinates(0, 0)

    n = 0
    e = 0
    s = 0
    w = 0

    print maze.map[0][0].get_weight()

    # while True:
    #   mouse.get_data(n, e, s, w)
    #   Next, compare the four values.


if __name__ == '__main__':
    maze = Maze(8)
    begin()