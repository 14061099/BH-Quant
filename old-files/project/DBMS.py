import pymongo

class DBMS(object):

    def __init__(self,host,ip):
        self.__connect = pymongo.MongoClient(host,ip)

    def __connect_to_db(self,stock_name):
        if stock_name in self.__connect.database_names():
            self.__db = self.__connect.get_database(stock_name)
        else:
            raise Exception("Illegal database name,please check and re-try")

    def get_col(self,stock_name,col_name):
        self.__connect_to_db(stock_name)
        if col_name in self.__db.collection_names():
            self.__col = self.__db.get_collection(col_name)
            return self.__col
        else:
            raise Exception("Illegal collection name")

