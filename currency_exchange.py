import tkinter as tk
import requests
import webbrowser
import pyperclip
import configparser
from tkinter import ttk
from style import apply_custom_styles

class CurrencyExchange(tk.Toplevel):
    def __init__(self):
        super().__init__() # Take everything from parent

        self.title("Currency exchange")
        self.geometry("275x165")
        self.resizable(False, False)
        
        self.user_input = tk.StringVar(self, "")

        self.confirm_key_button = ttk.Button(self, text="Confirm", command=self.write_to_ini, style='Confirm.TButton')
        self.input_key = ttk.Entry(self, textvariable=self.user_input, style='TEntry')
        self.input_label = tk.Label(self, text='Input API key:', font=('Arial', 11))
        self.api_key_tip = tk.Label(self, text='Get your API key here:', font=('Arial', 9, 'italic'))
        self.api_url = tk.Label(self, text='www.exchangerate-api.com', fg='blue', font=('Arial', 9, 'underline'), cursor='hand2')

        apply_custom_styles(self)

        self.api_key = configparser.ConfigParser()

        if not self.api_key.read('api_key.ini'):
            self.startup_widgets()

            self.api_key['key'] = {'key': ''}
            with open('api_key.ini', 'w') as config_file:
                self.api_key.write(config_file)

        else:
            key = self.api_key["key"]["key"]
            self.user_input.set(key)
            self.check_internet_connection()

    def write_to_ini(self):
        self.api_key['key']['key'] = self.user_input.get()
        with open('api_key.ini', 'w') as config_file:
            self.api_key.write(config_file)
            self.check_internet_connection()

    def open_api_url(self, url):
        webbrowser.open_new(url)

    def startup_widgets(self):
        self.input_label.pack()
        self.input_key.pack()
        self.confirm_key_button.pack(pady=5)
        self.api_key_tip.pack(pady=5)
        self.api_url.pack()
        self.api_url.bind('<Button-1>', lambda event: self.open_api_url('https://www.exchangerate-api.com/'))

    def check_internet_connection(self):
        try:
            requests.head("https://www.google.com")
            self.check_key(connection=True)
        
        except requests.exceptions.ConnectionError:
            self.user_input.set("Not connected")
            self.check_key(connection=False)

    def check_key(self, connection):
        if connection:
            try:
                url_key = self.user_input.get()
                url = f"https://v6.exchangerate-api.com/v6/{url_key}/latest/USD"

                request = requests.get(url)
                all_info = request.json()
                self.conversion_rates = all_info["conversion_rates"]

                if self.confirm_key_button.winfo_ismapped():
                    self.confirm_key_button.destroy()
                    self.input_key.destroy()
                    self.input_label.destroy()
                    self.api_key_tip.destroy()
                    self.api_url.destroy()
                
                self.conversion_widgets()

            except Exception as e:
                print(e)
                self.startup_widgets()
                self.user_input.set("Not a valid key")

    def conversion_widgets(self):
        self.currencies = list(self.conversion_rates.keys())
        self.input_number = tk.StringVar(self, "")
        self.output_number = tk.StringVar(self, "0")

        self.starting_currency_combo = ttk.Combobox(self, values=self.currencies, state="readonly", style="TCombobox")
        self.finishing_currency_combo = ttk.Combobox(self, values=self.currencies, state="readonly", style="TCombobox")
        self.starting_currency_combo.set("USD")
        self.finishing_currency_combo.set("EUR")

        self.startring_currency_entry = ttk.Entry(self, textvariable=self.input_number, style="TEntry")
        self.finishing_currency_entry = ttk.Entry(self, textvariable=self.output_number, state="readonly", style="TEntry")

        self.confirm_exchange = ttk.Button(self, text="Confirm", command=self.conversion, style="Confirm.TButton")
        self.confirm_exchange.grid(row=0, column=1, padx=5, pady=5)
        self.copy_result = ttk.Button(self, text="Copy", command=lambda:pyperclip.copy(self.final_value), style="Copy.TButton")
        self.copy_result.grid(row=2, column=1, padx=5, pady=5)

        self.starting_currency_combo.grid(row=1, column=0, padx=5, pady=5)
        self.startring_currency_entry.grid(row=0, column=0, padx=5, pady=5)
        self.finishing_currency_combo.grid(row=3, column=0, padx=5, pady=5)
        self.finishing_currency_entry.grid(row=2, column=0, padx=5, pady=5)

    def conversion(self):
        value_index1 = self.starting_currency_combo.current()
        value_index2 = self.finishing_currency_combo.current()

        self.currency1_value_in_usd = float(list(self.conversion_rates.values())[value_index1])
        self.currency2_value_in_usd = float(list(self.conversion_rates.values())[value_index2])

        value1 = float(self.input_number.get())
        usd = value1 / self.currency1_value_in_usd
        self.final_value = usd * float(self.currency2_value_in_usd)

        self.output_number.set(f"{self.final_value:,.5g}")

if __name__ == "__main__":
    window = CurrencyExchange()
    window.mainloop()