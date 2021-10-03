import requests
import json

#AUTH : 3d4818bf5064bafcb5b86ac0ef4cdedb

class arbitrage_money:

    def __init__(self, AUTH):
        self.AUTH = AUTH

    def top_exchange_pairs(self):
        url = "http://data.fixer.io/api/symbols?access_key=" + self.AUTH
        symbols = requests.get(url)
        symbols_json = symbols.json()
        symbols_list = symbols_json["symbols"]

        print(type(symbols_list))

        rates_list = {}

        for currency in symbols_list:
            rates_request = requests.get("http://data.fixer.io/api/latest?access_key="+self.AUTH+"&base%20=%20"+currency)
            rates_json = rates_request.json()
            rates_map = rates_json["rates"].json()  #key-value currency-rate for base
            rates_list[currency] = rates_map

            print(currency)
            #rates_list_json = json.dump(rates_list, )

       # with open("rates_pairs_list.json", "w+") as f:
        #    json.dump(rates_list.json(), f)

# testobj = arbitrage_money("3d4818bf5064bafcb5b86ac0ef4cdedb")
# testobj.top_exchange_pairs()
# print('done')


def tdm:

