from cProfile import label
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter

from numpy import size

# Tạo giao diện
windown = Tk()
windown.geometry("500x700")
windown.title("Mã hóa")

# Body
lbSignin = Label(windown, text="SIGN IN", font=("arial", 25))
lbSignin.place(x=200, y=10)
lbEmail = Label(windown, text='Email',font=('arial',15))
lbEmail.place(x = 50,y = 100)
lbName = Label(windown, text='Name',font=('arial',15))
lbName.place(x = 50,y = 150)
lbDOB = Label(windown, text='Date of birth',font=('arial',15))
lbDOB.place(x = 50,y = 200)
lbPhoneNumber = Label(windown, text='Phone number',font=('arial',15))
lbPhoneNumber.place(x = 50,y = 250)
lbAddress = Label(windown, text='Address',font=('arial',15))
lbAddress.place(x = 50,y = 300)
lbPassphase = Label(windown, text='Passphase',font=('arial',15))
lbPassphase.place(x = 50,y = 350)

eEmail = Entry(windown,font = ('Arial',15))
eEmail.place(x= 200, y= 100)
eName = Entry(windown,font = ('Arial',15))
eName.place(x= 200, y= 150)
eDOB = Entry(windown,font = ('Arial',15))
eDOB.place(x= 200, y= 200)
ePhoneNumber = Entry(windown,font = ('Arial',15))
ePhoneNumber.place(x= 200, y= 250)
eAddress = Entry(windown,font = ('Arial',15))
eAddress.place(x= 200, y= 300)
ePassphase = Entry(windown,font = ('Arial',15))
ePassphase.place(x= 200, y= 350)

btnSignin = Button(windown, text="REGISTER")
btnSignin.place(x=210, y=500)

# Hiển thị
windown.mainloop()