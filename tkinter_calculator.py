import tkinter as tk
import pyperclip
import currency_exchange as ce
import math
import random
from style import apply_custom_styles
from tkinter import ttk
from simpleeval import SimpleEval

def sin_deg(x):
    result = math.sin(math.radians(x))
    return round(result, 5)

def cos_deg(x):
    result = math.cos(math.radians(x))
    return round(result, 5)

def tan_deg(x):
    if abs(x % 180) > 90 or abs(x % 180) < 90:
        result = math.tan(math.radians(x))
        return round(result, 5)
    
    if abs(x % 180) == 90:
        return None

def cot_deg(x):
    if x % 180> 0 or x % 180 < 0:
        result = 1 / math.tan(math.radians(x))
        return round(result, 5)
    
    if x % 180 == 0:
        return None
    
def cot_rad(x):
    result = 1 / math.tan(x)
    return round(result, 5)

def asin_deg(x: int | float) -> int | float:
    return round(math.asin(x) * (180 / math.pi), 5)

def acos_deg(x: int | float) -> int | float:
    return round(math.acos(x) * (180 / math.pi))

def atan_deg(x: int | float) -> int | float:
    return round(math.atan(x) * (180 / math.pi))

def acot_deg(x: int | float) -> int | float:
    if x > 0:
        return round(math.atan(1/x) * (180 / math.pi), 5)
    else:
        return round((math.atan(1/x) + 180) * (180 / math.pi), 5)
    
def acot_rad(x: int | float) -> int | float:
    if x > 0:
        return round(math.atan(1/x), 5)
    else:
        return round((math.atan(1/x) + math.pi), 5)

def factorial(x):
    try:
        return math.factorial(x)
    
    except:
        return math.gamma(x + 1)

