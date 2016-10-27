from DBMS import DBMS

from datetime import datetime

class Query(object):
    def __init__(self,host,ip):
        self.dbms = DBMS(host,ip)
        self.min_year = 1995
        self.max_year = 2016

#start_date and end_date are string format like '2016.2.15.10.45'
#fields is one of []
    def get_price(self,stock_name,col_name,start_date=None,end_date=None,fields=None):
        start = start_date.split('.')
        end = end_date.split('.')
        if len(start) != 5 and len(end) != 5:
            raise Exception("Illegal date format")

        s_year=int(start[0])
        s_month=int(start[1])
        s_day=int(start[2])
        s_hour=int(start[3])
        s_minute=int(start[4])
        s_datetime = datetime(s_year,s_month,s_day,s_hour,s_minute)

        e_year = int(end[0])
        e_month = int(end[1])
        e_day = int(end[2])
        e_hour = int(end[3])
        e_minute = int(end[4])
        e_datetime = datetime(e_year, e_month, e_day, e_hour, e_minute)

        if s_year != e_year:
            raise Exception("start year and end year must be the same")

        if s_datetime>e_datetime:
            raise Exception("start time should not be later than end time")

        if s_year < self.min_year or e_year > self.max_year :
            raise Exception("query time out of range")


        col = self.dbms.get_col(stock_name,col_name)
        result = col.find({
            'year' : s_year,
            'month' : {'$gte':s_month , '$lte':e_month},
            'day' : {'$gte':s_day , '$lte':e_day},
            'hour' : {'$gte':s_hour , '$lte':e_hour},
            'minute' : {'$gte':s_minute ,'$lte':e_minute}
        })

        if fields == None:
            return result
        else:
            tmp = []
            for doc in result:
                tmp.append(doc.get(fields))
            return tmp
