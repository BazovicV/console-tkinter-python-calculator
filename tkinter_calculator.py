# A very simple calculator written in Python! Used to learn Tk and more of python.

import tkinter as tk
import numpy
import sys
import pyperclip
from tkinter import ttk
from numpy import sin as sin
from numpy import cos as cos # Not yet implemented fully but just learning how to rename functions.
from numpy import tan as tan

window = tk.Tk()
window.title("Calculator")

if sys.platform == "win32": # Detecting the OS
    window.geometry("475x200")
else:
    window.geometry("520x200")

window.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TEntry",
    font=("Fixedsys", 11),
    bordercolor="black"
)

style.configure(
    "TButton",
    font=("Fixedsys", 11),
    height=1, 
    width=3, 
    bordercolor="black"
)

style.configure("Blue.TButton", background="lightblue")
style.configure("White.TButton", background="white")
style.configure("Gray.TButton", background="lightgray")
style.configure("Red.TButton", background="tomato")
style.configure("History.TButton", background="white", width=7)
style.configure("Copy.TButton", background="white", width=4)

try:
    logo = tk.PhotoImage(file="calculator.png")
    window.iconphoto(True, logo)
except:
    pass

user_input = tk.StringVar(window) # A variable that stores what is written in .Entry().
output = tk.StringVar(window, "0")
history_list = ["No history"]

def backspace(event=None):
    if window.focus_get() != write:
        oldEntry = user_input.get()
        newText = oldEntry[:-1] # Doesnt take the last char of the string
        user_input.set(newText)
        output.set(0)

def clear_all(event=None):
    user_input.set("")
    output.set("0")

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
    
    operations = ["+", "-", "*", "/"]
    
    try:
        expression = user_input.get() # .get - Gets what is currently written in .Entry().

        if not any((element in expression) for element in operations):
            output.set("Not an expression")

        else:
            result = eval(expression)
            output.set(result)

            if expression in history_list[-1]:
                pass

            else:

                if "No history" in history_list:
                    history_list.clear()
                    history_menu.delete(0)

                if len(history_list) == 10:
                    history_list.pop(0) # pop - Removes by index
                    history_menu.delete(0)

        

                history_list.append(expression)
                history_menu.add_command(label=history_list[-1], command=lambda expression=history_list[-1]: user_input.set(expression)) # lambda creates a function for all our menu items       
        
    except:
        output.set("Error")

def clear_history():
    history_list.clear()
    history_menu.delete(0, "end")     
    history_list.append("No history")
    history_menu.add_command(label=history_list[0])

def copy_history():
    if "No history" in history_list:
        pass
    else:
        history_string = str(history_list)
        for char in "[]'":
            history_string = history_string.replace(char, "")
        pyperclip.copy(history_string)
                       
# Put frames here

resultWrite = tk.Frame(window, border=30, width=200, height=200)
resultWrite.pack(side="left", fill="both", expand=True)

buttonsInput = tk.Frame(window, border=30, width=150, height=200)
buttonsInput.pack(side="right", fill="both", expand=True)

# Put entry and labels here

input_text = tk.Label(resultWrite, text="Input:", font="Fixedsys")
input_text.pack(side="top")

write = ttk.Entry(resultWrite, textvariable=user_input, style="TEntry")
write.pack(side="top", after=input_text)

output_text = tk.Label(resultWrite, text="Result:", font="Fixedsys")
output_text.pack(side="top", after=write)

result = ttk.Entry(resultWrite, textvariable=output, style="TEntry")
result.config(state="readonly")
result.pack(side="top", after=output_text)

# Put buttons here

# ---Numbers---
calc = ttk.Button(buttonsInput, text="=", style="Blue.TButton", command=calculate)
calc.grid(row=3, column=2, padx=2, pady=2)

zero = ttk.Button(buttonsInput, text="0", style="White.TButton", command=lambda:insert("0")) # lambda - Acts as a sheild so that insert isn't already used on start
zero.grid(row=3, column=1, padx=2, pady=2)
# lambda - Function that gets read on start and the program realises it isn't supposed to be used yet.
# When we press the button, only then it "unpacks" lambda and does insert

one = ttk.Button(buttonsInput, text="1", style="White.TButton", command=lambda:insert("1"))
one.grid(row=2, column=0, padx=2, pady=2)

