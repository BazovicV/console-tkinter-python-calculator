import tkinter as tk
from tkinter import ttk
from simpleeval import SimpleEval

class CalculatorBody(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculator")
        self.geometry("520x200")
        self.resizable(False, False)
        self.option_add("*tearOff", False)

        self.inserted_number = tk.StringVar(self, "")
        self.output_number = tk.StringVar(self, "")

        self.evaluator = SimpleEval()

        try:
            self.logo = tk.PhotoImage(file="calculator.png")
            self.iconphoto(True, self.logo)
        except tk.TclError:
            pass

        self.simple_calculator_buttons = SimpleModeButtons(self) # Sends self to parent
        self.simple_calculator_buttons.pack(side="right", fill="both")

        self.display = Display(self)
        self.display.pack(side="left", fill="both")

        self.bind("<Return>", self.calculate) # .bind - binds key to a function.

        for key in "0123456789+-*/.()":
            self.bind(key, lambda event, k=key:self.input_binds(k) ) # Making k=key to lock in every key

        self.bind("<BackSpace>", self.backspace)

    def calculate(self, event=None):
        expression = self.inserted_number.get()
        try:
            self.result = self.evaluator.eval(expression)
            self.output_number.set(f"{self.result:,.15g}")
        except:
            self.output_number.set("Not an expression")

    def backspace(self, event=None):
        if event == None or self.focus_get() != self.display.inserted_number_entry:
            old_entry = self.inserted_number.get()
            new_entry = old_entry[:-1]
            self.inserted_number.set(new_entry)

    def input_symbol(self, symbol):
        old_entry = self.inserted_number.get()
        new_entry = old_entry + symbol
        self.inserted_number.set(new_entry)

    def input_binds(self, k):
        if self.focus_get() != self.display.inserted_number_entry:
            old_entry = self.inserted_number.get()
            new_entry = old_entry + k
            self.inserted_number.set(new_entry)

class Display(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.text_before_input = tk.Label(self, text="Input:")
        self.text_before_input.pack()

        self.inserted_number_entry = tk.Entry(self, textvariable=parent.inserted_number)
        self.inserted_number_entry.pack()

        self.text_before_output = tk.Label(self, text="Output:")
        self.text_before_output.pack()

        self.output_number_entry = tk.Entry(self, textvariable=parent.output_number)
        self.output_number_entry.config(state="readonly")
        self.output_number_entry.pack()

class SimpleModeButtons(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent # So it remember what is the parent

        self.button_list = [ # Nested list
            ["7", "8", "9", "C", "CE"],
            ["4", "5", "6", "(", ")"],
            ["1", "2", "3", "+", "-"],
            [".", "0", "=", "*", "/"]
        ]

        for row, row_of_symbols in enumerate(self.button_list):
            for column, symbols in enumerate(row_of_symbols):

                if symbols == "=":
                    command = self.parent.calculate

                elif symbols == "C":
                    command = lambda: self.parent.inserted_number.set("")

                elif symbols == "CE":
                    command = self.parent.backspace
                    
                else:
                    command = lambda symbol=symbols: self.parent.input_symbol(symbol)
                    
                self.simple_buttons_layout = tk.Button(self, text=symbols, command=command)
                self.simple_buttons_layout.grid(row=row, column=column)

window = CalculatorBody()
window.mainloop()