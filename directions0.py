'''Finding driving directions for CS 32 Act II, Scene I'''

import maze

def search(my_map):
    g = my_map.grid
    frontier = []

    loc = my_map.start
    row, col = loc
    g[row][col].content = '*'

    while loc != my_map.goal:
        row, col = loc

        # Based on the available moves from here, add new locations
        # to the frontier list.  A move is available if there's not
        # a wall in that direction and we haven’t previously added
        # that location to the frontier.
        if not g[row][col].north and g[row-1][col].content != '*':
            frontier.append((row-1, col))
            g[row-1][col].content = '*'
        if not g[row][col].south and g[row+1][col].content != '*':
            frontier.append((row+1, col))
            g[row+1][col].content = '*'
        if not g[row][col].east and g[row][col+1].content != '*':
            frontier.append((row, col+1))
            g[row][col+1].content = '*'
        if not g[row][col].west and g[row][col-1].content != '*':
            frontier.append((row, col-1))
            g[row][col-1].content = '*'

        if len(frontier) == 0:
            print('No solution')
            return

        # Choose a location from the frontier as next to explore
        loc = frontier.pop()
        row, col = loc

        my_map.print()

    return


def main():
    print('\nBuilding our map')
    my_map = maze.Maze(maze.MAZE_map, maze.MAZE_map_endpts)

    # Make it easier to see the roads
    for i in range(my_map.height+2):
        for j in range(my_map.width+2):
            c = my_map.grid[i][j]
            if c.north and c.south and c.east and c.west:
                c.content = '#'

    print(my_map)

    print('\nStarting the search')
    search(my_map)

    # Erase the non-road marks
    for i in range(my_map.height+2):
        for j in range(my_map.width+2):
            if my_map.grid[i][j].content == '#':
                my_map.grid[i][j].content = ' '

    print('\nSolution')
    print(my_map)

if __name__ == '__main__':
    main()