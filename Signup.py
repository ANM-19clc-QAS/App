from click import command
from Signin import *
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
import datetime as dt

# Create UI
winsu = tk.Tk()
winsu.geometry("500x600")
winsu.title("Mã hóa")

path = '/Users/anhquantran/Documents/GitHub/App/'
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"

#get the probability of a string being similar to another string
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#load json file and store users into data
with open(path+'user.txt') as fin:
    data = json.load(fin)

def valid_email(input):

    #check email existance
    checkUserExist = False
    for i in data:
        if(i['email']==str(email.get())): 
            checkUserExist = True

    if re.search(regex_email,input) and input.isalpha and checkUserExist==False:
        lbEmail_valid = Label(winsu, text='✅ Valid                                                                              ',font=('arial',10))
        lbEmail_valid.config(foreground="green")
        lbEmail_valid.place(x=201,y=130)
        btnSignup.config(state='active')  
        return True 

    elif re.search(regex_email,input) and input.isalpha and checkUserExist==True:
        lbEmail_exist = Label(winsu, text='❌ Email has been registered! Please try another email!',font=('arial',10))
        lbEmail_exist.config(foreground="red")
        lbEmail_exist.place(x=201,y=130)
        btnSignup.config(state='disabled') 
        return False

    else:
        lbEmail_error = Label(winsu, text='❌ Email is not valid! Please try again',font=('arial',10))
        lbEmail_error.config(foreground="red")
        lbEmail_error.place(x=201,y=130)
        btnSignup.config(state='disabled')  
        return False 

def valid_name(input):
    lbName_valid = Label(winsu, text='✅ Valid                                                                    ',font=('arial',9))
    lbName_valid.config(foreground="green")
    lbName_error = Label(winsu, text='❌ Name is not valid! Please try again',font=('arial',10))
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

    lbDOB_valid = Label(winsu, text='✅ Valid                                                                    ',font=('arial',9))
    lbDOB_valid.config(foreground="green")
    lbDOB_error = Label(winsu, text='❌ Date of birth is not valid! Please try again',font=('arial',10))
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
    lbPhone_valid = Label(winsu, text='✅ Valid                                                                    ',font=('arial',9))
    lbPhone_valid.config(foreground="green")
    lbPhone_error = Label(winsu, text='❌ Phone number is not valid! Please try again',font=('arial',10))
    lbPhone_error.config(foreground="red")
    
    # Entry with 10 numbers is ok
    if len(input) == 10 and input.isnumeric(): 
        lbPhone_error.grid_remove()
        lbPhone_valid.place(x = 201,y = 280)
        btnSignup.config(state='active')
        return True
    # Anything else, reject it
    else:
        lbPhone_valid.grid_remove()
        lbPhone_error.place(x = 201,y = 280) 
        btnSignup.config(state='disabled')  
        return False

#passphrase validation
def passphrase_format():

    SpecialSym =['$', '@', '#', '%', ' ', '.', '?', '_', '-', '/', ',']
    val = True
    
    if len(str(ePassphrase.get())) < 6:
        val = False
          
    if len(str(ePassphrase.get())) > 20:
        val = False
          
    if not any(char.isdigit() for char in str(ePassphrase.get())):
        val = False
          
    if not any(char.isupper() for char in str(ePassphrase.get())):
        val = False
          
    if not any(char.islower() for char in str(ePassphrase.get())):
        val = False
          
    if not any(char in SpecialSym for char in str(ePassphrase.get())):
        val = False

    if similar(str(ePassphrase.get()),str(eEmail.get()))>=0.3:
        val= False

    if similar(str(ePassphrase.get()),str(eName.get()))>=0.3:
        val= False

    if similar(str(ePassphrase.get()),str(eDOB.get()))>=0.3:
        val= False  

    if similar(str(ePassphrase.get()),str(ePhoneNumber.get()))>=0.3:
        val= False   

    if val:
        return val

def valid_pass(input):
    lbPass_valid = Label(winsu, text='✅ Valid                                                                    \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       '
    ,font=('arial',9))
    lbPass_valid.config(foreground="green")
    lbPass_error = Label(winsu, text='❌ Passphrase is not valid!\nPlease create a passphrase that meets the following conditions:\n- Length from 6 to 20 characters.\n- Includes special characters: \'$\', \'@\', \'#\', \'%\', \' \', \'.\', \'?\', \'_\', \'-\', \'/\', \',\'\n- Uppercase and lowercase letters.\n- Number.\n- Not the same as the information entered above.',font=('arial',10))
    lbPass_error.config(foreground="red")

    if passphrase_format()==TRUE:
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

mailValid = winsu.register(valid_email)
nameValid = winsu.register(valid_name)
dobValid = winsu.register(valid_dob)
phoneValid = winsu.register(valid_phone)
passValid = winsu.register(valid_pass)
    
def success_signup():
    if messagebox.showinfo('Message box',f'You have successfully registered!',icon='info',command=close_winsu):
        #winsu.destroy()
        winsi.mainloop()

def close_winsu():
    winsu.destroy()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

#save data after click register button
def register_click():
    
    salt = uuid.uuid4().hex
    hash_object = hashlib.sha256(salt.encode() + str(ePassphrase.get()).encode('utf-8'))

    data.append({
        'email': eEmail.get(),
        'name': eName.get(),
        'dob': eDOB.get(),
        'phone': ePhoneNumber.get(),
        'address': eAddress.get(),
        'passphrase': hash_object.hexdigest()+':'+salt,
        'Ksecret': ''
    })
    print(data)
    with open(path+'user.txt', 'w') as fout:
        json.dump(data, fout, indent=4, separators=(',',': '))


def showPass():
    if(cShow_v.get()==1):
        ePassphrase.config(show='')
    else:
        ePassphrase.config(show='*')

lbSignup = Label(winsu, text="SIGN UP", font=("arial", 25))
lbSignup.place(x=200, y=40)
lbEmail = Label(winsu, text='Email',font=('arial',15))
lbEmail.place(x = 50,y = 100)
lbName = Label(winsu, text='Full Name',font=('arial',15))
lbName.place(x = 50,y = 150)
lbDOB = Label(winsu, text='Date of birth',font=('arial',15))
lbDOB.place(x = 50,y = 200)
lbPhoneNumber = Label(winsu, text='Phone number',font=('arial',15))
lbPhoneNumber.place(x = 50,y = 250)
lbAddress = Label(winsu, text='Address',font=('arial',15))
lbAddress.place(x = 50,y = 300)
lbPassphrase = Label(winsu, text='Passphrase',font=('arial',15))
lbPassphrase.place(x = 50,y = 350)

email = tk.StringVar()
eEmail = Entry(winsu,width=25,font = ('Arial',15),validate='focusout',textvariable=email,validatecommand=(mailValid,'%P'))
eEmail.place(x= 200, y= 100)

eName = Entry(winsu,width=25,font = ('Arial',15),validate='focusout',validatecommand=(nameValid,'%P'))
eName.place(x= 200, y= 150)

eDOB = DateEntry(winsu,font = ('Arial',15),fieldbackground='light green',background= 'lemonchiffon', 
                foreground= 'dark blue',selectmode='day',maxdate=datetime.today(),
                showweeknumbers=FALSE,selectforeground='red',validate='focusout',validatecommand=(dobValid,'%P'))
eDOB.place(x= 201, y= 200)

ePhoneNumber = Entry(winsu,width=25,font = ('Arial',15),validate='focusout',validatecommand=(phoneValid,'%P'))
ePhoneNumber.place(x= 200, y= 250)

eAddress = Entry(winsu,width=25,font = ('Arial',15),validate='focusout')
eAddress.place(x= 200, y= 300)

ePassphrase = Entry(winsu,width=25,font = ('Arial',15),show='*',validate='focusout',validatecommand=(passValid,'%P'))
ePassphrase.place(x=200, y= 350)

cShow_v = IntVar(value=0)
cShowPass = Checkbutton(winsu,text='Show passphrase',variable=cShow_v,onvalue=1,offvalue=0,command=showPass)
cShowPass.place(x=200, y=380)

btnSignup = Button(winsu,text="REGISTER",state=DISABLED,command=combine_funcs(register_click,success_signup))
btnSignup.place(x=190, y=500)

# Display UI
winsu.mainloop()

