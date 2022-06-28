from argparse import FileType
from cgitb import text
from datetime import datetime
from select import select
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import json
import tkinter as tk
import re
import hashlib
from tokenize import String
import uuid
from numpy import empty
from tkcalendar import DateEntry
from difflib import SequenceMatcher
import datetime as dt
import os
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
import binascii
from tkinter import messagebox
import base64

#path = '/Users/anhquantran/Documents/GitHub/App/'
path = ''
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_name = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"

data_file = open('user.txt').read()

data = json.loads(data_file)

#DO MANY FUNCTIONS
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

#SIGN IN
def openSignin():
    # Create UI for Sign in screen
    winsi = tk.Tk()
    winsi.geometry("500x300")
    winsi.title("Mã hóa")

    #SIGN IN screen
    users = {}
    users['user'] = []

    class User(object):
        def __init__(self, email, passphrase):
            self.email = email
            self.passphrase = passphrase

    def object_decoder(obj):
        #print(obj['email'] + obj['email'])
        if 'email' in obj and 'passphrase' in obj:
            users['user'].append(User(obj['name'], obj['passphrase'])) 

    def valid_signin_email(input):
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
        for i in data:
            if (i["email"] == SIemail.get()) & check_password(i['passphrase'],SIpassphrase.get()):
                siEmail = i["email"]
                success_signin()
                winsi.destroy()
                openMenu()
                break
            else:
                SInotification.set("Not Right Password or Email")
        
    def success_signin():
        messagebox.showinfo('Sign in', 'You have successfully sign in!')
        

    def showPassIn():
        if(cShow_vin.get()==1):
            eSIpassphrase.config(show='')
        else:
            eSIpassphrase.config(show='*')

    mailValid = winsi.register(valid_signin_email)
    global SIemail
    SIemail = tk.StringVar()
    SIpassphrase = tk.StringVar()
    SInotification = tk.StringVar()

    # Body
    lbSignin = Label(winsi, text="SIGN IN", font=("arial", 25))
    lbSignin.place(x=200, y=40)
    lbSIEmail = Label(winsi, text='Email:',font=('arial',15))
    lbSIEmail.place(x = 50,y = 100)
    lbSIpassphrase = Label(winsi, text='Passphrase:',font=('arial',15))
    lbSIpassphrase.place(x = 50,y = 150)

    lbSINotification = Label(winsi,font=('arial',10),textvariable=SInotification)
    lbSINotification.place(x = 200,y = 200)

    eSIEmail = Entry(winsi,width=25,font = ('Arial',15),textvariable=SIemail,validate='focusout',validatecommand=(mailValid,'%P'))
    eSIEmail.place(x= 200, y= 100)
    eSIpassphrase = Entry(winsi,width=25,font = ('Arial',15),textvariable=SIpassphrase,show='*')
    eSIpassphrase.place(x= 200, y= 150)

    cShow_vin = IntVar(value=0)
    cShowPass = Checkbutton(winsi,text='Show passphrase',variable=cShow_vin,onvalue=1,offvalue=0,command=showPassIn)
    cShowPass.place(x=200, y=180)

    btnSignin = Button(winsi, text="LOGIN",state=DISABLED,command=checkAccount)
    btnSignin.place(x=210, y=220)

    bGoSignup = Button(winsi,text='SIGN UP',command=combine_funcs(winsi.destroy,openSignup))
    bGoSignup.place(x=400,y=10)

    winsi.mainloop()

