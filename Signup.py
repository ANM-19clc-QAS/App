from cProfile import label
from datetime import datetime
from time import time
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import tkinter as tk
import re
import hashlib
from tokenize import String
import uuid
from tkcalendar import DateEntry
from difflib import SequenceMatcher
import time 
import datetime as dt

data = []
path = '/Users/anhquantran/Documents/GitHub/App/'
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"

#get the probability of a string being similar to another string
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def valid_email(input):
    lbEmail_valid = Label(window, text='Valid                                                                    ',font=('arial',9))
    lbEmail_valid.config(foreground="green")
    lbEmail_error = Label(window, text='Email is not valid! Please try again',font=('arial',10))
    lbEmail_error.config(foreground="red")
    if(re.search(regex_email,input) and input.isalpha):
        lbEmail_error.destroy()
        lbEmail_valid.place(x=201,y=130)
        btnSignup.config(state='active')  
        return True        
    else:
        lbEmail_valid.destroy()
        lbEmail_error.place(x=201,y=130)
        btnSignup.config(state='disabled')  
        return False 

def valid_name(input):
    lbName_valid = Label(window, text='Valid                                                                    ',font=('arial',9))
    lbName_valid.config(foreground="green")
    lbName_error = Label(window, text='Name is not valid! Please try again',font=('arial',10))
    lbName_error.config(foreground="red")
    if(re.search(regex_name,input) and input.isalpha and len(input)<50):
        lbName_error.destroy()
        lbName_valid.place(x=201,y=180)
        btnSignup.config(state='active')  
        return True        
    else:
        lbName_valid.destroy()
        lbName_error.place(x=201,y=180)
        btnSignup.config(state='disabled')  
        return False 

def valid_dob(input):
    day,month,year = input.split('/')

    isValidDate = True
    try :
        dt.datetime(int(year),int(month),int(day))
        dt.datetime(int(day), int(month), int(year))
        dt.datetime(int(year), int(month),int(day))
    except ValueError :
        isValidDate = False

    lbDOB_valid = Label(window, text='Valid                                                                    ',font=('arial',9))
    lbDOB_valid.config(foreground="green")
    lbDOB_error = Label(window, text='Date of birth is not valid! Please try again',font=('arial',10))
    lbDOB_error.config(foreground="red")
    
    if(isValidDate):
        lbDOB_error.destroy()
        lbDOB_valid.place(x=201,y=230)
        btnSignup.config(state='active')  
        return True        
    else:
        lbDOB_valid.destroy()
        lbDOB_error.place(x=201,y=230)
        btnSignup.config(state='disabled')  
        return False 

def valid_phone(input):
    lbPhone_valid = Label(window, text='Valid                                                                    ',font=('arial',9))
    lbPhone_valid.config(foreground="green")
    lbPhone_error = Label(window, text='Phone number is not valid! Please try again',font=('arial',10))
    lbPhone_error.config(foreground="red")
    
    # Entry with 10 numbers is ok
    if len(input) == 10 and input.isnumeric(): 
        lbPhone_error.destroy()
        lbPhone_valid.place(x = 201,y = 280)
        btnSignup.config(state='active')
        return True
    # Anything else, reject it
    else:
        lbPhone_valid.destroy()
        lbPhone_error.place(x = 201,y = 280) 

        btnSignup.config(state='disabled')  
        return False

#Passphase validation
def passphrase_format(passph):

    SpecialSym =['$', '@', '#', '%', ' ', '.', '?', '_', '-', '/', ',']
    val = True
      
    if len(passph) < 6:
        val = False
          
    if len(passph) > 20:
        val = False
          
    if not any(char.isdigit() for char in passph):
        val = False
          
    if not any(char.isupper() for char in passph):
        val = False
          
    if not any(char.islower() for char in passph):
        val = False
          
    if not any(char in SpecialSym for char in passph):
        val = False

    if similar(passph,str(email))>=0.05:
        val= False

    if similar(passph,str(name))>=0.05:
        val= False

    if similar(passph,str(email))>=0.05:
        val= False  

    if similar(passph,str(dob))>=0.05:
        val= False  

    if similar(passph,str(phone))>=0.05:
        val= False   

    if val:
        return val

def valid_pass(input):
    lbPass_valid = Label(window, text='Valid                                                                    \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       '
    ,font=('arial',9))
    lbPass_valid.config(foreground="green")
    lbPass_error = Label(window, text='Passphrase is not valid!\nPlease create a passphrase that meets the following conditions:\n- Length from 6 to 20 characters.\n- Includes special characters: \'$\', \'@\', \'#\', \'%\', \' \', \'.\', \'?\', \'_\', \'-\', \'/\', \',\'\n- Uppercase and lowercase letters.\n- Number.\n- Not the same as the information entered above.',font=('arial',10))
    lbPass_error.config(foreground="red")
    
    if passphrase_format(input)==TRUE:
        lbPass_error.destroy()
        lbPass_valid.place(x = 201,y = 400)
        btnSignup.config(state='active')
        return True

    # Anything else, reject it
    else:
        lbPass_valid.destroy()
        lbPass_error.place(x = 201,y = 400) 
        btnSignup.config(state='disabled')
        return False

