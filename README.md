# Arbitrage

Arbitrage is the simultaneous purchase and sale of the same asset in different markets in order to profit from tiny differences in the asset's listed price. It exploits short-lived variations in the price of identical or similar financial instruments in different markets or different forms.

This project tries to find arbitrage in a real-world scenario. For this, I have taken cryptocurrency as currency, and for the data, I have used the API from
https://min-api.cryptocompare.com/documentation.

### Running the algorithm

- Get your API key from https://min-api.cryptocompare.com/documentation.
- Replace your API key in the run.py file where it is mentioned.
- Run the run.py file and wait for the algorithm to run its logic.

### Note

This algorithm can not be used in the real world as it takes some time to calculate the result, and while doing so, it works on a snapshot of the cryptocurrency price data and not the realtime
price. Also, the window for trading crypto for the arbitrage to actually work is very narrow. Hence it is not possible to find arbitrage in real time.