#SIGN UP
def openSignup():

    # Create UI for Sign up screen
    winsu = tk.Tk()
    winsu.geometry("500x600")
    winsu.title("Mã hóa")

    #get the probability of a string being similar to another string
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    #load json file and store user's keys into dataKey

    with open('userkeys.txt') as fkin:
        dataKey = json.load(fkin)

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
            lbName_valid.pack(padx=201,pady=180,fill='both')
            btnSignup.config(state='active')  
            return True        
        else:
            lbName_valid.destroy()
            lbName_error.pack(padx=201,pady=180,fill='both')
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
        lbPhone_valid = Label(winsu, text='✅ Valid                                                                      ',font=('arial',9))
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
        })

        dataKey.append({
            'email': eEmail.get(),
            'kprivate': '',
            'kpublic': '',
            'ksecret': '',
            'ksession': ''
        })

        with open('user.txt', 'w') as fout:
            json.dump(data, fout, indent=4, separators=(',',': '))

        with open('userkeys.txt','w') as fk:
            json.dump(dataKey, fk, indent=4, separators=(',',': '))

        success_signup()
        winsu.destroy()
        openSignin()

    def success_signup():
        messagebox.showinfo('Sign up', 'You have successfully registered!')

    #show or hide password
    def showPass():
        if(cShow_v.get()==1):
            ePassphrase.config(show='')
        else:
            ePassphrase.config(show='*')

    #Label for Sign up
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

    mailValid = winsu.register(valid_email)
    nameValid = winsu.register(valid_name)
    dobValid = winsu.register(valid_dob)
    phoneValid = winsu.register(valid_phone)
    passValid = winsu.register(valid_pass)

    #Entry for Sign up
    email = tk.StringVar()
    eEmail = Entry(winsu,width=25,font = ('Arial',15),validate='focusout',textvariable=email,validatecommand=(mailValid,'%P'))
    eEmail.place(x= 200, y= 100)

    eName = Entry(winsu,width=25,font = ('Arial',15),validate='focusout',validatecommand=(nameValid,'%P'))
    eName.place(x= 200, y= 150)

    eDOB = DateEntry(winsu,font = ('Arial',15),fieldbackground='light green',background= 'lemonchiffon', 
                    foreground= 'dark blue',selectmode='day',maxdate=datetime.today(),date_pattern='dd/mm/yyyy',
                    showweeknumbers=FALSE,selectforeground='red',validate='focusout',validatecommand=(dobValid,'%P'))
    eDOB.place(x= 201, y= 200)

    ePhoneNumber = Entry(winsu,width=25,font = ('Arial',15),validate='focusout',validatecommand=(phoneValid,'%P'))
    ePhoneNumber.place(x= 200, y= 250)

    eAddress = Entry(winsu,width=25,font = ('Arial',15))
    eAddress.place(x= 200, y= 300)

    ePassphrase = Entry(winsu,width=25,font = ('Arial',15),show='*',validate='focusout',validatecommand=(passValid,'%P'))
    ePassphrase.place(x=200, y= 350)

    cShow_v = IntVar(value=0)
    cShowPass = Checkbutton(winsu,text='Show passphrase',variable=cShow_v,onvalue=1,offvalue=0,command=showPass)
    cShowPass.place(x=200, y=380)

    btnSignup = Button(winsu,text="REGISTER",state=DISABLED,command=combine_funcs(register_click))
    btnSignup.place(x=190, y=500)

    bGoSignin = Button(winsu,text='SIGN IN',command=combine_funcs(winsu.destroy,openSignin))
    bGoSignin.place(x=400,y=10)

    winsu.mainloop()

#MENU
def openMenu():
    winM = tk.Tk()
    winM.geometry("700x800")
    winM.title("Mã hóa")

    def logout():
        SIemail.set('')

    # for i in data:
    #         if (i["email"] == SIemail.get()):
    #             lbWelcome = Label(winM, text="\nHi, "+i["name"]+"!  ",anchor=E).pack(fill='both')
    #             break

    bLogout = tk.Button(winM, text='Log out',command=combine_funcs(logout,winM.destroy,openSignin))
    bLogout.place(x=610,y=35)

    lbMenu = Label(winM, text="MENU", font=("arial", 25))
    lbMenu.place(x=310, y=80)

    bEdit = tk.Button(winM, font = ('Arial',18),text='Edit information',command=combine_funcs(winM.destroy,openConfirmPass),height=4,width=20)
    bEdit.place(x=50, y=150)

    bGenKey = tk.Button(winM, font = ('Arial',18),text='Generate RSA keys',command=combine_funcs(winM.destroy,openGenerateKey),height=4,width=20)
    bGenKey.place(x=50, y=300)

    bEncodeFile = tk.Button(winM, font = ('Arial',18),text='Encode file',command=combine_funcs(winM.destroy,openEncodeFile),height=4,width=20)
    bEncodeFile.place(x=50, y=450)

    bDecodeFile = tk.Button(winM, font = ('Arial',18),text='Decode file',command=combine_funcs(winM.destroy,openDecodeFile),height=4,width=20)
    bDecodeFile.place(x=390, y=150)

    bSignFile = tk.Button(winM, font = ('Arial',18),text='Sign file',command=combine_funcs(winM.destroy,openSignFile),height=4,width=20)
    bSignFile.place(x=390, y=300)

    bConfirmSignFile = tk.Button(winM, font = ('Arial',18),text='Sign file',command=combine_funcs(winM.destroy,openConfirmSignFile),height=4,width=20)
    bConfirmSignFile.place(x=390, y=450)

    bSendFile = tk.Button(winM, font = ('Arial',18),text='Send File',command=combine_funcs(winM.destroy,openSendFile),height=4,width=20)
    bSendFile.place(x=390, y=600)

    bDownFile = tk.Button(winM, font = ('Arial',18),text='List Download File',command=combine_funcs(winM.destroy,openListFile),height=4,width=20)
    bDownFile.place(x=50, y=600)
    winM.mainloop()


