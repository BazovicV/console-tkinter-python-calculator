import tkinter as tk
import pyperclip
import currency_exchange as ce
from style import apply_custom_styles
from tkinter import ttk
from simpleeval import SimpleEval

class CalculatorBody(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculator")
        self.geometry("475x200")
        self.resizable(False, False)
        self.option_add("*tearOff", False)

        self.inserted_number = tk.StringVar(self, "")
        self.output_number = tk.StringVar(self, "0")
        self.history_list = ['No history']

        self.evaluator = SimpleEval()

        try:
            self.logo = tk.PhotoImage(file="calculator.png")
            self.iconphoto(True, self.logo)
        except tk.TclError:
            pass

        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)

        self.simple_calculator_buttons = SimpleModeButtons(self) # Sends self to parent
        self.simple_calculator_buttons.pack(side="right", fill="x", padx=10, pady=10)

        self.display = DisplayHistory(self)
        self.display.pack(side="left", fill="y", expand=True, padx=10, pady=20)

        self.bind("<Return>", self.calculate) # .bind - binds key to a function.

        for key in "0123456789+-*/.()":
            self.bind(key, lambda event, k=key:self.input_binds(k) ) # Making k=key to lock in every key

        self.bind("<BackSpace>", self.backspace)

        apply_custom_styles(self)

    def calculate(self, event=None):
        operations = ['+', '-', '*', '/']
        self.expression = self.inserted_number.get()

        if not any ((element in self.expression) for element in operations):
            self.output_number.set('Not an expression')
        
        else:
            try:
                self.result = self.evaluator.eval(self.expression)
                self.output_number.set(f"{self.result:,.15g}")
                self.calculation_history()

            except Exception:
                self.output_number.set("Error")

    def backspace(self, event=None):
        if event == None or self.focus_get() != self.display.inserted_number_entry:
            old_entry = self.inserted_number.get()
            new_entry = old_entry[:-1]
            self.inserted_number.set(new_entry)
            self.output_number.set('0')

    def input_symbol(self, symbol):
        old_entry = self.inserted_number.get()
        new_entry = old_entry + symbol
        self.inserted_number.set(new_entry)

    def input_binds(self, k):
        if self.focus_get() != self.display.inserted_number_entry:
            old_entry = self.inserted_number.get()
            new_entry = old_entry + k
            self.inserted_number.set(new_entry)

    def calculation_history(self):
        if self.expression == self.history_list[-1]:
            pass

        else:
            if 'No history' in self.history_list:
                self.history_list.clear()
                self.display.history.delete(0)
            
            if len(self.history_list) == 10:
                self.history_list.pop(0)
                self.display.history.delete(0)

            self.history_list.append(self.expression)
            self.display.history.add_command(label=self.history_list[-1], command=lambda expression=self.history_list[-1]: (self.inserted_number.set(expression), self.calculate()))

    def copy_history(self):
        if 'No history' in self.history_list:
            pass

        else:
            history_string = str(self.history_list)
            for char in "[]'":
                history_string = history_string.replace(char, '')
            pyperclip.copy(history_string)

    def clear_history(self):
        self.history_list.clear()
        self.display.history.delete(0, 'end')
        self.history_list.append('No history')
        self.display.history.add_command(label=self.history_list[0])

    def open_currency_exchange(self):
        self.exchange_window = ce.CurrencyExchange()
        self.exchange_window.focus()

class DisplayHistory(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.text_before_input = tk.Label(self, text="Input:", font=("Arial", 11))
        self.text_before_input.grid(row=0, column=0, columnspan=3)

        self.inserted_number_entry = ttk.Entry(self, textvariable=parent.inserted_number, style="TEntry")
        self.inserted_number_entry.grid(row=1, column=0, columnspan=3)

        self.text_before_output = tk.Label(self, text="Output:", font=("Arial", 11))
        self.text_before_output.grid(row=2, column=0, columnspan=3)

        self.output_number_entry = ttk.Entry(self, textvariable=parent.output_number, style="TEntry")
        self.output_number_entry.config(state="readonly")
        self.output_number_entry.grid(row=3, column=0, columnspan=3)

        self.history_button = ttk.Menubutton(self, text='History', style='History.TButton')
        self.history = tk.Menu(self.history_button)
        self.history_button['menu'] = self.history

        self.history.add_command(label=self.parent.history_list[0])

        self.history_button.grid(row=4, column=0, pady=26)

        self.copy_history = ttk.Button(self, text='Copy', command=self.parent.copy_history, style='Copy.TButton')
        self.copy_history.grid(row=4, column=1, pady=26)

        self.clear_history = ttk.Button(self, text='CH', command=self.parent.clear_history, style='Red.TButton')
        self.clear_history.grid(row=4, column=2, pady=26)

class SimpleModeButtons(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent # So it remember what is the parent

        self.button_list = [ # Nested list
            [("7", "White.TButton"), ("8", "White.TButton"), ("9", "White.TButton"), ("C", "Red.TButton"), ("CE", "Red.TButton")],
            [("4", "White.TButton"), ("5", "White.TButton"), ("6", "White.TButton"), ("(", "Gray.TButton"), (")", "Gray.TButton")],
            [("1", "White.TButton"), ("2", "White.TButton"), ("3", "White.TButton"), ("+", "Gray.TButton"), ("-", "Gray.TButton")],
            [(".", "White.TButton"), ("0", "White.TButton"), ("=", "Blue.TButton"), ("*", "Gray.TButton"), ("/", "Gray.TButton")]
        ]

        for row, row_of_symbols in enumerate(self.button_list):
            for column, (symbols, style) in enumerate(row_of_symbols):

                if symbols == "=":
                    command = self.parent.calculate

                elif symbols == "C":
                    command = lambda: (self.parent.inserted_number.set(""), self.parent.output_number.set('0'))

                elif symbols == "CE":
                    command = self.parent.backspace
                    
                else:
                    command = lambda symbol=symbols: self.parent.input_symbol(symbol)
                    
                self.simple_buttons_layout = ttk.Button(self, text=symbols, style=style, command=command)
                self.simple_buttons_layout.grid(row=row, column=column, padx=2, pady=2)

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.config(bg='white')

        self.mode_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(menu=self.mode_menu, label='Mode', font=('Arial', 11)) 
        self.mode_menu.add_command(label='Simple')
        self.mode_menu.add_command(label='Currency exchange', command=self.parent.open_currency_exchange)

window = CalculatorBody()
window.mainloop()