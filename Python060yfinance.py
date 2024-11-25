import yfinance as yf
import matplotlib.pyplot as plt

# Get the data for the stock AAPL
data = yf.download('AAPL','2020-01-01','2020-12-31')
print(data)
print(type(data)) # <class 'pandas.core.frame.DataFrame'>

import pandas as pd
print(type(pd.DataFrame())) # <class 'pandas.core.frame.DataFrame'>


# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()
