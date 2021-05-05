import os
import investpy
import argparse

#stock_symb = 'tnt_u'
stock_symb = 'aapl'
#country = 'canada'
country = 'united states'
interval = 'daily'

techDataMA = investpy.technical.moving_averages(stock_symb, country=country, product_type='stock', interval=interval)
techDataTI = investpy.technical.technical_indicators(stock_symb, country=country, product_type='stock', interval=interval)

print(techDataMA)
print(techDataTI)