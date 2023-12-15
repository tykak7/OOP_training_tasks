import random #random number generation


# creates a 2D maze:
def create_maze(width, height, max_tunnels):
    maze = [['▓' for _ in range(width)] for _ in range(height)]

    # the starting position is (1, 1)
    maze[1][1] = '.'

    # tracking your current position in the maze
    current_position = (1, 1)
    # all possible directions: right, left, up, down
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# generate a random tunnel length
    for _ in range(max_tunnels):
        direction = random.choice(directions)
        length = random.randint(1, max(width, height))

# inside the loop, a new position is checked for each step in the tunnel:
        for _ in range(length):
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

# if there is a new position inside the labyrinth, the dot symbol is placed at that position:
            if 0 < new_position[0] < height - 1 and 0 < new_position[1] < width - 1:
                maze[new_position[0]][new_position[1]] = '.'
                current_position = new_position

# creating walls around the labyrinth
    for i in range(width):
        maze[0][i] = '▓'
        maze[height - 1][i] = '▓'
    for i in range(height):
        maze[i][0] = '▓'
        maze[i][width - 1] = '▓'

    return maze

# listing the maze in the console
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Set maze size and maximum number of tunnels
width = 31
height = 11
max_tunnels = 43

# Maze generation and display
maze = create_maze(width, height, max_tunnels)
print_maze(maze)
