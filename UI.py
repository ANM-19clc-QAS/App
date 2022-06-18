from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
from numpy import size
import tkinter as tk
import re

random_generator = Random.new().read
key = RSA.generate(2048,random_generator)
privkey, pubkey = key.exportKey().splitlines()[1:-1], key.publickey().exportKey().splitlines()[1:-1]

winGen = tk.Tk()
winGen.geometry("700x700")
winGen.title("Mã hóa")

lbTitle = Label(winGen, text="ENCRYPT", font=('arial', 20))
lbTitle.place(x=300, y=50)
lbPub = Label(winGen, text="Public key", font=('arial', 15))
lbPub.place(x=50, y=100)
lbPriv = Label(winGen, text="Private key", font=('arial', 15))
lbPriv.place(x=50, y=350)

ePub = Text(winGen,font = ('Arial',15), width=40)
ePub.place(x=180, y=100,width=450, height=200)

ePriv = Text(winGen,font = ('Arial',15), width=40)
ePriv.place(x=180, y=350,width=450, height=200)

def GererateKey():
    ePub.insert(END,pubkey)
    ePub.config(state=DISABLED)
    ePriv.insert(END,privkey)
    ePriv.config(state=DISABLED)

btnGetKey = Button(master = winGen,text = 'GERERATE KEY',command= GererateKey)
btnGetKey.place(x=300, y=600)

winGen.mainloop()