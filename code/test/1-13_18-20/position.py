# -*- coding: utf-8 -*-

from orderlist import Order

class Position(object):  # 仓位
    __slots__ = ('_security', '_price', '_avg_cost', '_total_amount', '_available_amount', '_locked_amount')

    def __init__(self, stock_name):
        self._security = stock_name
        self._price = 0
        self._avg_cost = None
        self._total_amount = 0
        self._available_amount = 0
        self._locked_amount = 0

    @property
    def security(self):
        return self._security

    @property
    def price(self):
        return self._price

    @property
    def avg_cost(self):
        return self._avg_cost

    @property
    def total_amount(self):
        return self._total_amount

    @property
    def available_amount(self):
        return self._available_amount

    @property
    def locked_amount(self):
        return self._locked_amount

    @property
    def total_value(self):
        return self._price * self._total_amount

    def Change(self, order):  # 订单对仓位的改变,成功返回0
        if isinstance(order, Order):
            if order.stock_name != self._security:
                #print('Position received an invalid parameter:an order with no connection(%s,%s)' % ( \
                #self._security, order.stock_name))
                return -1
            elif (order.is_buy == True ):
                # i need to know the buy-in price to update data (price,avg_cost)
                self._total_amount += order.amount
                self._locked_amount += order.amount
                if (self._avg_cost is None):
                    self._avg_cost = order.price
                elif (self._total_amount+order.amount==0):
                    self._avg_cost = self._avg_cost
                else:
                    self._avg_cost = (self.avg_cost*self._total_amount+order.price*order.amount)/(self._total_amount+order.amount)

                return 0
            else :
                if self._available_amount < order.amount:
                    #print('Position received an invalid parameter:an order with over-much amount(%d,%d)' % ( \
                    #self._available_amount, order.amount))
                    return -1
                else:
                    self._available_amount -= order.amount
                    self._total_amount -= order.amount

                    return 0
        else:
            print 'Position received a non-Order parameter'
            return -1

    def Update(self):  # 一天结束对仓位数据的检查和刷新，正常返回0
        # check
        if (self._price < 0 or (self._avg_cost < 0 and self._avg_cost is not None) or self._total_amount < 0 or self._available_amount < 0 or self._locked_amount < 0):
            print('Position occur an error: data < 0')
            return -1
        if (self._total_amount != self._available_amount + self._locked_amount):
            print('Position occur an error: data mess')
            return -1
        # flush
        self._available_amount = self._total_amount
        self._locked_amount = 0
        return 0
