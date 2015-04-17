"""

MICROMOUSE ALGORITHM
Python Edition

Written by Sam Roth
Last revised: 16 APRIL 2015

"""

import unittest


class Cell:
    x = 0
    y = 0
    weight = 0
    visited = None

    def __init__(self):
        self.visited = False

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
        x = 0
        for i in range(((size - 1) / 2) + 1):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            y = 0
            for j in list(reversed(range(half, full))):
                cell = Cell()
                cell.x = x
                cell.y = y
                cell.weight = j
                row.append(cell)
                y += 1
            for j in range(half, full):
                cell = Cell()
                cell.x = x
                cell.y = y
                cell.weight = j
                row.append(cell)
                y += 1
            self.map.append(row)
            x += 1
        for i in list(reversed(range((size/2)))):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            y = 0
            for j in list(reversed(range(half, full))):
                cell = Cell()
                cell.x = x
                cell.y = y
                cell.weight = j
                row.append(cell)
                y += 1
            for j in range(half, full):
                cell = Cell()
                cell.x = x
                cell.y = y
                cell.weight = j
                row.append(cell)
                y += 1
            self.map.append(row)
            x += 1


def sensor_read(sensor):
    return 0


def find_path(mouse, maze):
    """
    :param mouse: The mouse that will be navigating the maze.
    :param maze: The maze that has predefined cells with weights.
    :return: The cell object determined to be the best path.
    """
    xn = mouse.x - 1
    ye = mouse.y + 1
    xs = mouse.x + 1
    yw = mouse.y - 1
    n = maze.map[xn][mouse.y]
    e = maze.map[mouse.x][ye]
    s = maze.map[xs][mouse.y]
    w = maze.map[mouse.x][yw]
    options = [n, e, s, w]
    best_case = min(n.get_weight(), e.get_weight(), s.get_weight(), w.get_weight())
    best_options = []

    for i in options:
        if i.get_weight() is best_case:
            best_options.append(i)

    for i in best_options:
        print i.x, i.y, i.weight


def take_path(mouse, maze):
    """
    :param mouse: The mouse that will be navigating the maze.
    :param maze: The maze that has predefined cells with weights.
    :return: None; however, mouse.x and mouse.y are updated.
    """
    return 0


def begin():
    """
    :return: None. This function begins micromouse operation.
    """
    mouse = Mouse()
    maze = Maze(16)
    mouse.set_coordinates(0, 0)
    find_path(mouse, maze)
    take_path(mouse, maze)


if __name__ == '__main__':
    begin()