# -*- coding: utf-8 -*-

from datetime import datetime

class Config(object):  # 常量，其中变量不允许在回测运行后修改
    @staticmethod
    def starting_cash():
        return 100000

    @staticmethod
    def stock_pool():
        return ['SH600000']

    @staticmethod
    def benchmark():
        return 'SH600000'
    # 1-10#
    @staticmethod
    def open_commission(): # buy
        return 0.0003

    @staticmethod
    def close_commission():  # push
        return 0.0003

    @staticmethod
    def min_commission():
        return 5

    @staticmethod
    def close_today_commission():
        return 0

    @staticmethod
    def open_tax():#buy
        return 0

    @staticmethod
    def close_tax():#push
        return 0.001
# 1-10#

    @staticmethod
    def start_date():
        return datetime(2016,1,1,9,31)

    @staticmethod
    def end_date():
        return datetime(2016,2,2)

    @staticmethod
    def order_amount_base():
        return 100