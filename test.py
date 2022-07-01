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
from Crypto.Cipher import AES
import base64
import hashlib
import random

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

btnGetKey = Button(master = window,text = 'GERERATE KEY', command= GererateKey)
btnGetKey.place(x=200, y=500)


import pyaes, pbkdf2, binascii, os, secrets

# Derive a 256-bit AES encryption key from the password
passphase = "1234abcd"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(passphase, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key))

iv = secrets.randbits(256)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(str(privkey))
print('Encrypted:', binascii.hexlify(ciphertext))

# Decrypt
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print()
print('Decrypted:', decrypted)
print()

# String random
def random_session(length):
    str = '0123456789abcdefghijklmnopqrstuvwxyz'
    kSession = ''
    for i in range(length):
        kSession += random.choice(str)
    return kSession
kSession = random_session(16)

# Encrypt file
f = open("App/filename.txt")
text = f.read()
fpasswordSalt = os.urandom(16)
fkey = pbkdf2.PBKDF2(text, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(fkey))

fiv = secrets.randbits(256)
faes = pyaes.AESModeOfOperationCTR(fkey, pyaes.Counter(iv))
fciphertext = faes.encrypt(text)
print('Encrypted:', binascii.hexlify(fciphertext))


faes = pyaes.AESModeOfOperationCTR(fkey, pyaes.Counter(iv))
fdecrypted = faes.decrypt(fciphertext)
print()
print('Decrypted:', fdecrypted)
print()

# Encrypt
def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)
ciphertext = encrypt("abc11234", pubkey)
print(ciphertext)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

plaintext = decrypt(ciphertext, privkey)
print(plaintext)



window.mainloop()
