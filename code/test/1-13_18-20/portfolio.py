# -*- coding: utf-8 -*-

from config import Config
from position import Position
from pandas import Series
from datetime import datetime

class Portfolio(object):  # 个体
    __slots__ = (
    '_starting_cash', '_cash', '_available_cash', '_locked_cash', '_positions',
    '_total_value', '_positions_value', '_benchmark', '_bm_cash')

    def __init__(self,universe):
        self._starting_cash = Config.starting_cash()
        self._cash = self._starting_cash
        self._available_cash = self._cash
        self._bm_cash = self._starting_cash
        self._locked_cash = 0
        self._positions = Series([])
        '''
        p = []
        for name in universe:
            p.append(Position(name))
        self._positions = Series(p, index=universe)
        '''
        self._benchmark = Position(Config.benchmark())  # 基准


    @property
    def starting_cash(self):
        return self.starting_cash

    @property
    def cash(self):
        return self._cash

    @property
    def available_cash(self):
        return self._available_cash

    @property
    def locked_cash(self):
        return self._locked_cash

    @property
    def positions(self):
        return self._positions

    @property
    def benchmark(self):
        return self._benchmark

    def get_position(self, stock_name):
        return self._positions[stock_name]
    # 11_22#
    def Change(self,order):
        money = order.total_money
        if(order.is_buy==True): # 买入
            type = ' sub '
            if(self._available_cash<money):
                #print("don't have enough money %d,%d,%d" % (self._available_cash,money, order.price))
                return -1
            # 1-13 仓位个数变化
            if order.stock_name not in self._positions.index:
                new_pos = Series(Position(order.stock_name), index=[order.stock_name])
                self._positions = self._positions.append(new_pos)
            flg = self._positions[order.stock_name].Change(order)
            if(flg!=0):
                return -1
            self._available_cash -= money
            self._cash -= money
        else: # 卖出
            type = ' add '
            flg = self._positions[order.stock_name].Change(order)
            if(flg!=0):
                return -1
            # 1-13 仓位个数变化
            if self._positions[order.stock_name].total_amount==0:
                self._positions = self._positions.drop(order.stock_name)
            self._available_cash += money
            self._cash += money
        return 0

    def add_available_cash(self,num):
        self._available_cash += num

    def minus_available_cash(self,num):
        self._available_cash -= num

    def get_profit(self):
        return self._available_cash+self._positions.total_value()-self._starting_cash
    # 11_22#

    # 1-12
    def Value(self,prices):
        _index=[]
        amount=[]
        for p in self._positions:
            _index.append(p.security)
            amount.append(p.total_amount)
        s = Series(amount, index=_index)
        s = (s * prices).dropna(how='any')
        res = 0
        for i in s:
            res += i
        if (isinstance(res,float)):
            return res + self._cash
        else:
            return self._cash


    # 1-13
    def bmValue(self, price):
        return self._benchmark.total_amount * price + self._bm_cash

    def set_benchmark(self, bm_code):
        self._benchmark = Position(bm_code)
        return 0

    def set_starting_cash(self,value):
        if value<=0:
            return -1
        self._starting_cash = value
        self._cash = self._starting_cash
        self._available_cash = self._cash
        self._bm_cash = self._starting_cash
        return 0

    def init_benchmark(self, price):
        from orderlist import Order, get_money
        amount = int(self._starting_cash / price) / Config.order_amount_base() * Config.order_amount_base()
        date = datetime.now()
        order = Order(date, amount, self._benchmark.security, price, get_money(amount,price))
        flag = self._benchmark.Change(order)
        self._bm_cash -= get_money(amount,price)
        self._benchmark.Update()
        return flag


if __name__=="__main__":
    s1 = Series([1,2,33,4], index=[0,1,2,3])
    s2 = Series([1,-1,1], index=[0,1,3])
    s3 = s1.mul(s2)
    print s3