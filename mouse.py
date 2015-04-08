"""

MICROMOUSE ALGORITHM
Python Edition

Written by Sam Roth
Last revised: 14 APRIL 2015

"""


class Cell:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = x

    def coordinates(self):
        return [self.x, self.x]


class Mouse:

    x = 0
    y = 0

    def __init__(self):
        print "Hello world!"

    def get_coordinates(self):
        return [self.x, self.y]

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


class Maze:

    map = []

    def __init__(self, size):

        for i in range(((size - 1) / 2) + 1):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            for j in list(reversed(range(half, full))):
                row.append(j)
            for j in range(half, full):
                row.append(j)
            self.map.append(row)

        for i in list(reversed(range((size/2)))):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            for j in list(reversed(range(half, full))):
                row.append(j)
            for j in range(half, full):
                row.append(j)
            self.map.append(row)


def setup():
    mouse = Mouse()
    mouse.set_coordinates(0, 0)


def loop():
    while True:
        print "begin micromouse logic"

# BEGIN BEHAVIOR

if __name__ == '__main__':
    maze = Maze(16)
    print maze.map[7][7]

