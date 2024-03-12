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
window.title("2048")
window.geometry(str(h+2*(len(grid)+30))+"x"+str(h+2*(len(grid)+30)))
w = Toplevel(window, height=h+2*(len(grid)+1), width=h+2 *
                 (len(grid)+1), bg='white', highlightbackground='white')
w.title("2048")
background = Frame(window, bg='#9C9C9C', )
background.pack()


for i in range(0, len(grid)):
    for j in range(0, len(grid)):

        locals()["case" + str(i*len(grid)+j)] = Canvas(background, bd="2",
                                                           bg=COULEURS[str(grid[i][j])], height=h/len(grid)-1, width=h/len(grid)-1)

        locals()["case" + str(i*len(grid)+j)].grid(row=i, column=j)
        locals()["case" + str(i*len(grid)+j)].create_text(55-k, 55-k,
                                                              text=theme[grid[i][j]], fill="black", font=('Helvetica 20 bold'), anchor='center', justify='center')
window.mainloop()

#JE FAIS LE TRUC AVEC W, ESSAYER AVEC WINDOW SI MARCHE PAS 

def gauche(event):
    if move_possible(grid)[0] :
        grid = move_grid(grid,"g")
def droit(event):
    if move_possible(grid)[1] :
        grid = move_grid(grid,"d")
def haut(event):
    if move_possible(grid)[2] :
        grid = move_grid(grid,"h")
def bas(event):
    if move_possible(grid)[3] :
        grid = move_grid(grid,"b")


k = is_game_over(grid)
while k == False:
   
    w.bind("<Button-1>",gauche)
    w.bind("<Button-3>",droit)
    w.bind("<Up>",haut)
    w.bind("<Down>",bas)
    w.pack()
    
    grid = grid_add_new_tile(grid)
    k = is_game_over(grid)
if win_or_lose(grid):
    print("Gagné !")
else:
    print("Perdu !")
 






