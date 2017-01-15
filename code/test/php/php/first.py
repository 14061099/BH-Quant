from hmmlearn.hmm import GaussianHMM
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import cm
from matplotlib import pyplot
startdate = '2012-06-01'
enddate = '2016-04-07'
df = get_price(['000300.XSHG'], start_date=startdate, end_date=enddate, frequency='daily', fields=['close','volume','high','low'])
close = df['close']['000300.XSHG']
high = df['high']['000300.XSHG'][5:]
low = df['low']['000300.XSHG'][5:]
volume = df['volume']['000300.XSHG'][5:]
money = df['volume']['000300.XSHG'][5:]
datelist = pd.to_datetime(close.index[5:])
logreturn = (np.log(np.array(close[1:]))-np.log(np.array(close[:-1])))[4:]
logreturn5 = np.log(np.array(close[5:]))-np.log(np.array(close[:-5]))
diffreturn = (np.log(np.array(high))-np.log(np.array(low)))
closeidx = close[5:]
X = np.column_stack([logreturn,diffreturn,logreturn5])
len(X)