import requests
import json

### API Documention: https://site.financialmodelingprep.com/developer/docs
def get_stock_list():
    """
    This function will return a list of stock data dictionaries from the FMP API

    NOTE: I only get 250 requests per day
    """
    
    url = "https://financialmodelingprep.com/api/v3/symbol/NASDAQ?apikey=6agBUcu9TOtH9qZrX6HUaZlCZU8xRGGR"

    try:
        response = requests.get(url)
        stock_list = json.loads(response.text)
        return stock_list
    except requests.exceptions.RequestException as e:
        print(e)

def get_stock_percent_change(stock_symbol):
    """
    This function will return a dictionary of stock data based on the stock symbol
    """

    stock_list = get_stock_list()

    if stock_list:
        for stock in stock_list:
            if stock["symbol"] == stock_symbol:
                return stock["changesPercentage"]
            
stock_percent_change = get_stock_percent_change("PLTR")
print(stock_percent_change)
