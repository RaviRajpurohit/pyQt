import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("127.0.0.1")
db.setDatabaseName("new")
db.setUserName("root")
db.setPassword("internet")

w = QTextBrowser()


w.insertHtml('<style>div{color:red;}canvas{color:black;height:50px;width:10px;}</style><script></script><div><input type="button" value="new"></div>')



w.show()
sys.exit(app.exec_())
