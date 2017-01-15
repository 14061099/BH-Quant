import data
from pandas import DataFrame
from datetime import datetime, timedelta
from Query import get_data
from Query_new import get_data_Daily
from pandas import Series

class Security(object):
    def __init__(self,context):
        # security dtype:dataframe
        print "initializing security"
        datas = []
        for stock in context.universe:
            print 'loading ',stock,' ......'
            datas.append(get_data(stock,context.start_date,context.end_date))
        self._securities = Series(datas, index=context.universe)
        self._security = get_data(context.universe[0],context.start_date,context.end_date)
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
        id = list(security['datetime']).index(current_dt)
        res = security.iloc[id].end
        return float(res)

if __name__=="__main__":
    from glb import *
    print security.day_security