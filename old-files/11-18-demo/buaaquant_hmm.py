from hmmlearn.hmm import GaussianHMM
import numpy as np
import pandas as pd
import datetime
from Query import get_data_Daily
from matplotlib import cm,pyplot as plt
import warnings
import json
from Query import DateEncoder
warnings.filterwarnings("ignore")



high = 0
low = 0

class buaa_hmm():
    def __init__(self,begindate,enddate):
        self.data = get_data_Daily(stock_name='SZ399305', start_date=begindate, end_date=enddate)
        self.tradeDate = pd.to_datetime(self.data['datetime'][5:])

        self.closeindex = self.data['end']
        self.volume = np.array(self.data['amount'][5:]).astype('float')

        self.logReturn1 = np.array(np.diff(np.log(self.closeindex.astype('float'))))
        self.logReturn1 = self.logReturn1[4:]
        self.logReturn5 = np.log(np.array(self.closeindex[5:]).astype('float')) - np.log(
            np.array(self.closeindex[:-5]).astype('float'))
        print "init successfully"

    def hmm_explict_states(self):


        max = np.array(self.data['max']).astype('float')

        min = np.array(self.data['min']).astype('float')

        deltaindex = np.log(max) - np.log(min)
        deltaindex = deltaindex[5:]

        x = np.column_stack([self.logReturn1, self.logReturn5, deltaindex, self.volume])

        return x

    def hmm_getRes(self,states):
        res = pd.DataFrame({'tradeDate':self.tradeDate,'logReturn1':self.logReturn1,'logReturn5':self.logReturn5,
                                'volume':self.volume,'hidden_states':states})
        return res


class stat_handle():
    def __init__(self):
        print "the hmm model is training......"
        self.bh = buaa_hmm(begindate=datetime.datetime(2015, 1, 1), enddate=datetime.datetime(2015, 12, 20))
        self.t = self.bh.hmm_explict_states()
        print "before train"
        self.__model__ = GaussianHMM(n_components=5, covariance_type='diag', n_iter=100).fit(self.t)
        

    def show_hmm(self):
        hid_states = self.__model__.predict(self.t)
        res = self.bh.hmm_getRes(hid_states)

        file = open('hmm_status.json','w')

        out = {}
        print "before write status"
        out['datetime'] = res['tradeDate'].tolist()
        for i in range(self.__model__.n_components):
            idx = (hid_states == i)
            idx = np.append(0, idx[:-1])
            df = res.logReturn1
            res['ret%s' % i] = df.multiply(idx, axis=0)
            profit = np.exp(res['ret%s' % i].cumsum())
            out['status%s'% i] = profit.tolist()

        file.write(json.dumps(out,cls=DateEncoder))
        file.close()
#        plt.figure(figsize=(15, 8))
#        for i in range(self.__model__.n_components):
#            idx = (hid_states == i)
#            idx = np.append(0, idx[:-1])
#            df = res.logReturn1
#            res['ret%s' % i] = df.multiply(idx, axis=0)
#
#            plt.plot(np.exp(res['ret%s' % i].cumsum()), label='%dth hid states' % i)
#            plt.legend()
#            plt.grid(1)

#       plt.show()


    def bh_getState(self, es):
        bs = es + datetime.timedelta(days = -2)
        bh2 = buaa_hmm(begindate=bs, enddate=es)
        x = bh2.hmm_explict_states()
        if len(x):
            states = self.__model__.predict(x)
        else:
            states = [-1]
        return states[-1]


if __name__ == '__main__':
	sh = stat_handle()
	sh.show_hmm()


#	sts = sh.bh_getState(es = datetime.datetime(2016,5,20))
#	result = [0,0,0,0,0]
#	
#	for i in sts:
#		result[i] = result[i]+1
#	
#	for j in range(0,5,1):
#		print result[j]




