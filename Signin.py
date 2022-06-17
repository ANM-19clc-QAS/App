from Signup import *
from fileinput import hook_encoded
from tkinter.font import BOLD
from cProfile import label
from time import time
from tkinter import *
from tkinter.ttk import *
import json
import tkinter as tk
import re
import hashlib
from tokenize import String
from tkinter import messagebox

path = '/Users/anhquantran/Documents/GitHub/App/'
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#data of user
users = {}
users['user'] = []

class User(object):
    def __init__(self, email, passphrase):
        self.email = email
        self.passphrase = passphrase

def showSignin():
    winsi.mainloop()

def object_decoder(obj):
    #print(obj['email'] + obj['email'])
    if 'email' in obj and 'passphrase' in obj:
        users['user'].append(User(obj['name'], obj['passphrase'])) 


def valid_email(input):
    if(re.search(regex_email,input) and input.isalpha):
        btnSignin.config(state='active')  
        return True        
    else:
        btnSignin.config(state='disabled')  
        return False 

def check_password(hashed_password, user_password):
    #print(hashed_password)
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def checkAccount():
    
    data_file = open(path+'user.txt').read()
    data = json.loads(data_file)

    for i in data:
        if (i["email"] == email.get()) & check_password(i['passphrase'],passphrase.get()):
            #print('pass')
            #notification.set('')
            success_signin()
            break
        else:
            #print("failure")
            notification.set("Not Right Password or Email")
    
    
def success_signin():
    if messagebox.showinfo('Message box',f'You have successfully sign in!',icon='info'):
        
        winsi.destroy()


def showPassIn():
    if(cShow_vin.get()==1):
        epassphrase.config(show='')
    else:
        epassphrase.config(show='*')

# Tạo giao diện
winsi = tk.Tk()
winsi.geometry("500x300")
winsi.title("Mã hóa")
mailValid = winsi.register(valid_email)

email = tk.StringVar()
passphrase = tk.StringVar()
notification = tk.StringVar()

# Body
lbSignup = Label(winsi, text="SIGN IN", font=("arial", 25))
lbSignup.place(x=200, y=40)
lbEmail = Label(winsi, text='Email',font=('arial',15))
lbEmail.place(x = 50,y = 100)
lbpassphrase = Label(winsi, text='passphrase',font=('arial',15))
lbpassphrase.place(x = 50,y = 150)

lbNotification = Label(winsi,font=('arial',10),textvariable=notification)
lbNotification.place(x = 200,y = 200)

eEmail = Entry(winsi,width=25,font = ('Arial',15),textvariable=email,validate='focusout',validatecommand=(mailValid,'%P'))
eEmail.place(x= 200, y= 100)
epassphrase = Entry(winsi,width=25,font = ('Arial',15),textvariable=passphrase,show='*')
epassphrase.place(x= 200, y= 150)

cShow_vin = IntVar(value=0)
cShowPass = Checkbutton(winsi,text='Show passphrase',variable=cShow_vin,onvalue=1,offvalue=0,command=showPassIn)
cShowPass.place(x=200, y=180)

btnSignin = Button(winsi, text="LOGIN",state=DISABLED,command=checkAccount)
btnSignin.place(x=210, y=220)

# Hiển thị


