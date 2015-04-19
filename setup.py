from micromouse import mouse, maze


def begin():
    """
    :return: None. This function begins micromouse operation.
    """
    some_maze = maze.Maze(16)
    some_mouse = mouse.Mouse(0, 0, some_maze)

    print "Mouse initialized at (%d, %d)" % (some_mouse.x, some_mouse.y)

    while some_mouse.maze.map[some_mouse.x][some_mouse.y].get_weight() is not 0:
        path = some_mouse.find_path()
        some_mouse.take_path(path)
        print "Mouse moved to (%d, %d)" % (some_mouse.x, some_mouse.y)

    print "Mouse solved the maze."


if __name__ == '__main__':
    begin()