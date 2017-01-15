# -*- coding: utf-8 -*-
import random

def initialize(context):
    stocks = ['SZ399305']
    context.set_universe(stocks)

def handle_data(context,o):
    for pos in context.portfolio.positions:
        stat = random.random()
        if (stat < 0.5):
            o.order(pos.security,10)
            print ('%s buy %d, now %d ' % (pos.security,10, pos.total_amount))
        elif (stat > 0.6):
            o.order(pos.security,10,style="sell")
            print ('%s sell %d, now %d ' % (pos.security, 10, pos.total_amount))
    return 0