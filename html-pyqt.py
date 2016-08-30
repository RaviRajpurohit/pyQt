import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
w = QTextBrowser()


w.insertHtml('<style>table{color:red;}</style><table><tr><td>1</td><td>hello</td></tr><tr><td>2</td><td>world</td></tr></table>')



w.show()
sys.exit(app.exec_())
