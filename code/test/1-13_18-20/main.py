# -*- coding: utf-8 -*-
from glb import Global, set_o, set_security
import new
import old
from function import *
from security import Security
from orderlist import OrderList

def run():
    if status:
        chosen_f = new
    else:
        chosen_f = old
    # 开始回测
    first_date = Global.security.security.iloc[0].datetime
    if (Global.context.current_dt<first_date):
        Global.context.Changetime(first_date)  # 改变时间
    print 'start date:', Global.context.current_dt,"\n"
    print 'set benchmark: ', Global.context.portfolio.benchmark.security, ' , huice starts\n'
    bm_price = Global.security.get_current_price(Global.context.portfolio.benchmark.security, Global.context.current_dt)
    if (Global.context.init_benchmark(bm_price)==-1):
        print '\n@init benchmark error! program end@\n'
        exit(1)
    Global.g.tvalue0 = totalValue()
    Global.g.bvalue0 = benchmarkValue()
    if (Global.context.frequency=='day'):
        day_huice(chosen_f)
    else:
        minute_huice(chosen_f)
    chosen_f.show_info(Global.context, Global.g)
    #writeIndex(backDate, backYield)

def minute_huice(chosen_f):
    id2 = list(Global.security.security['datetime']).index(Global.context.current_dt)
    # backDate = []
    # backYield = []
    while (Global.context.hasday()):  # 按日循环
        Global.g.days += 1
        if (Global.g.days%50==0):
            print 'up to ',Global.context.current_dt
        # print '--in day loop',Global.context.current_dt
        # 开盘前
        for p in Global.context.portfolio.positions:
            p.Update()
        # 盘中
        # 权宜之计
        id1 = id2
        date1 = Global.security.security.iloc[id1].datetime
        id2 = id1
        date2 = Global.security.security.iloc[id2].datetime
        # while (id2<len(Global.security.security) and (date2-date1).days<1): # 报错用这个
        while (id2 < len(Global.security.security) and (date2.day == date1.day)):
            id2 += 1
            if (id2 < len(Global.security.security)):
                date2 = Global.security.security.iloc[id2].datetime
        # 权宜之计
        for i in range(id1, id2):  # 按分钟循环
            t = Global.security.security.iloc[i].datetime
            Global.context.Changetime(t)  # 改变时间
            # print '        --in minute loop',Global.context.current_dt
            chosen_f.handle_data(Global.context, Global.o, Global.g)
            # 处理订单:
            Global.o.order_consume()
            '''
            for pos in Global.context.portfolio.positions:
                print("%s amount is %d" % (pos.security,pos.total_amount))
            print ("")
            '''
            # backDate.append(t.strftime('%Y-%m-%d-%H-%M'))
            # backYield.append(o.security.get_current_price(context.universe[0]) / context.portfolio.positions[0].avg_cost)
            if (Global.context.frequency == 'day'):
                break
        for order in Global.o.Trades:
            Global.orderInfo.append(Global.o.Trades[order].toString())
        # 取消所有未完成订单:
        Global.o.order_reset()
        # 权宜之计
        # 计算下一天
        if (id2 < len(Global.security.security)):
            nxtday = Global.security.security.iloc[id2].datetime
            flag = Global.context.Changetime(nxtday)
        else:
            break
            # 反应结果
            # 打印日志
            # 权宜之计

def day_huice(chosen_f):
    for t in Global.security.day_security['datetime']:  # 按日循环
        #print t
        Global.context.Changetime(t)
        Global.g.days += 1
        if (Global.g.days%50==0):
            print 'up to ',Global.context.current_dt
        # print '--in day loop',context.current_dt
        # 开盘前
        for p in Global.context.portfolio.positions:
            p.Update()
        # 盘中
        old.handle_data(Global.context, Global.o, Global.g)
        # 处理订单:
        Global.o.order_consume()
        '''
        for pos in context.portfolio.positions:
            print("%s amount is %d" % (pos.security,pos.total_amount))
        print ("")
        '''
        for order in Global.o.Trades:
            Global.orderInfo.append(Global.o.Trades[order].toString())
        # 取消所有未完成订单:
        Global.o.order_reset()

def writeIndex(backDate, backYield):
    file = open('data.json', 'w')
    # file.write('{' + 'datetime : ' + str(backDate) + ',' + 'yeild : ' + str(backYield) + '}');
    file.write('{' + "\"datetime\" : " + '[')
    for i in xrange(0, len(backDate) - 1):
        file.write("\"" + backDate[i] + "\",")
    if (len(backDate)>0):
        file.write("\"" + backDate[len(backDate)-1] + "\" ] , \"yeild\" : [")
    else:
        file.write("] , \"yeild\" : [")
    for i in xrange(0, len(backYield) - 1):
        file.write(str(backYield[i]) + ",")
    if (len(backYield)>0):
        file.write(str(backYield[len(backYield)-1]))
    file.write(']}')
    file.close()

if __name__=="__main__":
    status = False
    if status:
        reload(new)
        chosen_f = new
    else:
        chosen_f = old
    # 初始化
    chosen_f.initialize(Global.context, Global.g)
    set_security(Security(Global.context))
    set_o(OrderList(Global.context, Global.security, Global.g))
    run()