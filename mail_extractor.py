'''
Author: Yashraj Singh Boparai
Date: 09/05/2021 (dd/mm/yyyy)
'''
from tkinter import *
import re

top = Tk()
top.title('Mail Extractor')
top.geometry('300x300')

def OPEN():
    f2=open('tk.txt', 'w')
    f2.write('Put some text below: ')
    f2.close()

def find_mail(str):
    email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
    for i,j in enumerate(email):
        print(f'Mail({i+1}) -----> {j}')

def GET():
    f = open('tk.txt', 'r')
    str1 = f.read()
    find_mail(str1)

st = StringVar()
def SUBMIT():
    str2 = st.get()
    find_mail(str2)

Open = Button(top, text='Open txt file', command=OPEN).place(x=30, y=40)
Get = Button(top, text='Get Mails', command=GET).place(x=200, y=40)

for_text = Label(top, text='Paste text here').place(x=90, y=80)
e1 = Entry(top,textvariable=st).place(x=10, y=100, width= 280, height=150)
Submit = Button(top, text='Submit', command=SUBMIT).place(x=120, y=260)
top.mainloop()
