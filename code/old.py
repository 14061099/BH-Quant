# -*- coding: utf-8 -*-
import random
from glb import *
from config import Config
from datetime import timedelta,datetime
from function import *

def initialize(context,g):
    stocks = ['SH600000', 'SH600007', 'SH600009']
    set_universe(stocks)
    set_startDate(datetime(2015,8,1))
    set_endDate(datetime(2016,2,2))
    set_frequency('day')

    g.times=0
    g.end = []
    g.info = []
    g.security = "SH600000"
    g.flag = False

# 双均线
'''
def handle_data(context,o,g):
    g.times += 1
    #print g.times
    if (g.times%1000==0):
        print context.current_dt
    if (g.days>1):
        g.f.write(context.current_dt.strftime('%y-%m-%d %H:%M')+'\n')
        #print context.current_dt.strftime('%y-%m-%d %H:%M')," ---- ",totalValue()
        n1 = 5
        n2 = 10
        security = g.security
        a = attribute_history(security, 10, '1m')
        if (a is None):
            return
        ma_n1 = a['end'][-n1:].astype('float').mean()
        ma_n2 = a['end'][-n2:].astype('float').mean()
        g.f.write('    '+'n1,n2 : ' +str(ma_n1)+' , '+str(ma_n2)+'\n')
        cash = context.portfolio.cash
        #print "n1,n2:",ma_n1,ma_n2
        g.end.append(a.iloc[0].start)
        if (ma_n1 > ma_n2): #buy in
            order = o.order_value(security, cash)

        else:# sell out
            order = o.order_target(security, 0)
        #print context.current_dt.strftime('%y-%m-%d ') + 'totalValue,benchmarkValue : ',totalValue(), benchmarkValue()
        return 0
'''
def handle_data(context,o,g):
    g.times += 1
    if (g.days==1 and g.flag==False):
        g.flag = True
        print context.current_dt
        cash = context.portfolio.cash / 3
        for stock in context.universe:
            order_value(stock,cash)
    elif (g.days%5==0):
        for stock in context.universe:
            order_target(stock,0)
        cash = context.portfolio.cash / 3
        for stock in context.universe:
            order_value(stock,cash)


def show_info(context,g):
    print '\norder'
    for i in Global.orderInfo:
        print i
    print 'totalValue,',totalValue()

if __name__=="__main__":
    #print security.security
    day = context.current_dt + timedelta(days=15)

