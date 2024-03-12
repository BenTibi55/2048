import random
from builtins import *


def read_player_command():
    # commande entrée par le joueur
    move = input(
        "Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move not in ['g', 'd', 'h', 'b']:
        move = input(
            "Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move


def mock_input_return(x):
    # renvoie une commande au hasard
    commandes = ["g", "d", "h", "b"]
    return random.choice(commandes)


def read_size_grid():
    # choix de la taille de la grille
    taille = input("Entrez la taille de la grille :")
    while taille not in ["i" for i in range(20)]:
        taille = input("Erreur - Entrez la taille de la grille :")
    return taille


def read_theme_grid():
    # choix du thème du jeu
    thème = input(
        "Entrez le thème du jeu (default (0), chemistry(1), alphabet(2)) :")
    while thème not in ["0", "1", "2"]:
        input("Thème non valide - Entrez le thème du jeu (default (0), chemistry(1), alphabet(2)) :")
    return thème


if __name__ == '__main__':
    game_play()
    exit(1)
