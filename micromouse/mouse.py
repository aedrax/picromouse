from random import randint


class Mouse:
    x = 0
    y = 0
    n_distance = 0
    e_distance = 0
    s_distance = 0
    w_distance = 0

    def __init__(self, x, y, maze):
        print "Hello world!"
        self.x = x
        self.y = y
        maze.map[x][y].visited = True

    def sensor_read(self, direction):
        if direction is 'north':
            self.n_distance = 0
        elif direction is 'east':
            self.e_distance = 1
        elif direction is 'south':
            self.s_distance = 2
        elif direction is 'west':
            self.w_distance = 3
        else:
            print "Usage error: sensor_read(north|east|south|west)"

    def find_path(self, maze):
        xn = self.x - 1
        ye = self.y + 1
        xs = self.x + 1
        yw = self.y - 1
        n = maze.map[xn][self.y]
        e = maze.map[self.x][ye]
        s = maze.map[xs][self.y]
        w = maze.map[self.x][yw]
        options = [n, e, s, w]
        best_case = min(n.get_weight(), e.get_weight(), s.get_weight(), w.get_weight())
        best_options = []
        for i in options:
            if i.get_weight() is best_case:
                best_options.append(i)
        choice = randint(0, len(best_options) - 1)
        return best_options[choice]

    def take_path(self, maze, next_cell):
        print self.x, self.y
        self.x = next_cell.x
        self.y = next_cell.y
        print self.x, self.y

    def get_coordinates(self):
        return [self.x, self.y]

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def move_north(self):
        # Add current coordinates to stack
        # Move to north cell
        self.x -= 1

    def move_east(self):
        # Add current coordinates to stack
        # Move to east cell
        self.y += 1

    def move_south(self):
        # Add current coordinates to stack
        # Move to south cell
        self.x += 1

    def move_west(self):
        # Add current coordinates to stack
        # Move to west cell
        self.y -= 1