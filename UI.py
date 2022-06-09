import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import rsa
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
from numpy import size
import tkinter as tk
import re

random_generator = Random.new().read
(pubkey, privkey) = rsa.newkeys(512)
#publickey = key.public_key # pub key export for exchange

window = tk.Tk()
window.geometry("700x700")
window.title("Mã hóa")

lbTitle = Label(window, text="ENCRYPT", font=('arial', 20))
lbTitle.place(x=200, y=50)
lbPub = Label(window, text="Public key", font=('arial', 15))
lbPub.place(x=50, y=200)
lbPriv = Label(window, text="Private key", font=('arial', 15))
lbPriv.place(x=50, y=300)

ePub = Entry(window,font = ('Arial',15), width=40)
ePub.place(x=200, y=200)
ePriv = Entry(window,font = ('Arial',15), width=40)
ePriv.place(x=200, y=300)

def GererateKey():
    ePub.insert(0, pubkey)
    ePriv.insert(0, privkey)

btnGetKey = Button(master = window,text = 'GERERATE KEY',command= GererateKey)
btnGetKey.place(x=200, y=500)

window.mainloop()