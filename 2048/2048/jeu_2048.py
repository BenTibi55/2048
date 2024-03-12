from grid_2048 import *
from affichage_grille import *
from textual_2048 import *
from longvalues import *
import random

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                   32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                   32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def ask_and_read_grid_size():
    # choix de la taille de la grille
    taille = input("Entrez la taille de la grille :")
    while taille not in [str(i) for i in range(2,20)]:
        taille = input("Erreur ! Taille non prise en charge ! Entrez la taille de la grille :")
    return taille


def ask_and_read_grid_theme():
    # choix du thème du jeu
    theme = input(
        "Entrez le thème du jeu (default (0), chimie(1), alphabet(2)) :")
    while (theme not in ["0", "1", "2"]):
        theme = input(
            "Thème non valide ! Entrez le thème du jeu (default (0), chemistry(1), alphabet(2)) :")
    return theme


def ask_and_read_command(grid):
    # choix de la translation (gauche g, droite d, haut h ou bas b)
    list_mov = ["g", "d", "h", "b"]
    # détermination des choix possibles
    choix_mov = [x*y for x, y in zip(list_mov, move_possible(grid))]
    # multiplier le terme list_mov[i] qui symbolise la direction par le booléen correspondant à si le mouvement est possible dans cette direction
    for i in range(0, len(choix_mov)):
        if choix_mov[i] == '':
            choix_mov[i] = 0
    choix_mov = list(filter(lambda a: a != 0, choix_mov))
    command = input(("Entrez la direction de translation ", choix_mov, " :"))
    while command not in choix_mov:
        command = input(
            ("Commande non valide ! Entrez la direction de translation ", choix_mov, " :"))
    return (command)


def random_play():
    grid = init_game(4)
    print(grid_to_string_with_size(grid, 4))
    k = (is_game_over(grid))
    list_mov = ['g', 'd', 'h', 'b']
    while k == False:
        choix_mov = [x*y for x, y in zip(list_mov, move_possible(grid))]
        # multiplier le terme list_mov[i] qui symbolise la direction par le booléen correspondant à si le mouvement est possible dans cette direction
        for i in range(0, len(choix_mov)):
            if choix_mov[i] == '':
                choix_mov[i] = 0
        choix_mov = list(filter(lambda a: a != 0, choix_mov))
        # Supprime les 0 de la liste (les zéros ont remplacé les directions impossible)
        mov = random.choice(choix_mov)
        # Choix parmi les directions possibles définies grâce aux deux étapes précédentes
        grid = move_grid(grid, mov)
        grid = grid_add_new_tile(grid)
        print(grid_to_string_with_size(grid, 4))
        k = is_game_over(grid)
        print(k)
    print(win_or_lose(grid))
    return (0)


# random_play()


def game_play():

    taille = int(ask_and_read_grid_size())
    theme_choice = ask_and_read_grid_theme()
    grid = init_game(taille)
    print(grid_to_string_with_size_and_theme(
        grid, THEMES[theme_choice], taille))
    k = (is_game_over(grid))
    while k == False:
        mov = ask_and_read_command(grid)
        grid = move_grid(grid, mov)
        grid = grid_add_new_tile(grid)
        print(grid_to_string_with_size_and_theme(
            grid, THEMES[theme_choice], taille))
        k = is_game_over(grid)

    if win_or_lose(grid):
        print("Gagné !")
    else:
        print("Perdu !")