def openSendFile():
    winEd = tk.Tk()
    winEd.geometry("700x800")
    winEd.title("Mã hóa")

    def openFolder():
        global filename
        filename = 'imgError.png'
        filename =  filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(('file_type','*.txt'),('all files','.*')))
        filename = filedialog.askopenfilename(multiple=True)
        print(filename)
    def sender():
        file = open(filename,'rb')
        file_data = file.read(4098)
        filename1 = "DB/" +filename.split('/')[-1]
        f = open(filename1, "wb")
        f.write(file_data)
        f.close()
        file.close()

    lbTitle = Label(winEd, text="SEND FILE", font=('arial', 20))
    lbTitle.place(x=250, y=70)

    bGoSignup = Button(winEd,text='BACK',command=combine_funcs(winEd.destroy,openMenu))
    bGoSignup.place(x=20,y=10)

    bChooseFile = Button(winEd,text='Choose File',command=openFolder)
    bChooseFile.place(x=250,y=150)

    bSend = Button(winEd,text='Send',command=sender)
    bSend.place(x=250,y=500)


def openListFile():
    winEd = tk.Tk()
    winEd.geometry("700x800")
    winEd.title("Mã hóa")

    listbox = Listbox(winEd,fg='blue')
    listbox.pack(pady=15)

    for i in os.listdir(path+'DB'):
        listbox.insert(0,i)

    def selectFile():
        my_lbl.config(text=listbox.get(ANCHOR))
    def saveFile():
        file = filedialog.asksaveasfile(defaultextension='.txt',
                                        filetypes=[
                                            ("Text file",".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*"),
                                        ])
        if file is None:
            return

        f = open(filename,'rb')
        file_data = f.read(4098)
        # filetext = str(text.get(1.0,END))
        #filetext = input("Enter some text I guess: ") //use this if you want to use console window
        file.write(file_data)
        f.close()
        file.close()
        

    button = Button(text='save',command=saveFile)
    button.pack()


    bSelect = Button(winEd,text='Select',command=selectFile)
    bSelect.pack(pady=10)

    global my_lbl
    my_lbl = Label(winEd,text='a')
    my_lbl.pack(pady=5)

    
