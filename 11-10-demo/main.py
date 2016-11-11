#coding=utf-8
from bq import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from datas import *
import old
import new
from datetime import datetime
from buaaquant_hmm import stat_handle

status = False
context = Context(datetime(2016,5,3,9,31),datetime(2016,5,7,3,0))
security = Security(context)
#print security.security
o = OrderList(context,security)

hm_state_handle = stat_handle()

hm_state_handle.show_hmm()

html = open("./test.html","r")
html = html.read()


class  myMainWindow(QtWidgets.QMainWindow):
    def __init__(self , parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        f = open('old.py','r')
        ct = ''
        for line in f:
            ct = ct + line
        self.ui.CodeText.setPlainText(ct)
        f.close()

        self.ui.SaveButton.clicked.connect(self.saveCode)
        self.ui.SaveButton.clicked.connect(self.keyPressEvent)
        self.ui.ClearButton.clicked.connect(self.ui.CodeText.clear)
	self.ui.webView.setHtml(html,QtCore.QUrl("file:///home/hadoop/PycharmProjects/11-10/test.html"))

    def keyPressEvent(self, QKeyEvent):
        if type(QKeyEvent) == QtGui.QKeyEvent:
            if QKeyEvent.key() == QtCore.Qt.Key_Escape:
                self.close()
            elif QKeyEvent.key == (QtCore.Qt.Key_Control and QKeyEvent.Qt.Key_S):
                self.saveCode()

    def saveCode(self):
        global status
        status = True
        pyText = self.ui.CodeText.toPlainText()
        f = open('new.py','w')
        f.write(pyText)
        f.close()
	
def run():
    if status:
        reload(new)
        chosen_f = new
    else:
        chosen_f = old
    # 初始化
    chosen_f.initialize(context)
    # 开始回测
    print 'start ', context.current_dt
    backDate = []
    backYield = []
    while security.hasday(context.current_dt):  # 按日循环
        print '--in day loop',context.current_dt
        # 开盘前
        for p in context.portfolio.positions:
            p.Update()
        # 盘中
        for t in security.security[context.current_dt.strftime('%Y-%m-%d')]['datetime']:  # 按分钟循环
            print '--in minute loop',context.current_dt
            context.Changetime(t)  # 改变时间
            chosen_f.handle_data(context,o,hm_state_handle)
            # 处理订单:
            o.order_consume()
            backDate.append(t.strftime('%Y-%m-%d-%H-%M'))
            backYield.append(o.get_current_price(context.universe[0]) / context.portfolio.positions[0].avg_cost)
        # 取消所有未完成订单:
        o.order_reset()
        nxtday = security.next_day(context.current_dt)
        if nxtday is None:
            break
        else:
            flag = context.Changetime(nxtday)  # 计算下一天
            # 反应结果
            # 打印日志
    writeIndex(backDate, backYield)

def writeIndex(backDate, backYield):
    file = open('data.json', 'w')
    # file.write('{' + 'datetime : ' + str(backDate) + ',' + 'yeild : ' + str(backYield) + '}');
    file.write('{' + "\"datetime\" : " + '[')
    for i in xrange(0, len(backDate) - 1):
        file.write("\"" + backDate[i] + "\",")
    file.write("\"" + backDate[i] + "\" ] , \"yeild\" : [")

    for i in xrange(0, len(backYield) - 1):
        file.write(str(backYield[i]) + ",")
    file.write(str(backYield[i]))

    file.write(']}')
    file.close()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('Mario.png'))
    app.setStyle('fusion')
    mapp = myMainWindow()
    mapp.ui.RunButton.clicked.connect(run)
    mapp.show()
    sys.exit(app.exec_())
   


