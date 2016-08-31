import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from PyQt4.QtSql import *

db = None
class ForumValues(QWidget):
	layout = None
	def __init__(self, loginWindow):
		loginWindow.hide()
		layout = QFormLayout()
		
		if loginWindow.item == "Admin":
			print "admin"
			
			self.accountHolder = QLineEdit("Select from Account Type")
			self.accountHolder.setReadOnly(True)
			layout.addRow(self.accountHolder)
			
			self.adminLogin()
			
		else:
			print "employee"
			self.p_word = QLineEdit()
			self.p_word.setEchoMode(QLineEdit.Password)
			self.p_word.setPlaceholderText("Enter Password")
			#self.p_word.textChanged.connect(self.getPassword)
			layout.addRow("Password",self.p_word)
			
			self.employeeLogin()
			
		
		
		QWidget.__init__(self)
		self.setLayout(layout)
		self.setWindowTitle("Login as "+loginWindow.item)
	def adminLogin(self):
		print "admin function"
		
	def employeeLogin(self):
		print "employee function"
		
		


class AccountType(QWidget):
	print "show"
	item = None
	username = None
	password = None
	
	def __init__(self, parent = None):
		super(AccountType, self).__init__(parent)
		self.show()
		layout = QFormLayout()

		self.accountHolder = QLineEdit("Select from Account Type")
		
		self.accountHolder.setReadOnly(True)
		self.accountType = QPushButton("Account Type")
      		self.accountType.clicked.connect(self.getAccount)
		layout.addRow(self.accountType,self.accountHolder)

		self.u_name = QLineEdit()
		self.u_name.setPlaceholderText("Enter username")
		self.u_name.textChanged.connect(self.getUsername)
		layout.addRow("Username",self.u_name)

		self.p_word = QLineEdit()
   		self.p_word.setEchoMode(QLineEdit.Password)
		self.p_word.setPlaceholderText("Enter Password")
		self.p_word.textChanged.connect(self.getPassword)
   		layout.addRow("Password",self.p_word)
		
		self.login = QPushButton("Login")
      		self.login.clicked.connect(self.logIn)
		layout.addRow(self.login)

		self.setLayout(layout)
      		self.setWindowTitle("Account Login")
		

	def getAccount(self):
		items = ("Admin", "Employee")

		self.item, ok = QInputDialog.getItem(self, "select Account Type", 
		 "list of Accounts", items, 0, False)		
		if ok and self.item:
			self.accountHolder.setText(self.item)


	def getUsername(self,text):
		self.username = text

	def getPassword(self,text):
		self.password = text
		
	def logIn(self):
		query = QSqlQuery ("""SELECT Username, Password FROM login WHERE `Account Type` = "%s" """%(str(self.item)))   
		query.next()
		#if ((self.username != query.value(0).toString()) and (self.password != query.value(0).toString())):
		#print query.value(0).toString(), query.value(1).toString()
		if True:
			self.forum = ForumValues(self)
			self.forum.show()
			



def main():
	db.setHostName("127.0.0.1")
    	db.setDatabaseName("python")
    	db.setUserName("root")
	db.setPassword("internet")
	if (db.open()==False):     
      		QMessageBox.critical(None, "Database Error",
			db.lastError().text()) 

	app = QApplication(sys.argv)
	ex = AccountType()
	#ex.show()
	sys.exit(app.exec_())



if __name__ == '__main__':
	db = QSqlDatabase.addDatabase("QMYSQL")
   	main()