#EDIT INFORMATION
def openEditInfo():
    winEd = tk.Tk()
    winEd.geometry("700x800")
    winEd.title("Mã hóa")

    lbTitle = Label(winEd, text="EDIT INFORMATION", font=('arial', 20))
    lbTitle.place(x=250, y=70)

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def valid_name(input):
        lbName_valid = Label(winEd, text='✅ Valid                                                                    ',font=('arial',9))
        lbName_valid.config(foreground="green")
        lbName_error = Label(winEd, text='❌ Name is not valid! Please try again',font=('arial',9))
        lbName_error.config(foreground="red")
        if(re.search(regex_name,input) and input.isalpha and len(input)<50):
            lbName_error.destroy()
            lbName_valid.pack(padx=301,pady=230,fill='both')
            btnSignup.config(state='active')  
            return True        
        else:
            lbName_valid.destroy()
            lbName_error.pack(padx=301,pady=230,fill='both')
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

        lbDOB_valid = Label(winEd, text='✅ Valid                                                                    ',font=('arial',9))
        lbDOB_valid.config(foreground="green")
        lbDOB_error = Label(winEd, text='❌ Date of birth is not valid! Please try again',font=('arial',10))
        lbDOB_error.config(foreground="red")
        
        if(isValidDate):
            lbDOB_error.destroy()
            lbDOB_valid.place(x=301,y=280)
            btnSignup.config(state='active')  
            return True        
        else:
            lbDOB_valid.destroy()
            lbDOB_error.place(x=301,y=280)
            btnSignup.config(state='disabled')  
            return False 

    def valid_phone(input):
        lbPhone_valid = Label(winEd, text='✅ Valid                                                                      ',font=('arial',9))
        lbPhone_valid.config(foreground="green")
        lbPhone_error = Label(winEd, text='❌ Phone number is not valid! Please try again',font=('arial',10))
        lbPhone_error.config(foreground="red")
        
        # Entry with 10 numbers is ok
        if len(input) == 10 and input.isnumeric(): 
            lbPhone_error.grid_remove()
            lbPhone_valid.place(x = 301,y = 330)
            btnSignup.config(state='active')
            return True
        # Anything else, reject it
        else:
            lbPhone_valid.grid_remove()
            lbPhone_error.place(x = 301,y = 330) 
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

        if str(ePassphrase.get())=="":
            val=True 

        if val:
            return val

    def valid_pass(input):
        lbPass_valid = Label(winEd, text='✅ Valid                                                                    \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       '
        ,font=('arial',9))
        lbPass_valid.config(foreground="green")
        lbPass_error = Label(winEd, text='❌ Passphrase is not valid!\nPlease create a passphrase that meets the following conditions:\n- Length from 6 to 20 characters.\n- Includes special characters: \'$\', \'@\', \'#\', \'%\', \' \', \'.\', \'?\', \'_\', \'-\', \'/\', \',\'\n- Uppercase and lowercase letters.\n- Number.\n- Not the same as the information entered above.',font=('arial',10))
        lbPass_error.config(foreground="red")
        lbPass_empty = Label(winEd, text='                                                                            \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       \n                                                                                                                       '
        ,font=('arial',9))

        if passphrase_format()==TRUE:
            lbPass_error.destroy()
            lbPass_valid.place(x = 301,y = 450)
            btnSignup.config(state='active')
            return True

        #If user do not change passphrase
        elif passphrase_format()==FALSE & ePassphrase.get()=='':
            lbPass_empty.place(x = 301,y = 450)
            btnSignup.config(state='active')
            return True

        # Anything else, reject it
        else:
            lbPass_valid.destroy()
            lbPass_error.place(x = 301,y = 450) 
            btnSignup.config(state='disabled')
            return False

    #save data after click register button
    def edit_click():
        salt = uuid.uuid4().hex
        hash_object = hashlib.sha256(salt.encode() + str(ePassphrase.get()).encode('utf-8'))

        for i in data:
            if (i["email"] == SIemail.get()):
                i["name"] = eName.get()
                i["dob"] = eDOB.get()
                i["phone"] = ePhoneNumber.get()
                i["address"] = eAddress.get()
                if(ePassphrase.get()!=''):
                    i["passphrase"] = hash_object.hexdigest()+':'+salt

        with open('user.txt', 'w') as fout:
            json.dump(data, fout, indent=4, separators=(',',': '))
        
        fout.close()
        success_edit()

    def success_edit():
        messagebox.showinfo('EDIT INFORMATION', 'You have successfully edited!')

    #show or hide password
    def showPass():
        if(cShow_v.get()==1):
            ePassphrase.config(show='')
        else:
            ePassphrase.config(show='*')

    #Label for Edit info
    
    lbEmail = Label(winEd, text='Email',font=('arial',15))
    lbEmail.place(x = 150,y = 150)
    lbName = Label(winEd, text='Full Name',font=('arial',15))
    lbName.place(x = 150,y = 200)
    lbDOB = Label(winEd, text='Date of birth',font=('arial',15))
    lbDOB.place(x = 150,y = 250)
    lbPhoneNumber = Label(winEd, text='Phone number',font=('arial',15))
    lbPhoneNumber.place(x = 150,y = 300)
    lbAddress = Label(winEd, text='Address',font=('arial',15))
    lbAddress.place(x = 150,y = 350)
    lbPassphrase = Label(winEd, text='Passphrase',font=('arial',15))
    lbPassphrase.place(x = 150,y = 400)

    nameValid = winEd.register(valid_name)
    dobValid = winEd.register(valid_dob)
    phoneValid = winEd.register(valid_phone)
    passValid = winEd.register(valid_pass)

    for i in data:
            if(i['email']==str(SIemail.get())): 
                sEmail = i['email']
                sName = i["name"]
                sDOB = i["dob"]
                sPhone = i["phone"]
                sAdd = i["address"]
                break
    
    dob = sDOB.split('/')
    dd = int(dob[0])
    mm = int(dob[1])
    yyyy = int(dob[2])

    #Entry for Edit Info
    eEmail = Entry(winEd,width=25,font = ('Arial',15))
    eEmail.insert(0,sEmail)
    eEmail.config(state=DISABLED)
    eEmail.place(x= 300, y= 150)

    eName = Entry(winEd,width=25,font = ('Arial',15),validate='focusout',validatecommand=(nameValid,'%P'))
    eName.insert(0,sName)
    eName.place(x= 300, y= 200)

    eDOB = DateEntry(winEd,font = ('Arial',15),fieldbackground='light green',background= 'lemonchiffon', 
                    foreground= 'dark blue',selectmode='day',maxdate=datetime.today(),date_pattern='dd/mm/yyyy',
                    showweeknumbers=FALSE,selectforeground='red',validate='focusout',validatecommand=(dobValid,'%P'),
                    year=yyyy,month=mm,day=dd)
    
    eDOB.place(x= 301, y= 250)

    ePhoneNumber = Entry(winEd,width=25,font = ('Arial',15),validate='focusout',validatecommand=(phoneValid,'%P'))
    ePhoneNumber.insert(0,sPhone)
    ePhoneNumber.place(x= 300, y= 300)

    eAddress = Entry(winEd,width=25,font = ('Arial',15))
    eAddress.insert(0,sAdd)
    eAddress.place(x= 300, y= 350)

    ePassphrase = Entry(winEd,width=25,font = ('Arial',15),show='*',validate='focusout',validatecommand=(passValid,'%P'))
    ePassphrase.place(x=300, y= 400)

    cShow_v = IntVar(value=0)
    cShowPass = Checkbutton(winEd,text='Show passphrase',variable=cShow_v,onvalue=1,offvalue=0,command=showPass)
    cShowPass.place(x=300, y=430)

    btnSignup = Button(winEd,text="SAVE",state=DISABLED,command=combine_funcs(edit_click))
    btnSignup.place(x=230, y=600)

    btnBack = Button(winEd, text = 'BACK',command=combine_funcs(winEd.destroy,openMenu))
    btnBack.place(x=380, y=600)


