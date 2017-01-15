# -*- coding: utf-8 -*-
from glb import Global as glb
from datetime import datetime, timedelta
from pandas import Series, DataFrame
import numpy as np

# 获取历史数据
def attribute_history(stock_name, count, unit='1d'):
    inter = unit[-1]  # day or minute
    gap = int(unit[0:-1])  #gap
    cnt = 0
    res = []

    if inter=='m':
        s = glb.security.securities[stock_name][glb.security.securities[stock_name]['datetime'] < glb.context.current_dt].tail(gap*count).reset_index(drop=True)
        id = len(s) - 1
        while (id >= 0 and cnt < count):
            res.append(id)
            cnt += 1
            id -= gap
        if cnt == 0:
            return None
        return s[s.index.isin(res)].reset_index(drop=True)

    elif inter=='d':
        s = glb.security.day_securities[stock_name][glb.security.day_securities[stock_name]['datetime']<glb.context.current_dt].tail(gap*count).reset_index(drop=True)
        if len(s)<1:
            return None
        id = len(s)-1
        while (id>=0 and cnt <count):
            res.append(id)
            cnt+=1
            id -= gap
        if cnt == 0:
            return None
        return s[s.index.isin(res)].reset_index(drop=True)
    else:
        return None

# 总金钱
def totalValue():
    stock_prices = []
    for stock_name in glb.security.securities.index:
        stock_prices.append(glb.security.get_current_price(stock_name, glb.context.current_dt))
    prices = Series(stock_prices, index=glb.security.securities.index)
    return glb.context.Value(prices)

# 基准金钱
def benchmarkValue():
    price = glb.security.get_current_price(glb.context.portfolio.benchmark.security,
                                           glb.context.current_dt)
    return glb.context.bmValue(price)

# 策略收益
def totalReturns():
    return (totalValue() - glb.g.tvalue0) / glb.g.tvalue0

# 基准收益
def benchmarkReturns():
    return (benchmarkValue() - glb.g.bvalue0) / glb.g.bvalue0

# 策略年化收益
def totalAnnualizedReturns():
    return (1+totalReturns())**(250/glb.g.days) - 1

# 基准年化收益
def benchmarkAnnualizedReturns():
    return (1+benchmarkReturns())**(250/glb.g.days) - 1

# 股数订单
def order(stock_name, amount):
    res =  glb.o.order(stock_name, amount)
    if glb.context.frequency=='day':
        glb.o.order_consume()
    return res

# 价格订单
def order_value(stock_name, value):
    res = glb.o.order_value(stock_name, value)
    if glb.context.frequency=='day':
        glb.o.order_consume()
    return res

# 目标股数订单
def order_target(stock_name, target_amount):
    res = glb.o.order_target(stock_name, target_amount)
    if glb.context.frequency=='day':
        glb.o.order_consume()
    return res

# 目标价格订单
def order_target_value(stock_name, target_value):
    res = glb.o.order_target_value(stock_name, target_value)
    if glb.context.frequency=='day':
        glb.o.order_consume()
    return res

# 设置股票池
def set_universe(universe):
    return glb.context.set_universe(universe)

# 设置基准度
def set_benchmark(bm_code):
    return glb.context.set_benchmark(bm_code)

# 设置初始现金
def set_startingCash(value):
    return glb.context.portfolio.set_starting_cash(value)

# 设置开始时间
def set_startDate(_datetime):
    return glb.context.set_startDate(_datetime)

# 设置结束时间
def set_endDate(_datetime):
    return glb.context.set_endDate(_datetime)

# 设置时间细度
def set_frequency(frequency):
    return glb.context.set_frequency(frequency)

if __name__=="__main__":
    glb.context.Changetime(datetime(2016,2,2))
    s = glb.security.security[glb.security.security['datetime']>glb.context.current_dt]
    print s.head()