two = ttk.Button(buttonsInput, text="2", style="White.TButton", command=lambda:insert("2"))
two.grid(row=2, column=1, padx=2, pady=2)

three = ttk.Button(buttonsInput, text="3", style="White.TButton", command=lambda:insert("3"))
three.grid(row=2, column=2, padx=2, pady=2)

four = ttk.Button(buttonsInput, text="4", style="White.TButton", command=lambda:insert("4"))
four.grid(row=1, column=0, padx=2, pady=2)

five = ttk.Button(buttonsInput, text="5", style="White.TButton", command=lambda:insert("5"))
five.grid(row=1, column=1, padx=2, pady=2)

six = ttk.Button(buttonsInput, text="6", style="White.TButton", command=lambda:insert("6"))
six.grid(row=1, column=2, padx=2, pady=2)

seven = ttk.Button(buttonsInput, text="7", style="White.TButton", command=lambda:insert("7"))
seven.grid(row=0, column=0, padx=2, pady=2)

eight = ttk.Button(buttonsInput, text="8", style="White.TButton", command=lambda:insert("8"))
eight.grid(row=0, column=1, padx=2, pady=2)

nine = ttk.Button(buttonsInput, text="9", style="White.TButton", command=lambda:insert("9"))
nine.grid(row=0, column=2, padx=2, pady=2)

# Operations
plus = ttk.Button(buttonsInput, text="+", style="Gray.TButton", command=lambda:insert("+"))
plus.grid(row=2, column=3, padx=2, pady=2)

minus = ttk.Button(buttonsInput, text="-", style="Gray.TButton", command=lambda:insert("-"))
minus.grid(row=2, column=4, padx=2, pady=2)

times = ttk.Button(buttonsInput, text="*", style="Gray.TButton", command=lambda:insert("*"))
times.grid(row=3, column=3, padx=2, pady=2)

divided = ttk.Button(buttonsInput, text="/", style="Gray.TButton", command=lambda:insert("/"))
divided.grid(row=3, column=4, padx=2, pady=2)

# ---Other---

comma = ttk.Button(buttonsInput, text=".", style="White.TButton", command=lambda:insert("."))
comma.grid(row=3, column=0, padx=2, pady=2)

open_bracket = ttk.Button(buttonsInput, text="(", style="Gray.TButton", command=lambda:insert("("))
open_bracket.grid(row=1, column=3, padx=2, pady=2)

close_bracket = ttk.Button(buttonsInput, text=")", style="Gray.TButton", command=lambda:insert(")"))
close_bracket.grid(row=1, column=4, padx=2, pady=2)

BackSpace = ttk.Button(buttonsInput, text="CE", style="Red.TButton", command=backspace)
BackSpace.grid(row=0, column=4, padx=2, pady=2)

clear = ttk.Button(buttonsInput, text="C", style="Red.TButton", command=clear_all)
clear.grid(row=0, column=3, padx=2, pady=2)

clear_history_button = ttk.Button(resultWrite, text="CH", style="Red.TButton", command=clear_history)

copy_history_button = ttk.Button(resultWrite, text="Copy", style="Copy.TButton", command=copy_history)


if sys.platform == "win32":
    pass
else:
    clear_history_button.place(x=139, y=115)
    copy_history_button.place(x=83, y=115)

# Put menus here

settings_menu = tk.Menu(window, bg="white")
window.config(menu=settings_menu)

mode_menu = tk.Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(menu=mode_menu, label="Mode")
mode_menu.add_command(label="Simple")
mode_menu.add_command(label="Scientific")
mode_menu.add_command(label="Exchange rates")

window.option_add("*tearOff", False) # Stops tearoffs

history = ttk.Menubutton(resultWrite, text="History", style="History.TButton")
history_menu = tk.Menu(history)
history_menu.add_command(label=history_list[0])
history["menu"] = history_menu # Telling Menubutton to use Menu

if sys.platform == "win32":
    pass
else:
    history.place(x=0, y=115)

# Put binds here

window.bind("<Return>", calculate) # .bind - binds key to a function.

for key in "0123456789+-*/.()":
    window.bind(key, lambda event, k=key:insert_keyboard(k) ) # Making k=key to lock in every key

window.bind("<BackSpace>", backspace) 
# backspace() - Doesn't work because () makes it work on startup and then does nothing
# Instead we write it without the brackets 

window.mainloop()

# Visuals mostly done! And it works fine.
