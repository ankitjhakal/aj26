import xlwt
import time
import xlutils
from xlutils.copy import copy
import xlrd
import smtplib
import datetime
import random
from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import pygame,webbrowser

def enterpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
   
   wb=xlwt.Workbook()
   ws1=wb.add_sheet('sheet1',cell_overwrite_ok=True) 
   wbr=xlrd.open_workbook("createemail.xls")
   wbr1=wbr.sheet_by_index(0)
   wb=xlutils.copy.copy(wbr)
   ws1=wb.get_sheet("sheet1")
   sheets=wbr.sheets()
   lrow=sheets[0].nrows
   while(1):   
       text=e1.get()
       text1=e2.get()
       count=0
       print(text,text1)
       for i in range (0,lrow):
            if(wbr1.cell_value(i,1)==text and wbr1.cell_value(i,2)==text1):
                  count+=1
                  print(count)
                  destroy()
                  break   
       if(count==0):   
            print(count)     
            global error
            try:
                error
                   
            except NameError:
                error=Label(root,text="couldn't find your account and id",fg="black",bg="red")
                error.place(x=290,y=80)
              
            else:
                error.destroy()
                error=Label(root,text="couldn't find your account and id",fg="black",bg="red")
                error.place(x=290,y=80)                
            break
       else:
            Label(root, text='successfully login',fg="black",bg="white").place(x=20,y=140)
            break
         
def destroy():
         error.destroy()
   


root = Tk()
root.title('gmail sign in')
root.geometry('500x500')
Label(root, text='Google',fg="red",bg="white",).place(x=20,y=20)
Label(root, text='Sign in',fg="black",bg="white").place(x=20,y=40)
Label(root, text='with your Google Account',fg="black",bg="white").place(x=20,y=60)
Label(root, text='email or phone',fg="blue").place(x=20,y=80)
Label(root, text='password',fg="blue").place(x=20,y=100)
button2=Button(root,text="submit",command=enterpress)
button2.place(x=20,y=120)
e1 = Entry(root)
e2 = Entry(root)
e1.place(x=120,y=80)
e2.place(x=120,y=100)
root.mainloop()

'''






# in the text entry box
def press():
    global expression
    expression = expression + str(num)
    equation.set(expression)
 

'''

