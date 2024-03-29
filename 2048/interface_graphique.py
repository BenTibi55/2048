import tkinter as tk


def quitter():
    global root

    def oui():
        print("Merci d'avoir jouer!")
        root.destroy()  # Détruit la fenêtre

    def non():
        print('Ok, ok je reste!')
        fenTop.destroy()  # Détruit la fenêtre
        root.deiconify()  # Remet la fenêtre principale

    root.withdraw()  # Réduit la fenêtre (sans la détruire)

    fenTop = tk.Toplevel()  # Créer une nouvelle fenêtre TopLevel

    msg = tk.Message(fenTop, text="Voulez-vous quitter?")
    msg.pack()

    btnOui = tk.Button(fenTop, text="Oui", command=oui)
    btnOui.pack()

    btnNon = tk.Button(fenTop, text="Non", command=non)
    btnNon.pack()


root = tk.Tk()

canva = tk.Canvas(root, width=500, height=500)
canva.pack()

btnQuitter = tk.Button(root, text="Quitter", command=quitter)
btnQuitter.pack()

root.mainloop()
