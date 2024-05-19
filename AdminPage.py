# Form implementation generated from reading ui file 'AdminPage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, cursor, username):
        super(Ui_MainWindow, self).__init__()
        self.cursor = cursor
        self.username = username
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addReserve = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addReserve.setGeometry(QtCore.QRect(320, 150, 101, 51))
        self.addReserve.setObjectName("addReserve")
        self.addBorrow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addBorrow.setGeometry(QtCore.QRect(320, 250, 101, 51))
        self.addBorrow.setObjectName("addBorrow")
        self.addReturn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addReturn.setGeometry(QtCore.QRect(320, 350, 101, 51))
        self.addReturn.setObjectName("addReturn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        # 设置状态栏内容
        mylabel = QtWidgets.QLabel()
        mylabel.setText("欢迎您，管理员" + self.username + "！")
        self.statusbar.addWidget(mylabel)

        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.BookManage = QtWidgets.QMenu(parent=self.menubar)
        self.BookManage.setObjectName("BookManage")
        self.StudentManage = QtWidgets.QMenu(parent=self.menubar)
        self.StudentManage.setObjectName("StudentManage")
        self.BadGuy = QtWidgets.QMenu(parent=self.menubar)
        self.BadGuy.setObjectName("BadGuy")
        self.AccountManage = QtWidgets.QMenu(parent=self.menubar)
        self.AccountManage.setObjectName("AccountManage")
        MainWindow.setMenuBar(self.menubar)
        self.addBook = QtGui.QAction(parent=MainWindow)
        self.addBook.setObjectName("addBook")
        self.alterBook = QtGui.QAction(parent=MainWindow)
        self.alterBook.setObjectName("alterBook")
        self.addStudent = QtGui.QAction(parent=MainWindow)
        self.addStudent.setObjectName("addStudent")
        self.alterStudent = QtGui.QAction(parent=MainWindow)
        self.alterStudent.setObjectName("alterStudent")
        self.badReserve = QtGui.QAction(parent=MainWindow)
        self.badReserve.setObjectName("badReserve")
        self.badBorrow = QtGui.QAction(parent=MainWindow)
        self.badBorrow.setObjectName("badBorrow")
        self.alterProfile = QtGui.QAction(parent=MainWindow)
        self.alterProfile.setObjectName("alterProfile")
        self.logOut = QtGui.QAction(parent=MainWindow)
        self.logOut.setObjectName("logOut")
        self.alterPassword = QtGui.QAction(parent=MainWindow)
        self.alterPassword.setObjectName("alterPassword")
        self.BookManage.addAction(self.addBook)
        self.BookManage.addAction(self.alterBook)

        # 图书管理菜单栏绑定事件
        self.BookManage.triggered.connect(self.manageBook)

        self.StudentManage.addAction(self.addStudent)
        self.StudentManage.addAction(self.alterStudent)

        # 学生管理菜单栏绑定事件
        self.StudentManage.triggered.connect(self.manageStudent)

        self.BadGuy.addAction(self.badReserve)
        self.BadGuy.addAction(self.badBorrow)
        self.AccountManage.addAction(self.alterProfile)
        self.AccountManage.addAction(self.alterPassword)
        self.AccountManage.addAction(self.logOut)

        # 账户管理菜单栏绑定事件
        self.AccountManage.triggered.connect(self.manageAccount)

        self.menubar.addAction(self.BookManage.menuAction())
        self.menubar.addAction(self.StudentManage.menuAction())
        self.menubar.addAction(self.BadGuy.menuAction())
        self.menubar.addAction(self.AccountManage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 预约图书按钮绑定事件
        self.addReserve.clicked.connect(self.reserveBook)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "管理页面"))
        self.addReserve.setText(_translate("MainWindow", "预约图书"))
        self.addBorrow.setText(_translate("MainWindow", "借阅图书"))
        self.addReturn.setText(_translate("MainWindow", "归还图书"))
        self.BookManage.setTitle(_translate("MainWindow", "图书管理"))
        self.StudentManage.setTitle(_translate("MainWindow", "学生管理"))
        self.BadGuy.setTitle(_translate("MainWindow", "违期管理"))
        self.AccountManage.setTitle(_translate("MainWindow", "账号设置"))
        self.addBook.setText(_translate("MainWindow", "添加图书"))
        self.alterBook.setText(_translate("MainWindow", "图书信息维护"))
        self.addStudent.setText(_translate("MainWindow", "添加学生"))
        self.alterStudent.setText(_translate("MainWindow", "学生信息维护"))
        self.badReserve.setText(_translate("MainWindow", "预约信息"))
        self.badBorrow.setText(_translate("MainWindow", "借阅信息"))
        self.alterProfile.setText(_translate("MainWindow", "修改资料"))
        self.logOut.setText(_translate("MainWindow", "退出登录"))
        self.alterPassword.setText(_translate("MainWindow", "修改密码"))

    # 图书管理菜单栏
    def manageBook(self, m):
        if m.text() == "添加图书":
            from addBook import Ui_Form
            self.addBook = Ui_Form(self.cursor)
            self.addBook.show()
        elif m.text() == "图书信息维护":
            from alterBook import Ui_Form
            self.alterBook = Ui_Form(self.cursor)
            self.alterBook.show()

    def manageStudent(self, m):
        if m.text() == "学生信息维护":
            from alterStudent import Ui_Form
            self.alterStudent = Ui_Form(self.cursor)
            self.alterStudent.show()

    def manageAccount(self, m):
        if m.text() == "修改资料":
            from alterProfile import Ui_Form
            self.alterProfile = Ui_Form(self.cursor, self.username)
            self.alterProfile.show()
        elif m.text() == "修改密码":
            from alterPassword import Ui_Form
            self.alterPassword = Ui_Form(self.cursor, self.username)
            self.alterPassword.show()
        elif m.text() == "退出登录":
            # 回到登录页面
            from Login import Ui_Form
            self.login = Ui_Form(self.cursor)
            self.login.show()
            self.close()


    # 预约图书
    def reserveBook(self):
        # 打开reserveBook页面
        from reserveBook import Ui_Form
        self.reserveBook = Ui_Form(self.cursor)
        self.reserveBook.show()


if __name__ == "__main__":
    import sys
    import pymysql
    app = QtWidgets.QApplication(sys.argv)
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="10086",
        database="library",
        charset="utf8"
    )
    cursor = db.cursor()
    ui = Ui_MainWindow(cursor, "admin1")
    ui.show()
    sys.exit(app.exec())
