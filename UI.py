from crypto import Random
from crypto.PublicKey import RSA
import rsa
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
from numpy import size
import tkinter as tk
import re


# random_generator = Random.new().read
# (pubkey, privkey) = rsa.newkeys(2048)
random_generator = Random.new().read
key = RSA.generate(2048,random_generator)
privkey, pubkey = key, key.publickey()
#publickey = key.public_key # pub key export for exchange

window = tk.Tk()
window.geometry("700x700")
window.title("Mã hóa")

lbTitle = Label(window, text="ENCRYPT", font=('arial', 20))
lbTitle.place(x=300, y=50)
lbPub = Label(window, text="Public key", font=('arial', 15))
lbPub.place(x=50, y=100)
lbPriv = Label(window, text="Private key", font=('arial', 15))
lbPriv.place(x=50, y=350)

ePub = Text(window,font = ('Arial',15), width=40)
ePub.place(x=180, y=100,width=450, height=200)

ePriv = Text(window,font = ('Arial',15), width=40)
ePriv.place(x=180, y=350,width=450, height=200)

def GererateKey():
    ePub.insert(END,pubkey)
    ePub.config(state=DISABLED)
    ePriv.insert(END,privkey)
    ePriv.config(state=DISABLED)

btnGetKey = Button(master = window,text = 'GERERATE KEY',command= GererateKey)
btnGetKey.place(x=300, y=600)

window.mainloop()