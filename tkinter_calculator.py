# A very simple calculator written in Python! Used to learn Tk and more of python.

import tkinter as tk
import numpy as np
from numpy import sin as sin
from numpy import cos as cos # Not yet implemented fully but just learning how to rename functions.
from numpy import tan as tan

window = tk.Tk()
window.title("Calculator")
window.geometry("550x200")
window.resizable(False, False) # Easier then having it ajust for now

user_input = tk.StringVar(window) # A variable that stores what is written in .Entry().

def backspace(event=None):
    if window.focus_get() != write:
        oldEntry = user_input.get()
        newText = oldEntry[:-1] # Doesnt take the last char of the string
        user_input.set(newText)
    else:
        pass

def insert(num):
    oldEntry = user_input.get()
    newText = oldEntry + num
    user_input.set(newText)

def insert_keyboard(num):
    # focus_get() - tells the program what widget is selected currently
    # != - If it isn't write, it will work!
    if window.focus_get() != write:
        oldEntry = user_input.get()
        newText = oldEntry + num
        user_input.set(newText) # .set - Sets the text we wrote into Entry
    else:
        pass
    
def calculate(event=None): # event=None - Needed because .bind() sends pressed key data to function, and it's set to None so it doesn't confuse our .button.
    try:
        expression = user_input.get() # .get - Gets what is currently written in .Entry().
        divisionFix = expression.replace(":", "/")
        result = eval(divisionFix)
        txt.config(text=str(result)) # .config - Configures the text.
    except:
        txt.config(text="Err")

# Put frames here

resultWrite = tk.Frame(window, border=50, width=200, height=200, background="red")
resultWrite.pack(side="left")

buttonsInput = tk.Frame(window, border=50, width=200, height=200, background="blue")
buttonsInput.pack(side="right")

# Entry and buttons

write = tk.Entry(resultWrite, textvariable=user_input)
write.grid(row=0)

calc = tk.Button(buttonsInput, text="=", command=calculate)
calc.grid(row=3, column=2)

zero = tk.Button(buttonsInput, text="0", command=lambda:insert("0")) # lambda - Acts as a sheild so that insert isn't already used on start
zero.grid(row=3, column=1)
# lambda - Function that gets read on start and the program realises it isn't supposed to be used yet.
# When we press the button, only then it "unpacks" lambda and does insert

one = tk.Button(buttonsInput, text="1", command=lambda:insert("1"))
one.grid(row=2, column=0)

two = tk.Button(buttonsInput, text="2", command=lambda:insert("2"))
two.grid(row=2, column=1)

three = tk.Button(buttonsInput, text="3", command=lambda:insert("3"))
three.grid(row=2, column=2)

four = tk.Button(buttonsInput, text="4", command=lambda:insert("4"))
four.grid(row=1, column=0)

five = tk.Button(buttonsInput, text="5", command=lambda:insert("5"))
five.grid(row=1, column=1)

six = tk.Button(buttonsInput, text="6", command=lambda:insert("6"))
six.grid(row=1, column=2)

seven = tk.Button(buttonsInput, text="7", command=lambda:insert("7"))
seven.grid(row=0, column=0)

eight = tk.Button(buttonsInput, text="8", command=lambda:insert("8"))
eight.grid(row=0, column=1)

nine = tk.Button(buttonsInput, text="9", command=lambda:insert("9"))
nine.grid(row=0, column=2)

plus = tk.Button(buttonsInput, text="+", command=lambda:insert("+"))
plus.grid(row=0, column=3)

minus = tk.Button(buttonsInput, text="-", command=lambda:insert("-"))
minus.grid(row=1, column=3)

times = tk.Button(buttonsInput, text="*", command=lambda:insert("*"))
times.grid(row=2, column=3)

divided = tk.Button(buttonsInput, text=":", command=lambda:insert(":"))
divided.grid(row=3, column=3)

comma = tk.Button(buttonsInput, text=".", command=lambda:insert("."))
comma.grid(row=3, column=0)

BackSpace = tk.Button(buttonsInput, text="⌫", command=backspace)
BackSpace.grid(row=0, column=4)
# Binds

window.bind("<Return>", calculate) # .bind - binds key to a function.
window.bind("0", lambda event:insert_keyboard("0")) 
# Event needed because Tk needs to send event somewhere, afterwards event is ignored by our function because lambda took the burden
window.bind("1", lambda event:insert_keyboard("1"))
window.bind("2", lambda event:insert_keyboard("2"))
window.bind("3", lambda event:insert_keyboard("3"))
window.bind("4", lambda event:insert_keyboard("4"))
window.bind("5", lambda event:insert_keyboard("5"))
window.bind("6", lambda event:insert_keyboard("6"))
window.bind("7", lambda event:insert_keyboard("7"))
window.bind("8", lambda event:insert_keyboard("8"))
window.bind("9", lambda event:insert_keyboard("9"))
window.bind("+", lambda event:insert_keyboard("+"))
window.bind("-", lambda event:insert_keyboard("-"))
window.bind("*", lambda event:insert_keyboard("*"))
window.bind(":", lambda event:insert_keyboard(":"))
window.bind("/", lambda event:insert_keyboard(":"))
window.bind(".", lambda event:insert_keyboard("."))
window.bind("<BackSpace>", backspace) 
# backspace() - Doesn't work because () makes it work on startup and then does nothing
# Instead we write it without the brackets 

# Labels

empty0 = tk.Label(resultWrite, text="").grid(row=1)
txt = tk.Label(resultWrite, text="", width=20, height=1, background="white")
txt.grid(row=2)

window.mainloop()

# VISUALS NOT DONE, that's why it looks ugly, sorry! At least it works.
