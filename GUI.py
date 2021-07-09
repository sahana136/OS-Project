import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
#main_frame = Frame(root)
#main_frame.pack(fill = BOTH, expand = 1)
#my_canvas = Canvas(main_frame)
#my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

#sb = Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
#sb.pack(side = RIGHT, fill = Y)

#my_canvas.configure(yscrollcommand = sb.set)
#my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#second_frame = Frame(my_canvas)

#my_canvas.create_window((0,0), window=second_frame, anchor="nw")

T = tk.Text(root, height = 52, width = 100, bg="#545454", fg="#ffffff")
T.pack()
#sb.config( command = T.yview )
#root.config(yscrollcommand = sb.set )
var = StringVar()
#L = Label(root, textvariable=var, relief=RAISED, bg="#545454", fg="#ffffff", height=52, width=100)
#L.pack()

root.title('Linux Voice Assistant')

def shortener(text):
    T.insert(END,text)
    #var.set(labels)
    #L = Label(root, textvariable=text)
    #var.set(text)
    #L.pack()
    #labels.append(L)
    root.update_idletasks()
    root.update()