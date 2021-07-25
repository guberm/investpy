#https://investpy.readthedocs.io/_api/stocks.html
#intervals = 5mins, 15mins, 30mins, 1hour, 5hours, daily, weekly, monthly
import investpy

stock_symb = 'AIM'
country = 'CANADA'
interval = 'weekly'

techData = ''
techDataIndicators = ''

def get_stock_tech_data(stock_symb, interval):
    techData = ''
    data = investpy.search_quotes(stock_symb, products=['stocks','etfs'], countries=[country], n_results=1)
    techData = data.retrieve_technical_indicators(interval=interval)

    #print(techData.head())
    print(techData)
    #return techData

get_stock_tech_data(stock_symb, interval)
