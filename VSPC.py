# A very simple calculator written in Python! Used to learn Tk and more of python.

import tkinter as tk
import numpy as np
from numpy import sin as sin
from numpy import cos as cos # Not yet implemented fully but just learning how to rename functions.
from numpy import tan as tan

window = tk.Tk()
window.title("Calculator")
window.geometry("400x200")

user_input = tk.StringVar(window) # A variable that stores what is written in .Entry().

def calculate(event=None): # event=None - Needed because .bind() sends pressed key data to function, and it's set to None so it doesn't confuse our .button.
    try:
        expression = user_input.get() # .get - gets what is currently written in .Entry().
        result = eval(expression)
        txt.config(text="Result: " + str(result)) # .config - configures the text.
    except:
        txt.config(text="Err")

resultWrite = tk.Frame(window, border=50, width=200, height=200, background="red")
resultWrite.pack(side="left")

write = tk.Entry(resultWrite, textvariable=user_input).grid(row=0)

button= tk.Button(window, text="Calculate", command=calculate)
window.bind("<Return>", calculate) # .bind - binds key to a function.
button.pack() 

empty0 = tk.Label(resultWrite, text="").grid(row=1)
txt = tk.Label(resultWrite, text="")
txt.grid(row=2)

window.mainloop()

# VISUALS NOT DONE, that's why it looks ugly, sorry! At least it works.
