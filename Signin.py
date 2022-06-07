from cProfile import label
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
from numpy import size
import tkinter as tk

#data of user
data = {}
data['user'] = []

# Tạo giao diện
window = tk.Tk()
window.geometry("500x700")
window.title("Mã hóa")

email = tk.StringVar()
name = tk.StringVar()
dob = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
passphase = tk.StringVar()

#save data after click register button
def register_click():
    data['user'].append({
        'email': email.get(),
        'name': name.get(),
        'dob': dob.get(),
        'phone': phone.get(),
        'address': address.get(),
        'passphase': passphase.get()
    })
    with open('/Users/anhquantran/Documents/GitHub/App/user.txt', 'a') as outfile:
        json.dump(data, outfile)

# Body
lbSignin = Label(window, text="SIGN IN", font=("arial", 25))
lbSignin.place(x=200, y=10)
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

eEmail = Entry(window,font = ('Arial',15),textvariable=email)
eEmail.place(x= 200, y= 100)
eName = Entry(window,font = ('Arial',15),textvariable=name)
eName.place(x= 200, y= 150)
eDOB = Entry(window,font = ('Arial',15),textvariable=dob)
eDOB.place(x= 200, y= 200)
ePhoneNumber = Entry(window,font = ('Arial',15),textvariable=phone)
ePhoneNumber.place(x= 200, y= 250)
eAddress = Entry(window,font = ('Arial',15),textvariable=address)
eAddress.place(x= 200, y= 300)
ePassphase = Entry(window,font = ('Arial',15),textvariable=passphase,show='*')
ePassphase.place(x= 200, y= 350)

btnSignin = Button(window, text="REGISTER",command=register_click)
btnSignin.place(x=210, y=500)

# Hiển thị
window.mainloop()