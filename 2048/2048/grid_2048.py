import random


def create_grid(taille):
    # crée une grille vide
    game_grid = []
    for i in range(0, int(taille)):
        game_grid.append([' ']*int(taille))
    return game_grid


def get_value_new_tile():
    # donne la valeur 2 (proba 0,9) ou 4 (proba 0,1)
    a = random.random()
    if a < 0.9:
        return 2
    return 4


def grid_add_new_tile_at_position(grid, x, y):
    # ajoute une tile 2 ou 4 en position x,y
    grid[x][y] = get_value_new_tile()
    return grid


def get_all_tiles(grid):
    # renvoie la liste de toutes les tiles de la grille
    all_tiles = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if type(grid[i][j]) == int:
                all_tiles.append(grid[i][j])
            else:
                all_tiles.append(0)
    return all_tiles


def get_empty_tiles_positions(grid):
    # renvoie la liste des positions des cases vides (ou 0)
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if type(grid[i][j]) != int or grid[i][j] == 0:
                positions.append((i, j))
                grid[i][j] = 0
    return positions


def get_new_position(grid):
    # prend une position au hasard parmi les cases vides
    return random.choice(get_empty_tiles_positions(grid))


def grid_get_value(grid, x, y):
    # renvoie la valeur dans la case x,y
    return grid[x][y]


def grid_add_new_tile(grid):
    # ajoute une nouvelle tile au hasard dans une case vide
    (x, y) = get_new_position(grid)
    grid_add_new_tile_at_position(grid, x, y)
    return grid


def init_game(taille):
    # crée une nouvelle grille avec 2 tiles
    grid = create_grid(taille)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)
    return grid


def move_row_left(row):
    longueur = len(row)
    row = list(filter(lambda a: a != 0, row))
    for i in range(0, len(row)-1):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] = 2*row[i]
            row[i+1] = 0
    row = list(filter(lambda a: a != 0, row))
    k = longueur - len(row)
    while k > 0:
        row.append(0)
        k = k-1
    return (row)


def move_row_right(row):
    return (list(reversed(move_row_left(list(reversed(row))))))


def move_row_haut(row):
    return (move_row_left(row))


def move_row_bas(row):
    return (move_row_right(row))


def transpose_grid(grid):
    transposed_grid = []
    colonne = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            colonne.append(grid[j][i])
        transposed_grid.append(colonne)
        colonne = []
    return (transposed_grid)


def move_grid(grid, key):
    if key == "g":
        for i in range(len(grid)):
            grid[i] = move_row_left(grid[i])
    if key == "d":
        for i in range(len(grid)):
            grid[i] = move_row_right(grid[i])
    if key == "h":
        grid = transpose_grid(grid)
        for i in range(len(grid)):
            grid[i] = move_row_haut(grid[i])
        grid = transpose_grid(grid)
    if key == "b":
        grid = transpose_grid(grid)
        for i in range(len(grid)):
            grid[i] = move_row_bas(grid[i])
        grid = transpose_grid(grid)
    return (grid)


def is_grid_full(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return (False)
    return (True)


def move_possible(grid):
    possible = [False, False, False, False]
    for i in range(len(grid)):                                  # test gauche
        if move_row_left(grid[i]) != grid[i]:
            possible[0] = True

    for i in range(len(grid)):                                  # test droite
        if move_row_right(grid[i]) != grid[i]:
            possible[1] = True

    grid = transpose_grid(grid)
    for i in range(len(grid)):                                  # test haut
        if move_row_haut(grid[i]) != grid[i]:
            possible[2] = True

    for i in range(len(grid)):                                  # test bas
        if move_row_bas(grid[i]) != grid[i]:
            possible[3] = True

    return (possible)


def valeur_voisine(grid, i):
    # renvoie la valeur situé a gauche de la valeur en position i dans grid sans tenir compte des zeros#
    k = i+1  # on ne regarde pas grid[len(grid)-1]
    while grid[k] == 0:
        k += 1
    return grid[k]


def is_game_over(grid):
    if is_grid_full(grid) == True and move_possible(grid) == [False, False, False, False]:
        return (True)
    else:
        return (False)


def get_grid_tile_max(grid):
    k = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > k:
                k = grid[i][j]
    return (k)


def win_or_lose(grid):
    return (get_grid_tile_max(grid) >= 2048)