# def success():
#   newWin = Toplevel(root)
#   newWin.title("New page")
#   newWin.geometry("700x400")

# Create UI
window = tk.Tk()
window.geometry("500x700")
window.title("Mã hóa")
mailValid = window.register(valid_email)
nameValid = window.register(valid_name)
dobValid = window.register(valid_dob)
phoneValid = window.register(valid_phone)
passValid = window.register(valid_pass)

#input
email = tk.StringVar
name = tk.StringVar
dob = tk.StringVar
phone = tk.StringVar
address = tk.StringVar
passphrase = tk.StringVar

#save data after click register button
def register_click():
    salt = uuid.uuid4().hex
    hash_object = hashlib.sha256(salt.encode() + str(passphrase.get()).encode('utf-8'))
    #with open(path+'user.txt') as fin:
    #    data = json.load(fin)

    data.append({
        'email': email.get(),
        'name': name.get(),
        'dob': dob.get(),
        'phone': phone.get(),
        'address': address.get(),
        'passphrase': hash_object.hexdigest()+':'+salt
    })

    with open(path+'user.txt', 'w') as fout:
        json.dump(data, fout, indent=4, separators=(',',': '))

# def check_empty_email() :
#      if eEmail.get():
#          pass     #your function where you want to jump
#      else:
#         print('Input email required')

# def check_empty_name() :
#      if eName.get():
#          pass     #your function where you want to jump
#      else:
#         print('Input name required')

# def check_empty_phone() :
#      if ePhoneNumber.get():
#          pass     #your function where you want to jump
#      else:
#         print('Input phone number required')

def showPass():
    if(cShow_v.get()==1):
        ePassphrase.config(show='')
    else:
        ePassphrase.config(show='*')

# def combine_funcs(*funcs):
#     def combined_func(*args, **kwargs):
#         for f in funcs:
#             f(*args, **kwargs)
#     return combined_func

# Body
lbSignup = Label(window, text="SIGN UP", font=("arial", 25))
lbSignup.place(x=200, y=10)
lbEmail = Label(window, text='Email',font=('arial',15))
lbEmail.place(x = 50,y = 100)
lbName = Label(window, text='Full Name',font=('arial',15))
lbName.place(x = 50,y = 150)
lbDOB = Label(window, text='Date of birth',font=('arial',15))
lbDOB.place(x = 50,y = 200)
lbPhoneNumber = Label(window, text='Phone number',font=('arial',15))
lbPhoneNumber.place(x = 50,y = 250)
lbAddress = Label(window, text='Address',font=('arial',15))
lbAddress.place(x = 50,y = 300)
lbPassphrase = Label(window, text='Passphrase',font=('arial',15))
lbPassphrase.place(x = 50,y = 350)

eEmail = Entry(window,font = ('Arial',15),textvariable=email,validate='focusout',validatecommand=(mailValid,'%P'))
eEmail.place(x= 200, y= 100)
eName = Entry(window,font = ('Arial',15),textvariable=name,validate='focusout',validatecommand=(nameValid,'%P'))
eName.place(x= 200, y= 150)
eDOB = DateEntry(window,font = ('Arial',15),fieldbackground='light green',background= 'lemonchiffon', 
                foreground= 'dark blue',textvariable=dob,selectmode='day',maxdate=datetime.today(),
                showweeknumbers=FALSE,selectforeground='red',validate='focusout',validatecommand=(dobValid,'%P'))
eDOB.place(x= 201, y= 200)
ePhoneNumber = Entry(window,font = ('Arial',15),textvariable=phone,validate='focusout',validatecommand=(phoneValid,'%P'))
ePhoneNumber.place(x= 200, y= 250)
phone_check = phone
eAddress = Entry(window,font = ('Arial',15),textvariable=address,validate='focusout')
eAddress.place(x= 200, y= 300)
ePassphrase = Entry(window,font = ('Arial',15),textvariable=passphrase,show='*',validate='focusout',validatecommand=(passValid,'%P'))
ePassphrase.place(x= 200, y= 350)

cShow_v = IntVar(value=0)
cShowPass = Checkbutton(window,text='Show passphrase',variable=cShow_v,onvalue=1,offvalue=0,command=showPass)
cShowPass.place(x=200, y=380)

btnSignup = Button(window, text="REGISTER",state=DISABLED,command=register_click)
btnSignup.place(x=210, y=500)

# Hiển thị
window.mainloop()

# Lỗi similar nên không write data được