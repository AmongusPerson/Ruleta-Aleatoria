from tkinter import *
import random

pg = Tk()
pg.geometry("500x500")
pg.title("Ruleta Aleatoria")
pg.configure(background="#264653")

lb1 = Label(pg, text="Ruleta Aleatoria", bg="#2a9d8f", fg="white")
lb1.place(relx=0.5, rely=0.04, anchor=CENTER,)

lb2 = Label(pg, text=".", bg="#2a9d8f", fg="white")
lb2.place(relx=0.5, rely=0.11, anchor=CENTER,)

lb3 = Label(pg, text=".", bg="#2a9d8f", fg="white")
lb3.place(relx=0.5, rely=0.25, anchor=CENTER,)

lista = ["rojo","azul","amarillo","verde","morado"]
va = 0

def fn():
    va = random.randint(0,4)
    print(va)
    lb3["text"] = lista[va]
    lb2["text"] = str(va)
bt1 = Button(pg, text="Generar", bg="#e76f51", fg="white", command=fn)
bt1.place(relx=0.5, rely=0.18, anchor=CENTER,)







pg.mainloop()
