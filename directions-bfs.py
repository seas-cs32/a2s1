'''Finding driving directions for CS 32 Act II, Scene I'''

import maze

# Keep track of the solution path
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


def search(my_map):
    g = my_map.grid
    frontier = []
    visited = []

    # Initialize the variables used in the search loop
    # with values from the start location
    loc = my_map.start
    row, col = loc
    g[row][col].content = '*'
    cur_node = Node(loc, None, None)
    visited.append(cur_node)

    while loc != my_map.goal:
        row, col = loc

        # Based on the available moves from here, add new locations
        # to the frontier list.  A move is available if there's not
        # a wall in that direction and we haven’t previously visited
        # that location.
        if not g[row][col].north and g[row-1][col].content != '*':
            new_loc = (row-1, col)
            new_node = Node(new_loc, cur_node, 'north')
            frontier.append(new_node)
            g[row-1][col].content = '*'
        if not g[row][col].south and g[row+1][col].content != '*':
            new_loc = (row+1, col)
            new_node = Node(new_loc, cur_node, 'south')
            frontier.append(new_node)
            g[row+1][col].content = '*'
        if not g[row][col].east and g[row][col+1].content != '*':
            new_loc = (row, col+1)
            new_node = Node(new_loc, cur_node, 'east')
            frontier.append(new_node)
            g[row][col+1].content = '*'
        if not g[row][col].west and g[row][col-1].content != '*':
            new_loc = (row, col-1)
            new_node = Node(new_loc, cur_node, 'west')
            frontier.append(new_node)
            g[row][col-1].content = '*'

        # We're done processing the cur_node
        visited.append(cur_node)

        if len(frontier) == 0:
            print('No solution')
            return

        # Choose a location from the frontier as next to explore
        cur_node = frontier.pop(0)
        loc = cur_node.state
        row, col = loc

        my_map.print()

    # Follow the parent links from cur_node to create
    # the actual driving directions
    ddirections = [cur_node]
    while cur_node.parent:
        cur_node = cur_node.parent
        ddirections.insert(0, cur_node)

    # Print out the driving directions
    print('## Solution ##')
    print(f'Starting at {ddirections[0].state}')
    ddirections.pop(0)
    for n in ddirections:
        print(f'Go {n.action} then')
    print('Arrive at your goal')
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

if __name__ == '__main__':
    main()