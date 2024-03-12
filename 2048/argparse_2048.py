from jeu_2048 import *
from affichage_grille import *
from textual_2048 import *
from longvalues import *
from grid_2048 import *

import argparse

def game_play_argparse(taille,theme_choice) :
    grid = init_game(taille)
    print(grid_to_string_with_size_and_theme(grid, THEMES[theme_choice], taille))
    k = (is_game_over(grid))
    while k == False:
        mov = ask_and_read_command(grid)
        grid = move_grid(grid, mov)
        grid = grid_add_new_tile(grid)
        print(grid_to_string_with_size_and_theme(grid, THEMES[theme_choice],taille))
        k = is_game_over(grid)
    if win_or_lose(grid):
        print("Gagné !")
    else:
        print("Perdu !")

parser = argparse.ArgumentParser()
parser.add_argument("taille", help="choisis la taille de la grille de jeu (entre 2 et 19)", type=str)
parser.add_argument("theme", help="choisis le theme de jeu (0 : defaut ; 1 : chimie ; 2 : alphabet)", type=str)
args = parser.parse_args()
game_play_argparse(args.taille,args.theme)