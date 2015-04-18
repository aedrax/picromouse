from micromouse import cell


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
                maze_cell = cell.Cell()
                maze_cell.x = x
                maze_cell.y = y
                maze_cell.weight = j
                row.append(maze_cell)
                y += 1
            for j in range(half, full):
                maze_cell = cell.Cell()
                maze_cell.x = x
                maze_cell.y = y
                maze_cell.weight = j
                row.append(maze_cell)
                y += 1
            self.map.append(row)
            x += 1
        for i in list(reversed(range((size/2)))):
            full = size - 1 - i
            half = ((size - 1) / 2) - i
            row = []
            y = 0
            for j in list(reversed(range(half, full))):
                maze_cell = cell.Cell()
                maze_cell.x = x
                maze_cell.y = y
                maze_cell.weight = j
                row.append(maze_cell)
                y += 1
            for j in range(half, full):
                maze_cell = cell.Cell()
                maze_cell.x = x
                maze_cell.y = y
                maze_cell.weight = j
                row.append(maze_cell)
                y += 1
            self.map.append(row)
            x += 1