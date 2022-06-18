from Signup import *
from Signin import email
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

# with open('user.txt') as fin:
#     data = json.load(fin)
print('hehe: '+str(email.get()))

winei = tk.Tk()
winei.geometry("500x600")
winei.title("Mã hóa")
mailValid = winei.register(valid_email)
nameValid = winei.register(valid_name)
dobValid = winei.register(valid_dob)
phoneValid = winei.register(valid_phone)
passValid = winei.register(valid_pass)


