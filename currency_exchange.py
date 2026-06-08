import tkinter as tk
from tkinter import ttk
import requests
import pyperclip
import configparser

class CurrencyExchange(tk.Toplevel):
    def __init__(self):
        super().__init__() # Take everything from parent

        self.title("Exchange rates")
        self.geometry("300x250")
        self.resizable(False, False)
        
        self.user_input = tk.StringVar(self, "")

        self.confirm_key_button = tk.Button(self, text="Confirm", command=self.write_to_ini)
        self.input_key = tk.Entry(self, textvariable=self.user_input)

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

    def startup_widgets(self):
        self.confirm_key_button.pack()

        self.input_key.pack()

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
                
                self.conversion_widgets()

            except Exception as e:
                print(e)
                self.user_input.set("Not a valid key")

    def conversion_widgets(self):
        self.currencies = list(self.conversion_rates.keys())
        self.input_number = tk.StringVar(self, "")
        self.output_number = tk.StringVar(self, "")

        self.starting_currency_combo = ttk.Combobox(self, values=self.currencies, state="readonly")
        self.finishing_currency_combo = ttk.Combobox(self, values=self.currencies, state="readonly")
        self.starting_currency_combo.set("USD")
        self.finishing_currency_combo.set("EUR")

        self.startring_currency_entry = tk.Entry(self, textvariable=self.input_number)
        self.finishing_currency_entry = tk.Entry(self, textvariable=self.output_number, state="readonly")

        self.confirm_exchange = tk.Button(self, text="Confirm", command=self.conversion)
        self.confirm_exchange.place(anchor="center", x=100, y=100)
        self.copy_result = tk.Button(self, text="Copy", command=lambda:pyperclip.copy(self.final_value))
        self.copy_result.place(anchor="center", x=200, y=100)

        self.starting_currency_combo.grid(row=0, column=1)
        self.startring_currency_entry.grid(row=0, column=0)
        self.finishing_currency_combo.grid(row=1, column=1)
        self.finishing_currency_entry.grid(row=1, column=0)

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