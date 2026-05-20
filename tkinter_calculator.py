# A very simple calculator written in Python! Used to learn Tk and more of python.

import tkinter as tk
import numpy
from numpy import sin as sin
from numpy import cos as cos # Not yet implemented fully but just learning how to rename functions.
from numpy import tan as tan

window = tk.Tk()
window.title("Calculator")
window.geometry("550x250")
window.resizable(False, False) # Easier than having it adjust for now

logo = tk.PhotoImage(file="calculator.png")
window.iconphoto(True, logo)

user_input = tk.StringVar(window) # A variable that stores what is written in .Entry().
output = tk.StringVar(window, "0")

def backspace(event=None):
    if window.focus_get() != write:
        oldEntry = user_input.get()
        newText = oldEntry[:-1] # Doesnt take the last char of the string
        user_input.set(newText)

def clear_all(event=None):
    user_input.set("")

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
    
def calculate(event=None): # event=None - Needed because .bind() sends pressed key data to function, and it's set to None so it doesn't confuse our .button.
    try:
        expression = user_input.get() # .get - Gets what is currently written in .Entry().
        divisionFix = expression.replace(":", "/")
        result = eval(divisionFix)
        output.set(result) # .config - Configures the text.
    except:
        output.set("Error")

# Put frames here

resultWrite = tk.Frame(window, border=30, width=200, height=200)
resultWrite.pack(side="left")

buttonsInput = tk.Frame(window, border=30, width=150, height=200)
buttonsInput.pack(side="right")

# Put entry and labels here

input_text = tk.Label(resultWrite, text="Input:", font="Fixedsys")
input_text.pack(side="top")

write = tk.Entry(resultWrite, textvariable=user_input, font="Fixedsys", highlightbackground="black",)
write.pack(side="top", after=input_text)

output_text = tk.Label(resultWrite, text="Result:", font="Fixedsys")
output_text.pack(side="top", after=write)

result = tk.Entry(resultWrite, textvariable=output, font="Fixedsys", highlightbackground="black",)
result.config(state="readonly", readonlybackground="white")
result.pack(side="top", after=output_text)

# Put buttons here

# ---Numbers---
calc = tk.Button(buttonsInput, text="=", font="Fixedsys", width=1, height=1, background="lightblue", highlightbackground="black", command=calculate)
calc.grid(row=3, column=2, padx=2, pady=2)

zero = tk.Button(buttonsInput, text="0", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("0")) # lambda - Acts as a sheild so that insert isn't already used on start
zero.grid(row=3, column=1, padx=2, pady=2)
# lambda - Function that gets read on start and the program realises it isn't supposed to be used yet.
# When we press the button, only then it "unpacks" lambda and does insert

one = tk.Button(buttonsInput, text="1", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("1"))
one.grid(row=2, column=0, padx=2, pady=2)

two = tk.Button(buttonsInput, text="2", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("2"))
two.grid(row=2, column=1, padx=2, pady=2)

three = tk.Button(buttonsInput, text="3", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("3"))
three.grid(row=2, column=2, padx=2, pady=2)

four = tk.Button(buttonsInput, text="4", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("4"))
four.grid(row=1, column=0, padx=2, pady=2)

five = tk.Button(buttonsInput, text="5", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("5"))
five.grid(row=1, column=1, padx=2, pady=2)

six = tk.Button(buttonsInput, text="6", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("6"))
six.grid(row=1, column=2, padx=2, pady=2)

seven = tk.Button(buttonsInput, text="7", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("7"))
seven.grid(row=0, column=0, padx=2, pady=2)

eight = tk.Button(buttonsInput, text="8", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("8"))
eight.grid(row=0, column=1, padx=2, pady=2)

nine = tk.Button(buttonsInput, text="9", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("9"))
nine.grid(row=0, column=2, padx=2, pady=2)

# Operations
plus = tk.Button(buttonsInput, text="+", font="Fixedsys", width=1, height=1, background="lightgray", highlightbackground="black", command=lambda:insert("+"))
plus.grid(row=0, column=3, padx=2, pady=2)

minus = tk.Button(buttonsInput, text="-", font="Fixedsys", width=1, height=1, background="lightgray", highlightbackground="black", command=lambda:insert("-"))
minus.grid(row=1, column=3, padx=2, pady=2)

times = tk.Button(buttonsInput, text="*", font="Fixedsys", width=1, height=1, background="lightgray", highlightbackground="black", command=lambda:insert("*"))
times.grid(row=2, column=3, padx=2, pady=2)

divided = tk.Button(buttonsInput, text=":", font="Fixedsys", width=1, height=1, background="lightgray", highlightbackground="black", command=lambda:insert(":"))
divided.grid(row=3, column=3, padx=2, pady=2)

# ---Other---

comma = tk.Button(buttonsInput, text=".", font="Fixedsys", width=1, height=1, background="white", highlightbackground="black", command=lambda:insert("."))
comma.grid(row=3, column=0, padx=2, pady=2)

BackSpace = tk.Button(buttonsInput, text="C", font="Fixedsys", width=1, height=1, background="tomato", highlightbackground="black", command=backspace)
BackSpace.grid(row=1, column=4, padx=2, pady=2)

clear = tk.Button(buttonsInput, text="CE", font="Fixedsys", width=1, height=1, background="tomato", highlightbackground="black", command=clear_all)
clear.grid(row=0, column=4, padx=2, pady=2)

# Put binds here

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

window.mainloop()

# Visuals mostly done! And it works fine.
