# -*- coding: utf-8 -*-

from config import Config
from portfolio import Portfolio
from position import Position

class Context(object):  # 全局变量
    __slots__ = (
    '_portfolio', '_current_dt', '_previous_dt', '_universe', '_start_date', '_end_date',
    '_style', '_frequency', '_run_flag')

    def __init__(self):
        print "initializing context"
        self._universe = Config.stock_pool()  # 股票池
        self._portfolio = Portfolio(self._universe)  # 账户
        self._current_dt = Config.start_date()  # 当前时间
        self._previous_dt = None  # 前一个时间
        self._start_date = Config.start_date()   # 回测起时
        self._end_date = Config.end_date()   # 回测终时
        self._run_flag = False # 回测运行标志
        self._style = 'huice'  # ？？？
        self._frequency = 'day'  # 时间细度

    # set
    def set_run_flag(self):
        self._run_flag = True

    def set_benchmark(self, bm_code):
        if self._run_flag:
            return -1
        self._portfolio.set_benchmark(bm_code)
        return 0

    def set_universe(self, universe):
        if self._run_flag:
            return -1
        self._universe = universe
        return 0

    def set_startDate(self, _datetime):
        if self._run_flag:
            return -1
        if (_datetime<self._end_date):
            self._start_date = _datetime
            self._current_dt = _datetime
            return 0
        else:
            return -1

    def set_endDate(self, _datetime):
        if self._run_flag:
            return -1
        if (_datetime>self._start_date):
            self._end_date = _datetime
            return 0
        else:
            return -1

    def set_frequency(self, frequency):
        if self._run_flag:
            return -1
        self._frequency = frequency
        return 0

    # use value
    @property
    def portfolio(self):
        return self._portfolio

    @property
    def universe(self):
        return self._universe

    @property
    def current_dt(self):
        return self._current_dt

    @property
    def previous_dt(self):
        return self._previous_dt

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def style(self):
        return self._style

    @property
    def frequency(self):
        return self._frequency

    @property
    def run_flag(self):
        return self._run_flag

    # 方法
    def Changetime(self, t):
        self._previous_dt = self._current_dt
        self._current_dt = t
        return True

    def hasday(self):
        if (self._current_dt >= self._start_date and self._current_dt <= self._end_date):
            return True
        else:
            return False

    def Value(self, prices):
        return self._portfolio.Value(prices)

    def bmValue(self, price):
        return self._portfolio.bmValue(price)

    def init_benchmark(self, price):
        return self._portfolio.init_benchmark(price)
