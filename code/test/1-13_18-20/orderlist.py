# -*- coding: utf-8 -*-
from config import *
from datetime import datetime


def get_money(amount, price, is_buy=True):
    if (is_buy):
        fee = Config.open_commission() * amount * price
        if (fee < Config.min_commission()):
            fee = Config.min_commission()
        money = amount * price * (1 + Config.open_tax()) + fee
    else:
        fee = Config.close_commission() * amount * price
        if (fee < Config.min_commission()):
            fee = Config.min_commission()
        money = amount * price * (1 - Config.close_tax()) - fee
    return money

class Order(object):
    def __init__(self, date, amount, stock_name, price, total_money, is_buy=True):
        self.date = date
        self.is_buy = is_buy
        self.amount = amount
        self.stock_name = stock_name
        self.price = price
        self.total_money = total_money

    def toString(self):
        if self.is_buy==True:
            type="buy "
        else:
            type="sell "
        return self.date.strftime('%y-%m-%d %H:%M ') + type + self.stock_name + " ( " + str(self.price) + " , " + str(self.amount) + " ) " + str(self.total_money)


class OrderList(object):
    List = {}  # unfinished orders set , do not include the canceled orders
    Backup = {}  # orders set of all , do include the canceled orders
    i = 1  # index order id , first order's index is 1
    Trades = {}  # finished orders set

    def __init__(self, context,security,g):
        print "initializing orderlist"
        self.context = context
        self.security = security
        self.g = g

    def order(self, stock_name, amount):  # return id
        # 1-13 positions可变后，position可能不存在
        '''
        position = self.context.portfolio.get_position(stock_name)
        if amount + position.total_amount < 0:
            raise Exception("Illegal order amount , return -1")
        else:
        '''
        if amount>0:
            tmp = amount%100
            if int(tmp) != 0:
                amount = amount - tmp
                print "the amount of order ,%d,is changed to %d"%(amount+tmp,amount)
            if amount == 0:
                print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, amount, stock_name, price, self.get_money(amount, price,False), False)
            #o = Order(amount, stock_name, self.security.get_current_price(stock_name,self.context.current_dt), self.security.get_current_price(stock_name,self.context.current_dt),False),False)  # port
        else:
            amount = -amount
            tmp = amount % 100
            if int(tmp) != 0:
                amount = amount - tmp
                print "the amount of order ,%d,is changed to %d" % (amount + tmp, amount)
            if amount == 0:
                print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, amount, stock_name, price, self.get_money(amount, price, True), True)
            #o = Order(amount, stock_name, self.security.get_current_price(stock_name,self.context.current_dt), self.security.get_current_price(stock_name,self.context.current_dt),True),True)  # port
        self.List[self.i] = o
        self.Backup[self.i] = o
        self.i += 1
        return o

    def order_target(self, stock_name, amount):  # return id
        # 1-13 positions可变后，position可能不存在
        '''
        position = self.context.portfolio.get_position(stock_name)
        gap = amount - position.total_amount  # port
        if amount < 0:
            raise Exception("Illegal stock total amount, return -1")
        else:
        '''
        if stock_name not in self.context.portfolio.positions.index:
            pos_amount = 0
        else:
            pos_amount = self.context.portfolio.positions[stock_name].total_amount
        gap = amount - pos_amount  # port
        if gap >= 0:
            tmp = gap % 100
            if int(tmp) != 0:
                gap = gap - tmp
                #print "the amount of order ,%d,is changed to %d" % (gap + tmp, gap)
            if gap == 0:
                #print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, gap, stock_name, price, self.get_money(gap, price, True), True)
            #o = Order(gap, stock_name, self.security.get_current_price(stock_name,self.context.current_dt),self.get_money(gap,self.security.get_current_price(stock_name),True),True)  # port
        else:
            gap =-gap
            tmp = gap % 100
            if int(tmp) != 0:
                gap = gap - tmp
                #print "the amount of order ,%d,is changed to %d" % (gap + tmp, gap)
            if gap == 0:
                #print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, gap, stock_name, price, self.get_money(gap, price, False), False)
            #o = Order(-gap, stock_name, self.security.get_current_price(stock_name), self.get_money(-gap,self.security.get_current_price(stock_name),False),False)  # port
        self.List[self.i] = o
        self.Backup[self.i] = o
        self.i += 1
        return o

    def order_value(self, stock_name, value):  # return id
        # 1-13 positions可变后，position可能不存在
        '''
        position = self.context.portfolio.get_position(stock_name)
        if value + position.total_value < 0:
            raise Exception("Illegal order value , return -1")
        else:
        '''
        price = self.security.get_current_price(stock_name,self.context.current_dt)  # port
        if value >= 0:
            amount = value/price
            tmp = amount % 100
            if int(tmp) != 0:
                amount = amount - tmp
                #print "the amount of order ,%d,is changed to %d" % (amount + tmp, amount)
            if amount == 0:
                #print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, amount, stock_name, price, self.get_money(amount, price, True), True)
            #o = Order(amount, stock_name, self.security.get_current_price(stock_name,context.current_dt),self.get_money(amount,self.security.get_current_price(stock_name),True),True)  # port
        else:
            amount = -value/price
            tmp = amount % 100
            if int(tmp) != 0:
                amount = amount - tmp
                #print "the amount of order ,%d,is changed to %d" % (amount + tmp, amount)
            if amount == 0:
                #print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, amount, stock_name, price, self.get_money(amount, price, False), False)
            #o = Order(amount, stock_name, self.security.get_current_price(stock_name,self.context.current_dt), self.get_money(amount,self.security.get_current_price(stock_name,self.context.current_dt),False),False)  # port
        self.List[self.i] = o
        self.Backup[self.i] = o
        self.i += 1
        return o

    def order_target_value(self, stock_name, value):  # return id
        # 1-13 positions可变后，position可能不存在
        '''
        position = self.context.portfolio.get_position(stock_name)
        gap = value - position.total_value  # port
        price = self.security.get_current_price(stock_name,self.context.current_dt)  # port
        print '------price',price
        if value < 0:
            raise Exception("Illegal stock total value, return -1")
        else:
        '''
        price = self.security.get_current_price(stock_name, self.context.current_dt)  # port
        if stock_name not in self.context.portfolio.positions.index:
            pos_amount = 0
        else:
            pos_amount = self.context.portfolio.positions[stock_name].total_amount
        gap = value - price*pos_amount  # port
        if gap >= 0:
            amount = gap/price
            tmp = amount % 100
            if int(tmp) != 0:
                amount = amount - tmp
                #print "the amount of order ,%d,is changed to %d" % (amount + tmp, amount)
            if amount == 0:
                #print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, amount, stock_name, price, self.get_money(amount, price, True), True)
            #o = Order(amount, stock_name, self.security.get_current_price(stock_name,self.context.current_dt),self.security.get_current_price(stock_name,self.context.current_dt),True),True)  # port
        else:
            amount = -gap/price
            tmp = amount % 100
            if int(tmp) != 0:
                amount = amount - tmp
                #print "the amount of order ,%d,is changed to %d" % (amount + tmp, amount)
            if amount == 0:
                #print "the amount of order is %d and no valid order" % (tmp)
                return None
            # 1-12
            price = self.security.get_current_price(stock_name, self.context.current_dt)
            o = Order(self.context.current_dt, amount, stock_name, price, self.get_money(amount, price, False), False)
            #o = Order(amount, stock_name, self.security.get_current_price(stock_name,self.context.current_dt), self.security.get_current_price(stock_name,self.context.current_dt),False),False)  # port
        self.List[self.i] = o
        self.Backup[self.i] = o
        self.i += 1
        return o

    def cancel_order(self, o):  # return Order
        if o not in self.List:
            raise Exception("Order has been canceled or consumed. Can't cancel it !")
        else:
            self.List.pop(o)
            return o
        return None

    def get_open_orders(self):  # return dict(id,object)
        return self.List

    def get_orders(self):  # return dict(id,object)
        return self.Backup

    def get_trades(self):  # retur
        # n dict(id,object)
        return self.Trades

    def order_consume(self):  # consume orders
        pop_id = []
        for id in self.List.keys():
            # 11_22#
            flag = self.context.portfolio.Change(self.List[id])
            # 11_22#
            if (flag==0):
                pop_id.append(id)
                if self.List[id].is_buy:
                    type = "buy"
                else:
                    type = "sell"
                info = "day "+str(self.g.days)+" "+type+" "+str(self.List[id].amount)+","+str(self.List[id].total_money)
                self.g.orderInfo.append(info)
                self.Trades[id] = self.List[id]

        for i in pop_id:
            self.List.pop(i)

    def get_money(self,amount,money,is_buy):
        if(is_buy==True):
            fee = Config.open_commission() * amount * money
            if (fee < Config.min_commission()):
                fee = Config.min_commission()
            money = amount*money*(1+Config.open_tax())+ fee
        else:
            fee = Config.close_commission() * amount * money
            if (fee < Config.min_commission()):
                fee = Config.min_commission()
            money = amount*money*(1-Config.close_tax())-fee
        return money

    def order_reset(self):  # at the end of day , reset the order set
        self.List = {}
        self.Backup = {}
        self.Trades = {}
        self.i = 1

if __name__=="__main__":
    from glb import *
    ord = o.order_target(context.universe[0],0)
    print ord.toString()