from coinmarketcapapi import CoinMarketCapAPI

from dotenv import load_dotenv
import os

def load_api_keys():
    load_dotenv()

def getcoinvalue(coin):

    client_CoinMarketCapA = CoinMarketCapAPI(os.getenv('coinmarketcap_api_key'))
    coin_dollar_value = 0
    
    try:
        coin_dollar_value =  float(str(client_CoinMarketCapA.cryptocurrency_quotes_latest(symbol=coin.upper()).data[coin.upper()]['quote']['USD']['price']))
    except:
        print("Invalid client_CoinMarketCapA key or invalid coin")

    return coin_dollar_value

def main() -> None:
   
   load_api_keys()
   print(f"Cake value: {getcoinvalue('CAKE'):.2f} USDT")
   

if __name__ == '__main__':
    main()
