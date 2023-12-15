import random #generování náhodných čísel


# vytvoří 2D bludiště:
def create_maze(width, height, max_tunnels):
    maze = [['▓' for _ in range(width)] for _ in range(height)]

    # startovní pozice je (1, 1)
    maze[1][1] = '.'

    # sledovaní aktuální pozici v bludišti
    current_position = (1, 1)
    # všichni možné směry: doprava, doleva, nahoru, dolů
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# vygenerujeme náhodnou délku tunelu
    for _ in range(max_tunnels):
        direction = random.choice(directions)
        length = random.randint(1, max(width, height))

# uvnitř smyčky se pro každý krok v tunelu kontroluje nová pozice:
        for _ in range(length):
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

# je-li nová pozice uvnitř labyrintu, na tuto pozici umístěn symbol tečky:
            if 0 < new_position[0] < height - 1 and 0 < new_position[1] < width - 1:
                maze[new_position[0]][new_position[1]] = '.'
                current_position = new_position

# vytvoření stěn kolem labyrintu
    for i in range(width):
        maze[0][i] = '▓'
        maze[height - 1][i] = '▓'
    for i in range(height):
        maze[i][0] = '▓'
        maze[i][width - 1] = '▓'

    return maze

# vypsání bludiště do konzoly
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Nastavení velikosti bludiště a maximálního počtu tunelů
width = 31
height = 11
max_tunnels = 43

# Generování a zobrazení bludiště
maze = create_maze(width, height, max_tunnels)
print_maze(maze)