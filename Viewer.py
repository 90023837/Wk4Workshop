import Maze

def view(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j] == maze.EMPTY:
                print("-- ", end="")

            elif grid[i][j] == maze.WALL:
                print("||", end="")

            elif grid[i][j] == maze.START:
                print("00", end="")

            elif grid[i][j] == maze.END:
                print("__", end="")

            elif griiid[i][j] == maze.VISITED:
                print("!!", end="")

            else:
                raise AssertionError
    print()
