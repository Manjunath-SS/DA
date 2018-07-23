import tkinter as tk
from tkinter import *



myDisp=''

r = tk.Tk()
r.title('Simple Calculator')

v = StringVar()
w=Label(r,textvariable=v).grid(row=0,columnspan=5)
v.set("Enter expression using GUI")

def myPress(x):
    global myDisp
    myDisp=myDisp+x
    v.set(myDisp)

def myRes():
    global myDisp
    try:
        myDisp=str(eval(myDisp))
        v.set(myDisp)
    except:
        v.set("Invalid Expression Entered")

def myClr():
    global myDisp
    myDisp=''
    v.set(myDisp)

def myDel():
    global myDisp
    try:
        myDisp=myDisp[:-1]
    except:
        myDisp=''
    v.set(myDisp)


button1 = tk.Button(r, text='1', width=6, command=lambda:myPress('1')).grid(row=2,column=1)
button2 = tk.Button(r, text='2', width=6, command=lambda:myPress('2')).grid(row=2,column=2)
button3 = tk.Button(r, text='3', width=6, command=lambda:myPress('3')).grid(row=2,column=3)

button4 = tk.Button(r, text='4', width=6, command=lambda:myPress('4')).grid(row=4,column=1)
button5 = tk.Button(r, text='5', width=6, command=lambda:myPress('5')).grid(row=4,column=2)
button6 = tk.Button(r, text='6', width=6, command=lambda:myPress('6')).grid(row=4,column=3)

button7 = tk.Button(r, text='7', width=6, command=lambda:myPress('7')).grid(row=6,column=1)
button8 = tk.Button(r, text='8', width=6, command=lambda:myPress('8')).grid(row=6,column=2)
button9 = tk.Button(r, text='9', width=6, command=lambda:myPress('9')).grid(row=6,column=3)

button0 = tk.Button(r, text='0', width=6, command=lambda:myPress('0')).grid(row=8,column=1)
buttonD = tk.Button(r, text='.', width=6, command=lambda:myPress('.')).grid(row=8,column=2)
buttonE = tk.Button(r, text='Compute', width=6, command=myRes, fg='green').grid(row=8,column=3,rowspan=2)

buttonC = tk.Button(r,text='Clear', width=6, command=myClr, fg='red').grid(row=10,column=1)

buttonS = tk.Button(r, text='[', width=6, command=lambda:myPress('[')).grid(row=2,column=4)
buttonR = tk.Button(r, text=']', width=6, command=lambda:myPress(']')).grid(row=2,column=5)
buttonF = tk.Button(r, text='(', width=6, command=lambda:myPress('(')).grid(row=4,column=4)
buttonF = tk.Button(r, text=')', width=6, command=lambda:myPress(')')).grid(row=4,column=5)
buttonF = tk.Button(r, text='{', width=6, command=lambda:myPress('{')).grid(row=6,column=4)
buttonF = tk.Button(r, text='}', width=6, command=lambda:myPress('}')).grid(row=6,column=5)

buttonO1 = tk.Button(r, text='+', width=6, command=lambda:myPress('+')).grid(row=8,column=4)
buttonO2 = tk.Button(r, text='-', width=6, command=lambda:myPress('-')).grid(row=8,column=5)
buttonO3 = tk.Button(r, text='/', width=6, command=lambda:myPress('/')).grid(row=10,column=4)
buttonO4 = tk.Button(r, text='*', width=6, command=lambda:myPress('*')).grid(row=10,column=5)

buttonBk = tk.Button(r, text='Del', width=6, command=myDel, fg='gray').grid(row=10,column=2)


r.mainloop()