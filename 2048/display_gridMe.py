from tkinter import *

COULEURS = {" ": "#7F7F7F", "0": "#7F7F7F", "2": "#FFF", "4": "#FFE1DE", "8": "#FFC2BE", "16": "#FFA29F", "32": "#FF8080", "64": "#FF5A64", "128": "#FF2048",
            "256": "#A98683", "512": "#7A1F26", "1024": "#512A1C", "2048": "#FF20A0", "4096": "#C7CF00", "8192": "#708D23"}

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                   32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def init_2048_graphical_grid():
    window = Tk()
    window.title("2048")
    w = Toplevel(window)
    w.grid()
    w.title("2048")
    window.mainloop()


'''

window = Tk()
window.title("2048")
window.geometry('450x450')
w = Toplevel(window, bg='white', highlightbackground='white')
w.title("2048")
background = Frame(window, bg='#9C9C9C', )
background.pack()
case1 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case1.grid(row=0, column=0)
case2 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case2.grid(column=0, row=1)
case3 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case3.grid(column=0, row=2)
case4 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case4.grid(column=0, row=3)
case5 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case5.grid(column=1, row=0)
case6 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case6.grid(column=1, row=1)
case7 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case7.grid(column=1, row=2)
case8 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case8.grid(column=1, row=3)
case9 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case9.grid(column=2, row=0)
case10 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case10.grid(column=2, row=1)
case11 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case11.grid(column=2, row=2)
case12 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case12.grid(column=2, row=3)
case13 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case13.grid(column=3, row=0)
case14 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case14.grid(column=3, row=1)
case15 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case15.grid(column=3, row=2)
case16 = Canvas(background, bd="2", bg='#7F7F7F', height='100', width='100')
case16.grid(column=3, row=3)

window.mainloop()

'''


def display_grid(grid, theme):
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


"""def afficher_tuiles(grid):
    for ligne in range(len(grid)):
        for colonne in range(len(grid)):
            canvas(nom à changer).create_text(100, 100, text=theme[grid[ligne][colonne]], fill="black", font=('Helvetica 15 bold'))
            case(nom var à changer) = Canvas(background, bd="2", bg=COULEURS[grid[ligne][colonne]], height='100', width='100')

"""


     
