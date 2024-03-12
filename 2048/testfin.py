from tkinter import *
from jeu_2048 import *
from display_gridMe import *
from grid_2048 import *
from affichage_grille import *
from textual_2048 import *
from longvalues import *
import random


taille = int(ask_and_read_grid_size())
theme = THEMES[ask_and_read_grid_theme()]
grid = init_game(taille)


h = len(grid)*100
k = 0
while h > 500:
    h = h-len(grid)
    k = k+1
window = Tk()
window.title("grid_game")
window.geometry(str(h+2*(len(grid)+30))+"x"+str(h+2*(len(grid)+30)))
w = Toplevel(window, height=h+2*(len(grid)+1), width=h+2 *
                 (len(grid)+1), bg='white', highlightbackground='white')
w.title("graphical")
background = Frame(window, bg='#9C9C9C', )
background.pack()


for i in range(0, len(grid)):
    for j in range(0, len(grid)):

        locals()["case" + str(i*len(grid)+j)] = Canvas(background, bd="2",
                                                           bg=COULEURS[str(grid[i][j])], height=h/len(grid)-1, width=h/len(grid)-1)

        locals()["case" + str(i*len(grid)+j)].grid(row=i, column=j)
        locals()["case" + str(i*len(grid)+j)].create_text(55-k, 55-k,
                                                              text=theme[grid[i][j]], fill="black", font=('Helvetica 20 bold'), anchor='center', justify='center')


def clavier(event):
    global grid

    touche = event.keysym

    if touche == "Up":
        grid = move_grid(grid,"h")
    elif touche == "Down":
        grid = move_grid(grid,"b")
    elif touche == "Right":
        grid = move_grid(grid,"d")
    else:
        grid = move_grid(grid,"g")         
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            locals()["case" + str(i*len(grid)+j)].create_text(55-k, 55-k,text=theme[grid[i][j]], fill="black", font=('Helvetica 20 bold'), anchor='center', justify='center')

canvas = Canvas(window, width=500, height=500, bg="ivory")
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()

window.mainloop()