def openGenerateKey():
    random_generator = Random.new().read
    key = RSA.generate(2048,random_generator)
    privkey, pubkey = key, key.public_key()
    privkeyPEM, pubkeyPEM = privkey.exportKey().decode('ascii'), pubkey.exportKey().decode('ascii')

    winGen = tk.Tk()
    winGen.geometry("700x700")
    winGen.title("Mã hóa")

    lbTitle = Label(winGen, text="ENCRYPT", font=('arial', 20))
    lbTitle.place(x=300, y=50)
    lbPub = Label(winGen, text="Public key", font=('arial', 15))
    lbPub.place(x=50, y=100)
    lbPriv = Label(winGen, text="Private key", font=('arial', 15))
    lbPriv.place(x=50, y=350)

    def GererateKey():
        btnGetKey.config(state=DISABLED)
        ePub.insert(END,pubkeyPEM)
        ePub.config(state=DISABLED)
        ePriv.insert(END,privkeyPEM)
        ePriv.config(state=DISABLED)  
        for i in dataKey:
            if (i["email"] == SIemail.get()):
                i["kprivate"] = str(privkeyPEM)
                i["kpublic"] = str(pubkeyPEM)
                break

        with open('userkeys.txt', 'w') as fout:
            json.dump(dataKey, fout, indent=4, separators=(',',': '))
        
        fout.close()
    
    def successGen():
        messagebox.showinfo('GENERATE KEYS', 'Your keys have been saved!')

    with open('userkeys.txt') as fkin:
        dataKey = json.load(fkin)
    with open('userkeys.txt','w') as fk:
        json.dump(dataKey, fk, indent=4, separators=(',',': '))

    ePub = Text(winGen,font = ('Arial',15), width=40)
    ePub.place(x=180, y=100,width=450, height=200)

    ePriv = Text(winGen,font = ('Arial',15), width=40)
    ePriv.place(x=180, y=350,width=450, height=200)

    btnGetKey = Button(master = winGen,text = 'GERERATE KEY',command=combine_funcs(GererateKey,successGen))
    btnGetKey.place(x=400, y=600)

    btnBack = Button(winGen, text = 'BACK',command=combine_funcs(winGen.destroy,openMenu))
    btnBack.place(x=200, y=600)

    for i in dataKey:
        if (i["email"] == SIemail.get()):
            if(i["kprivate"] != "" or i["kpublic"] != ""):
                ePub.insert(END,i["kpublic"])
                ePub.config(state=DISABLED)
                ePriv.insert(END,i["kprivate"])
                ePriv.config(state=DISABLED)
                btnGetKey.config(state=DISABLED)
            break

    winGen.mainloop()

