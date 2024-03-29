def long_value(grid):
    max = len(str(grid[0][0]))
    for l in grid:
        for e in l:
            w = len(str(e))
            if w > max:
                max = w
    return (max)


THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                   32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


# permet de relever la longueur maximale d'un élément de la grille
def long_value_with_theme(grid, t):
    max = len(t[grid[0][0]])
    for l in grid:
        for e in l:
            w = len(t[e])
            if w > max:
                max = w
    return (max)


def test_long_value_with_theme():
    grid = [[2048, 16, 32, 0], [0, 4, 0, 2], [0, 0, 0, 32], [512, 1024, 0, 2]]
    assert long_value_with_theme(grid, THEMES["0"]) == 4
    assert long_value_with_theme(grid, THEMES["1"]) == 2
    assert long_value_with_theme(grid, THEMES["2"]) == 1
    grid = [[16, 4, 8, 2], [2, 4, 2, 128], [
        4, 512, 32, 4096], [1024, 2048, 512, 2]]
    assert long_value_with_theme(grid, THEMES["0"]) == 4
    assert long_value_with_theme(grid, THEMES["1"]) == 2
    assert long_value_with_theme(grid, THEMES["2"]) == 1
