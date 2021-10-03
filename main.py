import pandas as pd
import requests
import os
import json
import tqdm


class arbitrage:

    def __init__(self, AUTH) -> None:
        self.AUTH = AUTH

    def top_exchange_pairs(self):
        url = "https://min-api.cryptocompare.com/data/v3/all/exchanges?topTier=true&api_key=" + self.AUTH
        r = requests.get(url)
        print(type(r))
        with open("pairs_list.json", "w") as f:
            json.dump(r.json(), f)
            
    def binance_connected_pairs(self):
        with open("pairs_list.json", "r") as f:
            data = json.load(f)
        pairs = data["Data"]["Binance"]["pairs"]
        return {k: v for k, v in pairs.items() if len(v) > 3}
        #k = BTC (key)
        #v = [usd,eth,xyz] (value)
    
    def download_snapshot(self,pair_dict, outfolder):
        if not os.path.exists(outfolder):
            os.makedirs(outfolder)

        # Download data and write to files
        #p1 = key 
        #p2s = array of values
        for p1, p2s in tqdm.tqdm(pair_dict.items()):
            url = (
                "https://min-api.cryptocompare.com/data/" 
                + f"ob/l1/top?fsyms={p1}&tsyms={','.join(p2s)}"
                + "&e=Binance&api_key=" + self.AUTH
            )
            r = requests.get(url)
            with open(f"{outfolder}/{p1}_pairs_snapshot.json", "w") as f:
                json.dump(r.json(), f)

    def create_adj_matrix(self,pair_dict, snapshot_directory, outfile="snapshot.csv"):

        """
        e.g col BTC row ETH is how much ETH you get for 1 BTC
        e.g col ETH row BTC is how much BTC you get for 1 ETH

        :param pair_dict: dict of pairs
        :type pair_dict: {str : str list}
        :param outfile: name of output adjacency matrix file
        :type outfile: str
        """

        # Union of 'from' and 'to' pairs
        flatten = lambda l: [item for sublist in l for item in sublist]
        all_pairs = list(set(pair_dict.keys()).union(flatten(pair_dict.values())))

        # Create empty df
        df = pd.DataFrame(columns=all_pairs, index=all_pairs)

        for p1 in pair_dict.keys():
            with open(f"{snapshot_directory}/{p1}_pairs_snapshot.json", "r") as f:
                res = json.load(f)

            if res["Data"]["RAW"] == {}:
                continue

            quotes = res["Data"]["RAW"][p1]
            for p2 in quotes:
                try:
                    df[p1][p2] = float(quotes[p2]["BID"])
                    df[p2][p1] = 1 / float(quotes[p2]["ASK"])
                except KeyError:
                    print(f"Error for {p1}/{p2}")
                    continue
        df.to_csv(outfile)