def openConfirmPass():
    winCon = tk.Tk()
    winCon.geometry("500x300")
    winCon.title("Mã hóa")

    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def showPassIn():
        if(cShow_vin.get()==1):
            eSIpassphrase.config(show='')
        else:
            eSIpassphrase.config(show='*')

    def checkAccount():
        for i in data:
            print(i["email"])
            # if ((i["email"] == SIemail.get()) & check_password(i['passphrase'],passphrase.get())==FALSE):
            #     messagebox.showinfo('Edit information','Your passphrase is not valid!\nPlease try again!')
            #     break
            if (i["email"] == SIemail.get()) & check_password(i['passphrase'],passphrase.get()):
                print(i["email"])
                messagebox.showinfo('Edit information','Your passphrase is correct!')
                winCon.destroy()
                openEditInfo()
                break
            else:
                noti.set("Your passphrase is incorrect!")
            
    passphrase = tk.StringVar()
    noti = tk.StringVar()

    lbConfirm = Label(winCon, text='Please enter your passphrase before editing:',font=('arial',15))
    lbConfirm.place(x = 50,y = 60)

    lbSIpassphrase = Label(winCon, text='Passphrase:',font=('arial',15))
    lbSIpassphrase.place(x = 50,y = 110)

    eSIpassphrase = Entry(winCon,width=25,font = ('Arial',15),textvariable=passphrase,show='*')
    eSIpassphrase.place(x= 200, y= 110)

    cShow_vin = IntVar(value=0)
    cShowPass = Checkbutton(winCon,text='Show passphrase',variable=cShow_vin,onvalue=1,offvalue=0,command=showPassIn)
    cShowPass.place(x=200, y=140)

    lbNotification = Label(winCon,font=('arial',10),textvariable=noti)
    lbNotification.place(x = 200,y = 160)
    lbNotification.config(foreground="red")

    btnSignin = Button(winCon, text="CONFIRM",command=checkAccount)
    btnSignin.place(x=210, y=220)

    bGoSignup = Button(winCon,text='BACK',command=combine_funcs(winCon.destroy,openMenu))
    bGoSignup.place(x=20,y=10)

def openEncodeFile():
    pass
def openDecodeFile():
    pass
def openSignFile():
    pass
def openConfirmSignFile():
    pass

if __name__ == "__main__":

    openSignup()
    #openMenu()

    #openGenerateKey()
    #del data
    




