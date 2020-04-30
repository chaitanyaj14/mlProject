# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:55:54 2020

@author: Chaitanya
"""

from tkinter import *
from FaceRecognitionAtd.userData import *

root = Tk()


def saveData():
    global entry1
    global entry2
    global entry3
    name = entry1.get()
    sccode = entry2.get()
    branch = entry3.get()
    add_user(name, sccode, branch)
    print(name, sccode, branch)


root.minsize(800, 400)
root.title("User Data")
root.configure(background='light grey')

root.grid_columnconfigure(0, minsize=20)
root.grid_columnconfigure(1, minsize=30)
root.grid_columnconfigure(3, minsize=75)
root.grid_columnconfigure(4, minsize=105)
root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(4, minsize=50)
root.grid_rowconfigure(6, minsize=50)

label_1 = Label(root, text="Enter Your Name :", font=(None, 15))
label_1.grid(row=1, column=2, sticky=W)

entry1 = Entry(root, width=30)
entry1.grid(row=1, column=4, sticky=W)

label_2 = Label(root, text="Enter Your SC Code :", font=(None, 15))
label_2.grid(row=3, column=2, sticky=W)

entry2 = Entry(root, width=30)
entry2.grid(row=3, column=4, sticky=W)

label_3 = Label(root, text="Enter Your Branch :", font=(None, 15))
label_3.grid(row=5, column=2, sticky=W)

entry3 = Entry(root, width=30)
entry3.grid(row=5, column=4, sticky=W)

button = Button(root, text='Enter', command=saveData, width=10, font=(None, 15))
button.grid(row=9, column=3, sticky=W)

root.mainloop()
