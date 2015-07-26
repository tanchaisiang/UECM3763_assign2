import pylab as p
import pandas as pd

#Downloading daily data of Malayan Banking with the code 1155
from pandas.io.data import DataReader as DR
from datetime import datetime as dt

start = dt(2010,1,1)
end = dt(2015,7,24)
data = DR("1155.KL",'yahoo',start,end)

#Calculating 5-day moving average of Malayan Banking
MB = data['Close'].values
mov_avg = pd.rolling_mean(MB,5)

#Plotting
p.plot(mov_avg)
label = 'Days'; p.xlabel(label)
label = 'Average stock price'; p.ylabel(label)
p.title('5-days moving average of Malayan Banking')
p.show()

#Downloading FTSEKLCI daily data
combine_data = ["1155.KL","^KLSE"]
all_data = DR(combine_data,'yahoo',start,end)['Adj Close']

#Calculating correlation
correlation = all_data.corr()
print ('Correlation = ' +str(correlation))