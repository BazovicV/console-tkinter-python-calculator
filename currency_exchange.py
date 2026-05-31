import requests

url_key = input("Enter your key:") # To use this converter you have to have a key from their site.
url = f"https://v6.exchangerate-api.com/v6/{url_key}/latest/USD"

requesting = requests.get(url)
all_info = requesting.json()
conversion_rates = all_info["conversion_rates"]

currencies = conversion_rates.keys()
currencies_values = conversion_rates.values()

def conversion():

    print(currencies)
    input_name1 = input("Select first currency:")
    input_amount = float(input("Input how much money you are exchanging: "))
    input_name2 = input("Enter second currency:")

    if input_name1 in currencies and input_name2 in currencies:

        currency_index1 = list(currencies).index(input_name1)
        currency_index2 = list(currencies).index(input_name2)
        value1 = float(list(currencies_values)[currency_index1])
        value2 = float(list(currencies_values)[currency_index2])

        value_in_usd = input_amount / value1
        final_value = value_in_usd * value2

        print(f"{final_value:,}")

conversion()