import pandas as pd
import pandas_datareader.data as web
import datetime as dt
start = dt.datetime(1900, 1, 1)
end = dt.datetime.today()
df = web.DataReader(['TSLA','AAPL', 'RELIANCE.NS', 'TCS.NS', 'AMZN'], 'yahoo', start, end)
df.to_csv("stocks_data.csv")
print("data fetched succesfully")
