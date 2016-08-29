import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget() 
# Set window size.
w.resize(1100, 1100)
# Set window title
w.setWindowTitle("Forum")

# Create user list
userList = QComboBox(w)
userList.addItem("--select--")
userList.addItem("Admin")
userList.addItem("Employee")
userList.move(10,10)




# Create textbox
name = QLineEdit(w)
name.move(20, 60)
name.resize(200,30)
name.setPlaceholderText ("Name")

fname = QLineEdit(w)
fname.move(20, 100)
fname.resize(200,30)
fname.setPlaceholderText ("Father's Name")

mname = QLineEdit(w)
mname.move(20, 140)
mname.resize(200,30)
mname.setPlaceholderText ("Mother's Name")

email = QLineEdit(w)
email.move(20, 180)
email.resize(200,30)
email.setPlaceholderText ("E-Mail ID")

contact = QLineEdit(w)
contact.move(20, 220)
contact.resize(200,30)
contact.setPlaceholderText ("Contact No")















# Create a button in the window
btn = QPushButton('submit', w)
# Create the actions
@pyqtSlot()
def on_click():
    print('submited')

btn.move(10,1060)
# connect the signals to the slots
btn.clicked.connect(on_click)




# Show window
w.show()
 
sys.exit(a.exec_())
