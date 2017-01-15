import data
from pandas import DataFrame
from datetime import datetime, timedelta
from Query import get_data
from Query_new import get_data_normal,get_data_Daily
from pandas import Series

class Security(object):
    def __init__(self,context):
        # security dtype:dataframe
        print "initializing security"
        data = []
        day_data = []
        for stock in context.universe:
            data.append(get_data_normal(stock,context.start_date,context.end_date))
            day_data.append(get_data_Daily(stock, context.start_date, context.end_date))
        self._securities = Series(data, index=context.universe)
        self._day_securities = Series(day_data, index=context.universe)
        self._security = get_data_normal(context.universe[0],context.start_date,context.end_date)
        self._day_security = get_data_Daily(context.universe[0],context.start_date,context.end_date)
        #self._security = DataFrame(data.data, columns=['datetime','start','end'])
 
    @property
    def security(self):
        return self._security

    @property
    def day_security(self):
        return self._day_security
 
    @property
    def securities(self):
        return self._securities

    @property
    def day_securities(self):
        return self._day_securities

    def next_day(self, current_date):
        if isinstance(current_date, datetime):
            d = current_date + timedelta(days=1)
            while self.hasday(d):
                try:
                    sublist = (self._security[d.strftime('%Y-%m-%d')])
                    res = sublist.iloc[0].datetime
                    return res
                except Exception,e:
                    d = d + timedelta(days=1)
                    return None
        else:
            print 'Security received an invalid parameter: a non-datetime object'
            return None

    def get_current_price(self, stock_name,current_dt):
        security = self._securities[stock_name]
        #id = list(security['datetime']).index(current_dt)
        #res = security.iloc[id].end
        res = security[security['datetime'].isin([current_dt])].iloc[0].end
        return float(res)

if __name__=="__main__":
    from glb import *