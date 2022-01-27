import pandas as pd
import numpy as np

# For reading stock data from yahoo
import pandas_datareader.data as web

# For time stamps
import datetime

# stocks of companies will use for analysis
company = ['DJIA', '^GSPC', 'T', 'F','AAPL', 'MSFT', 'NIO', 'BAC', 'INTC', 'VZ', 'TMUS', 'PFE', 'TSLA', 'GOOG', 'AMZN', 'UBER', 'CSCO', 'BABA', 'C', 'FB', 'JPM', 'TWTR', 'KO', 'PYPL', 'GS', 'MRNA', 'NFLX', 'ZM']

# Set up End and Start times for data grab
end = datetime.date.today()
start = datetime.datetime(2016, 1, 1)


#loop for grabing yahoo finance data and setting as a dataframe
for stock in company:
    # Set DataFrame as the Stock Ticker
    price = web.DataReader(stock, 'yahoo', start, end)
    price['symbol'] = stock
    filename = stock + '.csv'
    price.to_csv(filename, index = True)