class CalculatorBody(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculator")
        self.geometry("430x200")
        self.resizable(False, False)
        self.option_add("*tearOff", False)

        self.inserted_number = tk.StringVar(self, "")
        self.output_number = tk.StringVar(self, "0")
        self.history_list = ['No history']
        self.result_history = ['']
        # --- Scientific string vars ---
        self.deg_button = tk.StringVar(self,'Rad → Deg')
        self.sin = tk.StringVar(self, 'sin')
        self.cos = tk.StringVar(self, 'cos')
        self.tan = tk.StringVar(self, 'tan')
        self.cot = tk.StringVar(self, 'cot')
        self.ln = tk.StringVar(self, 'ln')
        self.log = tk.StringVar(self, 'log')
        self.fact = tk.StringVar(self, 'fact')
        self.squared = tk.StringVar(self, '^2')
        self.ans_rnd = tk.StringVar(self, 'Ans')

        self.deg2rad_rad2deg()

        try:
            self.logo = tk.PhotoImage(file="calculator.png")
            self.iconphoto(True, self.logo)
        except tk.TclError:
            pass

        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)

        self.simple_calculator_buttons = SimpleModeButtons(self) # Sends self to parent
        self.simple_calculator_buttons.grid(row=0, column=1, padx=10, pady=10)

        self.display = DisplayHistory(self)
        self.display.grid(row=0, column=0, padx=10, pady=10)

        self.bind("<Return>", self.calculate) # .bind - binds key to a function.

        for key in "0123456789+-*/.()":
            self.bind(key, lambda event, k=key:self.input_binds(k) ) # Making k=key to lock in every key

        self.bind("<BackSpace>", self.backspace)

        apply_custom_styles(self)

    def calculate(self, event=None):
        operations = ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'cot', 'log', 'ln', 'e', 'π', '^', 'fact', 'sqrt']
        self.expression = self.inserted_number.get()

        if not any ((element in self.expression) for element in operations):
            self.output_number.set('Not an expression')
        
        else:
            try:
                to_the_power_of = self.expression.replace('^', '**')
                self.result = self.evaluator.eval(to_the_power_of)
                self.output_number.set(f"{self.result:,.15g}")
                self.calculation_history()

            except Exception as error:
                self.output_number.set("Error")
                print(error.args)

    def get_cursor_pos(self):
        cursor_pos = self.display.inserted_number_entry.index(tk.INSERT) # INSERT - gets the pos of blinking cursor
        return cursor_pos

    def backspace(self, event=None):
        old_entry = self.inserted_number.get()
        
        if event is None and self.focus_get() == self.display.inserted_number_entry:
            cursor_pos = self.get_cursor_pos()

            new_entry = old_entry[:cursor_pos - 1] + old_entry[cursor_pos:]
            self.inserted_number.set(new_entry)
            self.output_number.set('0')
            self.display.inserted_number_entry.icursor(cursor_pos-1)
        
        elif event is None or self.focus_get() != self.display.inserted_number_entry:
            new_entry = old_entry[:-1]
            self.inserted_number.set(new_entry)
            self.output_number.set('0')


    def input_symbol(self, symbol):
        self.display.inserted_number_entry.focus_set()
        old_entry = self.inserted_number.get()
        symbol_len = len(symbol)

        if self.focus_get() == self.display.inserted_number_entry:
            cursor_pos = self.get_cursor_pos()

            new_entry = old_entry[:cursor_pos] + symbol + old_entry[cursor_pos:]

        else: 
            new_entry = old_entry + symbol

        self.inserted_number.set(new_entry)

        if symbol_len > 1 and symbol != self.result_history[-1]:
            self.display.inserted_number_entry.icursor(cursor_pos+symbol_len-1)
        else:
            self.display.inserted_number_entry.icursor(cursor_pos+symbol_len)

    def input_binds(self, k):
        if self.focus_get() != self.display.inserted_number_entry:
            old_entry = self.inserted_number.get()
            new_entry = old_entry + k
            self.inserted_number.set(new_entry)

    def calculation_history(self):
        if self.expression == self.history_list[-1] and self.display.output_number_entry.get() == self.result_history[-1]:
            pass

        else:
            if 'No history' in self.history_list:
                self.history_list.clear()
                self.display.history.delete(0)
            
            if len(self.history_list) == 10:
                self.history_list.pop(0)
                self.result_history.pop(0)
                self.display.history.delete(0)

            self.history_list.append(self.expression)
            self.result_history.append(self.output_number.get())
            self.display.history.add_command(label=self.history_list[-1] + " = " + self.result_history[-1], command=lambda expression=self.history_list[-1]: (self.inserted_number.set(expression), self.calculate()))

    def ans(self):
        if self.ans_rnd.get() == 'Ans':
            if self.result_history[-1] == '':
                pass

            else: 
                self.input_symbol(self.result_history[-1])
        
        else:
            random_number: str = str(round(random.random(), 5))
            self.input_symbol(random_number)

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

    def shrink_calculator(self):
        self.geometry("430x200")

        try:
            self.scientific_mode.destroy()

        except AttributeError:
            pass

    def expand_calculator(self):
        self.geometry("430x375")

        self.scientific_mode = ScientificMode(self)
        self.scientific_mode.grid(row=1, column=0, columnspan=2)

    def deg2rad_rad2deg(self):
        
        if self.deg_button.get() == 'Deg → Rad':
            self.evaluator = SimpleEval(functions={
                'sin': lambda num: round(math.sin(num), 5),
                'cos': lambda num: round(math.cos(num), 5),
                'tan': lambda num: round(math.tan(num), 5),
                'cot': cot_rad,
                'asin': lambda num: round(math.asin(num), 5),
                'acos': lambda num: round(math.acos(num), 5),
                'atan': lambda num: round(math.atan(num), 5),
                'acot': acot_rad,
                'log': math.log10,
                'ln': lambda num: math.log(num, math.e),
                'π': math.pi,
                'e': math.e,
                'fact': factorial,
                'sqrt': math.sqrt,
            })

            self.deg_button.set('Rad → Deg')

        elif self.deg_button.get() == 'Rad → Deg':
            self.evaluator = SimpleEval(functions={
                'sin': sin_deg,
                'cos': cos_deg,
                'tan': tan_deg,
                'cot': cot_deg,
                'asin': asin_deg,
                'acos': acos_deg,
                'atan': atan_deg,
                'acot': acot_deg,
                'log': math.log10,
                'ln': lambda num: math.log(num, math.e),
                'π': math.pi,
                'e': math.e,
                'fact': factorial,
                'sqrt': math.sqrt,
            })

            self.deg_button.set('Deg → Rad')

    def invert(self):
        if self.sin.get() == 'sin':
            self.sin.set('asin')
            self.cos.set('acos')
            self.tan.set('atan')
            self.cot.set('acot')
            self.ln.set('e^')
            self.log.set('10^')
            self.squared.set('sqrt')
            self.ans_rnd.set('Rnd')

        else:
            self.sin.set('sin')
            self.cos.set('cos')
            self.tan.set('tan')
            self.cot.set('cot')
            self.ln.set('ln')
            self.log.set('log')
            self.squared.set('^2')
            self.ans_rnd.set('Ans')

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
                    
                self.simple_buttons_layout = ttk.Button(self, text=symbols, style=style, command=command, takefocus=False)
                self.simple_buttons_layout.grid(row=row, column=column, padx=2, pady=2)

