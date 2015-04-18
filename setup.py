from micromouse import cell, mouse, maze

def begin():
    """
    :return: None. This function begins micromouse operation.
    """
    some_maze = maze.Maze(16)
    some_mouse = mouse.Mouse(0, 0, some_maze)
    some_mouse.set_coordinates(0, 0)
    path = some_mouse.find_path(maze)
    some_mouse.take_path(maze, path)


if __name__ == '__main__':
    begin()