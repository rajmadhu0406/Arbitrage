from main import arbitrage
import graph

#get your api key from https://min-api.cryptocompare.com/
obj = arbitrage("your_api_key")

obj.top_exchange_pairs()
connected_pairs = obj.binance_connected_pairs()
obj.download_snapshot(connected_pairs, "data_")
print("Download finished. Creating adjacency matrix..")
obj.create_adj_matrix(connected_pairs, "data_")

graph.find_arbitrage(find_all=True)


