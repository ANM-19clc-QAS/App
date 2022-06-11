from cProfile import label
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import tkinter as tk
import re
import hashlib
import uuid
from tkcalendar import DateEntry

data = []
path = '/Users/anhquantran/Documents/GitHub/App/'
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"

def valid_email(input):
    if(re.search(regex_email,input) and input.isalpha):
        btnSignup.config(state='active')  
        return True        
    else:
        btnSignup.config(state='disabled')  
        return False 

def valid_name(input):
    if(re.search(regex_name,input) and input.isalpha):
        btnSignup.config(state='active')  
        return True        
    else:
        btnSignup.config(state='disabled')  
        return False 



# Tạo giao diện
window = tk.Tk()
window.geometry("500x700")
window.title("Mã hóa")
mailValid = window.register(valid_email)
nameValid = window.register(valid_name)

email = tk.StringVar()
name = tk.StringVar()
dob = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
passphase = tk.StringVar()

#save data after click register button
def register_click():
    salt = uuid.uuid4().hex
    hash_object = hashlib.sha256(salt.encode() + str(passphase.get()).encode('utf-8'))
    with open(path+'user.txt') as fin:
        data = json.load(fin)

    data.append({
        'email': email.get(),
        'name': name.get(),
        'dob': dob.get(),
        'phone': phone.get(),
        'address': address.get(),
        'passphase': hash_object.hexdigest()+':'+salt
    })

    with open(path+'user.txt', 'w') as fout:
        json.dump(data, fout, indent=4, separators=(',',': '))


def check_empty_email() :
     if eEmail.get():
         pass     #your function where you want to jump
     else:
        print('Input email required')

def check_empty_name() :
     if eName.get():
         pass     #your function where you want to jump
     else:
        print('Input name required')

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

# Body
lbSignup = Label(window, text="SIGN UP", font=("arial", 25))
lbSignup.place(x=200, y=10)
lbEmail = Label(window, text='Email',font=('arial',15))
lbEmail.place(x = 50,y = 100)
lbName = Label(window, text='Name',font=('arial',15))
lbName.place(x = 50,y = 150)
lbDOB = Label(window, text='Date of birth',font=('arial',15))
lbDOB.place(x = 50,y = 200)
lbPhoneNumber = Label(window, text='Phone number',font=('arial',15))
lbPhoneNumber.place(x = 50,y = 250)
lbAddress = Label(window, text='Address',font=('arial',15))
lbAddress.place(x = 50,y = 300)
lbPassphase = Label(window, text='Passphase',font=('arial',15))
lbPassphase.place(x = 50,y = 350)

eEmail = Entry(window,font = ('Arial',15),textvariable=email,validate='focusout',validatecommand=(mailValid,'%P'))
eEmail.place(x= 200, y= 100)
eName = Entry(window,font = ('Arial',15),textvariable=name,validate='focusout',validatecommand=(nameValid,'%P'))
eName.place(x= 200, y= 150)
eDOB = DateEntry(window,font = ('Arial',15),textvariable=dob,selectmode='day')
eDOB.place(x= 200, y= 200)
ePhoneNumber = Entry(window,font = ('Arial',15),textvariable=phone)
ePhoneNumber.place(x= 200, y= 250)
eAddress = Entry(window,font = ('Arial',15),textvariable=address)
eAddress.place(x= 200, y= 300)
ePassphase = Entry(window,font = ('Arial',15),textvariable=passphase,show='*')
ePassphase.place(x= 200, y= 350)

btnSignup = Button(window, text="REGISTER",state=DISABLED,command=combine_funcs(register_click, check_empty_email, check_empty_name))
btnSignup.place(x=210, y=500)

# Hiển thị
window.mainloop()