class ScientificMode(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


        self.button_list = [
            [(self.parent.deg_button, 'Scientific.Blue.TButton'), ('Inv', 'Scientific.Blue.Small.TButton'), (self.parent.ans_rnd, 'Scientific.White.TButton')],
            [(self.parent.sin, 'Scientific.Yellow.TButton'), (self.parent.cos, 'Scientific.Yellow.TButton'), ('π', 'Scientific.White.TButton'), ('e', 'Scientific.White.TButton')],
            [(self.parent.tan, 'Scientific.Yellow.TButton'), (self.parent.cot, 'Scientific.Yellow.TButton'), (self.parent.fact, 'Scientific.Gray.TButton'), ('root', 'Scientific.Gray.TButton')],
            [(self.parent.ln, 'Scientific.Gray.TButton'), (self.parent.log, 'Scientific.Gray.TButton'), (self.parent.squared, 'Scientific.Gray.TButton'), ('^', 'Scientific.Gray.TButton')]
        ]

        for row, row_of_symbols in enumerate(self.button_list):
            for column, (symbols, style) in enumerate(row_of_symbols):

                if symbols == self.parent.deg_button:
                    command = self.parent.deg2rad_rad2deg
                    columnspan = 2
                    textvariable = self.parent.deg_button

                    self.scientific_calculator_layout = ttk.Button(self, textvariable=textvariable, style=style, command=command, takefocus=False)

                elif symbols == self.parent.ans_rnd:
                    command = self.parent.ans
                    columnspan = 1
                    column += 1

                    self.scientific_calculator_layout = ttk.Button(self, textvariable=symbols, style=style, command=command, takefocus=False)

                elif symbols == 'root':
                    command = lambda: self.parent.input_symbol('^(1/)')
                    columnspan = 1

                    self.scientific_calculator_layout = ttk.Button(self, text=symbols, style=style, command=command, takefocus=False)

                elif symbols == 'Inv':
                    command = self.parent.invert
                    columnspan = 1
                    column += 1

                    self.scientific_calculator_layout = ttk.Button(self, text=symbols, style=style, command=command, takefocus=False)

                else:
                    num_symbols = ('π', 'e', '^')

                    if symbols in num_symbols:
                        command = lambda symbol=symbols: self.parent.input_symbol(symbol)

                        self.scientific_calculator_layout = ttk.Button(self, text=symbols, style=style, command=command, takefocus=False)
                    else:
                        command = lambda symbol=symbols: self.parent.input_symbol(symbol.get()+'()')

                        self.scientific_calculator_layout = ttk.Button(self, textvariable=symbols, style=style, command=command, takefocus=False)

                    columnspan = 1

                self.scientific_calculator_layout.grid (row=row, column=column, columnspan=columnspan, padx=2, pady=2)


class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.config(bg='white')

        self.mode_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(menu=self.mode_menu, label='Mode', font=('Arial', 11)) 
        self.mode_menu.add_command(label='Simple', command=self.parent.shrink_calculator)
        self.mode_menu.add_command(label='Scientific', command=self.parent.expand_calculator)
        self.mode_menu.add_command(label='Currency exchange', command=self.parent.open_currency_exchange)

if __name__ == '__main__':
    window = CalculatorBody()
    window.mainloop()