import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

tickers = ['SHOP', 'GME' ,'TSLA' ,'BB' ,'BBW' ,'CHGG' ,'CSCO', 'BBBY', 'PLTR' ,'KOSS' ,'DG',
 'CLNE' ,'EQIX' ,'CLOV' ,'GS' ,'HA', 'HD' ,'JNJ', 'LDOS' ,'MMP' ,'MARA' ,'MCD' ,'MU',
 'PINS', 'PAA', 'PSA', 'RIOT' ,'RPRX' ,'LUV' ,'SIVB' ,'TDOC' ,'TXT' ,'TMDX', 'UL',
 'U' ,'V', 'WMT' ,'DRIV' ,'SDIV' ,'EEM', 'IDRV']
 
# Set the investment weights (I arbitrarily picked for example)
weights_t = np.array([0.0231, 0.0244, 0.0261, 0.0213, 0.0258, 0.0111, 0.0415, 0.0449 ,0.0371, 0.0145,
 0.0277 ,0.0239 ,0.0203, 0.018 , 0.0279, 0.0315,0.0208, 0.0278 ,0.0232, 0.005,
 0.0073 ,0.0251, 0.0292, 0.0131, 0.0148 ,0.0201, 0.0056,0.0259, 0.0131 ,0.0284,
 0.0161, 0.045 , 0.0204, 0.0174, 0.0127, 0.0101, 0.0343 ,0.0166 ,0.0182 ,0.0201,
 0.0165])

weights = weights_t + 0.0022951219512195122

df = yf.download(tickers,start='2000-12-01',end='2021-6-29')

df = np.log(1+df['Adj Close'].pct_change())

def portfolioreturn(weights):
    return np.dot(df.mean(),weights)

def portfoliostd(weights):
    return (np.dot(np.dot(df.cov(),weights),weights))**(1/2)*np.sqrt(250)

print(portfoliostd(weights))

def weightscreator(df):
    rand = np.random.random(len(df.columns))
    rand /= rand.sum()
    return rand

print(weightscreator(df))

returns = []
stds = []
w = []

for i in range(500):
    weights =  weightscreator(df)
    returns.append(portfolioreturn(weights))
    stds.append(portfoliostd(weights))
    w.append(weights)

#print (returns)

plt.scatter(stds,returns)
plt.scatter(df.std().iloc[0]*np.sqrt(250),df.mean().iloc[0], c ='k')
plt.scatter(df.std().iloc[1]*np.sqrt(250),df.mean().iloc[1], c ='yellow')
plt.scatter(df.std().iloc[2]*np.sqrt(250),df.mean().iloc[2], c ='red')
plt.scatter(df.std().iloc[3]*np.sqrt(250),df.mean().iloc[3], c ='pink')
plt.scatter(df.std().iloc[4]*np.sqrt(250),df.mean().iloc[4], c ='grey')
plt.scatter(min(stds),returns[stds.index(min(stds))], c='green')
plt.title("Efficient frontier")
plt.xlabel("portfoliostd")
plt.ylabel("portfolioreturn")
plt.show()

stds.index(min(stds))
