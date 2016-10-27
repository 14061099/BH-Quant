from bq import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from datas import Context
import Query
import x
import new

context = Context(10000)
status = False
rp = context.run_params('2016.2.1.9.35','2016.2.1.9.40')

class  myMainWindow(QtWidgets.QMainWindow):
    def __init__(self , parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        f = open('x.py','r')
        ct = ''
        for line in f:
            ct = ct + line
        self.ui.CodeText.setPlainText(ct)
        f.close()

        self.ui.SaveButton.clicked.connect(self.saveCode)
        self.ui.SaveButton.clicked.connect(self.keyPressEvent)
        self.ui.ClearButton.clicked.connect(self.ui.CodeText.clear)

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
    print status
    if status:
        reload(new)
        m = new
    else:
        m = x
    m.initialize(context)
    query = Query.Query('localhost',27017)
    data = query.get_price('gupiao',context.universe[0],rp.start_date,rp.end_date,'money')
    i = 0
    while i < len(data):
        m.handle_data(context,data,i)
        i+=1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('Mario.png'))
    app.setStyle('fusion')
    app.setStyle('fusion')
    mapp = myMainWindow()
    mapp.ui.RunButton.clicked.connect(run)
    mapp.show()
    sys.exit(app.exec_())




