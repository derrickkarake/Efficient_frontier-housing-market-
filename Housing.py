from matplotlib import colors
import pandas as pd
from pandas_datareader import data as pdr
import scipy
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm


test = []
date = []
f = plt.figure()
data = pd.read_csv("ASPUS.CSV", converters={"MSPS":float})
test = data.ASPUS
dates = data.DATE
x_values = [dt.datetime.strptime(d,"%Y-%m-%d").date() for d in dates]
MA = pd.Series(test)
new_ma4 = MA.rolling(5).mean()
new_ma8 = MA.rolling(10).mean()
print(new_ma4)
print(new_ma8)
my_array = np.asarray(test)

plt.figure(figsize=(15,8))
plt.plot(x_values,test,label = "price=403600")
plt.plot(x_values,new_ma4, c = "red", label = "MA5=392560")
plt.plot(x_values,new_ma8, c = "green", label = "MA10=386630")
plt.legend(loc="upper left")

plt.title("ASPUS data") # change this to refelct good time date
plt.xlabel("Years")
plt.ylabel("MSPS")
plt.show()




