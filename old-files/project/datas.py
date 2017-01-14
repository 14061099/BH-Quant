
from datetime import datetime

class Context(object):
    def __init__(self,starting_cash):
        self.portfolio = Portfolio(starting_cash)
        self.current_dt = datetime.now()
        #previous_dt = datetime()
        self.universe = []

    def set_Universe(self,stock_names):
        for stock_name in stock_names:
            self.universe.append(stock_name)

    class run_params :
        def __init__(self,start_date,end_date,s_type='full',frequency='daily'):
            self.start_date=start_date
            self.end_date=end_date
            self.type = s_type
            self.frequency =frequency


class Portfolio(object):
    def __init__(self,starting_cash=10000):
        self.inout_cash = 0
        self.available_cash = starting_cash
        #self.locked_cash =
        #sefl.margin =
        self.total_value = starting_cash
        self.profits = 0
        self.starting_cash = starting_cash
        self.positions_value = 0

#class Stocks(object):

class Order(object):
    def __init__(self,amount,stock_name,is_buy=True):
        #self.status
        self.add_time=datetime.now()
        self.is_buy=is_buy
        self.amount=amount
        self.stock_name=stock_name
        #self.order_id
        #self.price
        #self.avg_cost

    def log(self):
        print "Order %d of %s "%(self.amount,self.stock_name)