from micromouse import mouse, maze


def begin():
    """
    :return: None. This function begins micromouse operation.
    """
    some_maze = maze.Maze(16)
    some_mouse = mouse.Mouse(0, 0, some_maze)
    some_mouse.set_coordinates(0, 0)

    while some_mouse.maze.map[some_mouse.x][some_mouse.y].get_weight() is not 0:
        path = some_mouse.find_path()
        some_mouse.take_path(path)
        print some_mouse.x, some_mouse.y


if __name__ == '__main__':
    begin()