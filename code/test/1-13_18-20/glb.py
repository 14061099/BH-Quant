from context import Context
from config import Config
from security import Security
from orderlist import OrderList

class glb(object):
    flag = False
    days = 0
    orderInfo = []
    tvalue0 = 0
    bvalue0 = 0
class Global:
    g = glb()
    context = Context()
    security = None
    o = None
    orderInfo = []

def set_context(c):
    Global.context = c

def get_context(c):
    return Global.context

def set_security(s):
    Global.security = s

def get_security():
    return Global.security

def set_o(o):
    Global.o = o

def get_o():
    return Global.o