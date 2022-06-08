from cProfile import label
from fileinput import hook_encoded
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import tkinter as tk
import re
import hashlib
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


#data of user
users = {}
users['user'] = []

class User(object):
    def __init__(self, email, passphase):
        self.email = email
        self.passphase = passphase


def object_decoder(obj):
    print(obj['email'] + obj['email'])
    if 'email' in obj and 'passphase' in obj:
        users['user'].append(User(obj['name'], obj['passphase'])) 


def valid_email(input):
    if(re.search(regex_email,input) and input.isalpha):
        btnSignin.config(state='active')  
        return True        
    else:
        btnSignin.config(state='disabled')  
        return False 

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def checkAccount():

    data_file = open('/Users/son.n/Desktop/Ngay 8_6/App/user.txt').read()
    print(data_file)
    data = json.loads(data_file)
    print(data["user"])





# Tạo giao diện
window = tk.Tk()
window.geometry("500x300")
window.title("Mã hóa")
mailValid = window.register(valid_email)

email = tk.StringVar()
name = tk.StringVar()
dob = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
passphase = tk.StringVar()


# Body
lbSignup = Label(window, text="SIGN IN", font=("arial", 25))
lbSignup.place(x=200, y=10)
lbEmail = Label(window, text='Email',font=('arial',15))
lbEmail.place(x = 50,y = 100)
lbPassphase = Label(window, text='Passphase',font=('arial',15))
lbPassphase.place(x = 50,y = 150)

eEmail = Entry(window,font = ('Arial',15),textvariable=email,validate='focusout',validatecommand=(mailValid,'%P'))
eEmail.place(x= 200, y= 100)
ePassphase = Entry(window,font = ('Arial',15),textvariable=passphase,show='*')
ePassphase.place(x= 200, y= 150)

btnSignin = Button(window, text="LOGIN",state=DISABLED,command=checkAccount)
btnSignin.place(x=210, y=200)

# Hiển thị
window.mainloop()
