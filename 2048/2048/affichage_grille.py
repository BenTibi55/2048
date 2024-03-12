THEMES = {"0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                    32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: " ", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def grid_to_string(grid, taille):
    string_grille = ""
    for ligne in range(len(grid)):
        string_grille = string_grille+"  === "*taille
        string_grille = string_grille + "\n"
        for case in grid[ligne]:
            string_grille = string_grille + "|  "+str(case) + "  "
        string_grille = string_grille + "|" "\n "
        string_grille = string_grille+" ===  "*taille + "\n"
    return string_grille


def long_value(grid):
    max = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            longueur = len(str(grid[x][y]))
            if longueur > max:
                max = longueur
    return max


def grid_to_string_with_size(grid, n):
    string_grille = ""
    for ligne in range(len(grid)):
        string_grille = string_grille+"  === "*n
        string_grille = string_grille + "\n"
        for case in grid[ligne]:
            if len(str(case)) == 1:
                string_grille = string_grille + "|  "+str(case) + "  "
            if len(str(case)) == 2:
                string_grille = string_grille+"| "+str(case)+"  "
            if len(str(case)) == 3:
                string_grille = string_grille+"| "+str(case)+" "
            if len(str(case)) == 4:
                string_grille = string_grille+"|"+str(case)+" "
        string_grille = string_grille + "|" "\n "
        string_grille = string_grille+" ===  "*n + "\n"
    return string_grille


#print(grid_to_string_with_size([['2048', ' ', ' ', ' '], [' ', '16', ' ', ' '], [' ', '256', ' ', ' '], [2, ' ', ' ', 2]], 4))


def long_value_with_theme(grid, t):
    max = len(t[grid[0][0]])
    for l in grid:
        for e in l:
            w = len(t[e])
            if w > max:
                max = w
    return (max)


def grid_to_string_with_size_and_theme(grid, theme, n):
    string_grille = ""
    for ligne in range(len(grid)):
        string_grille = string_grille + "  === "*int(n)
        string_grille = string_grille + "\n"
        for case in grid[ligne]:
            case_theme = theme[case]
            if len(str(case_theme)) == 0:
                string_grille = string_grille + "|   "+str(case_theme) + "  "
            if len(str(case_theme)) == 1:
                string_grille = string_grille + "|  "+str(case_theme) + "  "
            if len(str(case_theme)) == 2:
                string_grille = string_grille+"| "+str(case_theme)+"  "
            if len(str(case_theme)) == 3:
                string_grille = string_grille+"| "+str(case_theme)+" "
            if len(str(case_theme)) == 4:
                string_grille = string_grille+"|"+str(case_theme)+" "
        string_grille = string_grille + "|" "\n "
        string_grille = string_grille+" ===  "*int(n) + "\n"
    return string_grille
