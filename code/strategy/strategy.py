#-*- coding:UTF-8 -*-
import random
from glb import *
from config import Config
from datetime import timedelta,datetime
from function import *
import pandas as pd

def initialize(context,g):
    stocks = ['SH600000']
    set_universe(stocks)
    set_startDate(datetime(2014,1,1))
    set_endDate(datetime(2016,1,1))
    set_frequency('day')

    g.security = "SH600000"
    g.flag = False

# 双均线
def handle_data(context,o,g):
    n1 = 5
    n2 = 10
    security = g.security
    a = attribute_history(security, n2, '1d')
    if (a is None):
        return
    ma_n1 = a['end'][-n1:].astype('float').mean() # 计算5日均线
    ma_n2 = a['end'][-n2:].astype('float').mean() # 计算10日均线
    cash = context.portfolio.cash
    # 比较均线关系
    if (ma_n1 > ma_n2):  # 全买
        order = order_value(security, cash)
    else:# 全卖
        order = order_target(security, 0)
    return 0

def show_info(context,g):
    print '\norder'
    for i in Global.orderInfo:
        print i
    print 'totalValue,',totalValue()