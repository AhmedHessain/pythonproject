import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class login(QDialog):
	def __init__(self):
		super(login,self).__init__()
		loadUi("login.ui",self)
		self.loginbutton.clicked.connect(self.loginfunction)
		self.password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.username.setPlaceholderText("              Username")
		self.password.setPlaceholderText("              Password")
		self.createaccountbutton.clicked.connect(self.signupfunction)
	def loginfunction(self):
		userName=self.username.text()
		passWord=self.password.text()
		print("Successfully username: " , userName , "and password: " , passWord)
	def signupfunction(self):
		createAccount=signup()
		widget.addWidget(createAccount)
		widget.setCurrentIndex(widget.currentIndex()+1)

class signup(QDialog):
	def __init__(self):
		super(signup,self).__init__()
		loadUi("Sign Up.ui",self)
		self.signupbutton.clicked.connect(self.signupfunction)
		self.loginherebutton.clicked.connect(self.loginherefunction)
		self.password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
		self.username.setPlaceholderText("              Username")
		self.password.setPlaceholderText("              Password")
		self.confirmpassword.setPlaceholderText("        Confirm Password")
		self.email.setPlaceholderText("                 E-mail")

	def signupfunction(self):
		userName=self.username.text()
		passWord=self.password.text()
		confirmPassWord=self.confirmpassword.text()
		email=self.email.text()
		if passWord==confirmPassWord:
			print("congrats you have an acoount,", userName , "password" , passWord ,"email",email)
		else:
			print("password is not the same")

	def loginherefunction(self):
		loginHere=login()
		widget.addWidget(loginHere)
		widget.setCurrentIndex(widget.currentIndex()+1)
app=QApplication(sys.argv)
mainWindow=signup()
widget=QtWidgets.QStackedWidget()
widget.setFixedWidth(900)
widget.setFixedHeight(1200)
widget.addWidget(mainWindow)
widget.show()
app.exec_()