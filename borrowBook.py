# Form implementation generated from reading ui file 'borrowBook.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, cursor):
        super().__init__()
        self.cursor = cursor
        self.setupUi(self)
        self.initBookTable()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.BookTable = QtWidgets.QTableWidget(parent=Form)
        self.BookTable.setGeometry(QtCore.QRect(40, 111, 721, 211))
        self.BookTable.setObjectName("BookTable")
        self.BookTable.setColumnCount(4)
        self.BookTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BookTable.setHorizontalHeaderItem(3, item)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 721, 71))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 53, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 53, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(340, 30, 53, 15))
        self.label_3.setObjectName("label_3")
        self.searchSure = QtWidgets.QPushButton(parent=self.groupBox)
        self.searchSure.setGeometry(QtCore.QRect(640, 20, 81, 31))
        self.searchSure.setObjectName("searchSure")
        self.selectBid = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectBid.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.selectBid.setObjectName("selectBid")
        self.selectBname = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectBname.setGeometry(QtCore.QRect(230, 30, 91, 21))
        self.selectBname.setObjectName("selectBname")
        self.selectAuthor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectAuthor.setGeometry(QtCore.QRect(390, 30, 91, 21))
        self.selectAuthor.setObjectName("selectAuthor")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(500, 30, 53, 15))
        self.label_4.setObjectName("label_4")
        self.selectStatus = QtWidgets.QComboBox(parent=self.groupBox)
        self.selectStatus.setGeometry(QtCore.QRect(550, 30, 69, 22))
        self.selectStatus.setObjectName("selectStatus")
        self.selectStatus.addItem("")
        self.selectStatus.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 330, 721, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.viewBid = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.viewBid.setObjectName("viewBid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.viewBid)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.viewBname = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.viewBname.setObjectName("viewBname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.viewBname)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.viewAuthor = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.viewAuthor.setObjectName("viewAuthor")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.viewAuthor)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.viewPublisher = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.viewPublisher.setObjectName("viewPublisher")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.viewPublisher)
        self.viewCover = QtWidgets.QGraphicsView(parent=self.groupBox_2)
        self.viewCover.setGeometry(QtCore.QRect(350, 20, 181, 161))
        self.viewCover.setObjectName("viewCover")
        self.borrowSure = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.borrowSure.setGeometry(QtCore.QRect(640, 150, 81, 31))
        self.borrowSure.setObjectName("borrowSure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.searchSure.clicked.connect(self.searchBook)
        self.BookTable.clicked.connect(self.viewBook)
        self.viewBid.setReadOnly(True)
        self.viewBname.setReadOnly(True)
        self.viewAuthor.setReadOnly(True)
        self.viewPublisher.setReadOnly(True)
        self.viewBid.setStyleSheet("background-color: #eee;")
        self.viewBname.setStyleSheet("background-color: #eee;")
        self.viewAuthor.setStyleSheet("background-color: #eee;")
        self.viewPublisher.setStyleSheet("background-color: #eee;")
        self.borrowSure.clicked.connect(self.borrowBook)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "借阅图书"))
        item = self.BookTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "编号"))
        item = self.BookTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "书名"))
        item = self.BookTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "作者"))
        item = self.BookTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "出版社"))
        self.groupBox.setTitle(_translate("Form", "筛选"))
        self.label.setText(_translate("Form", "编   号："))
        self.label_2.setText(_translate("Form", "书   名："))
        self.label_3.setText(_translate("Form", "作   者："))
        self.searchSure.setText(_translate("Form", "搜索"))
        self.label_4.setText(_translate("Form", "状   态："))
        self.selectStatus.setItemText(0, _translate("Form", "已预约"))
        self.selectStatus.setItemText(1, _translate("Form", "在馆"))
        self.groupBox_2.setTitle(_translate("Form", "预览"))
        self.label_5.setText(_translate("Form", "编   号："))
        self.label_6.setText(_translate("Form", "书   名："))
        self.label_7.setText(_translate("Form", "作   者："))
        self.label_8.setText(_translate("Form", "出版社："))
        self.borrowSure.setText(_translate("Form", "借阅"))

    def initBookTable(self):
        self.BookTable.setRowCount(0)
        self.cursor.execute("select bid, bname, author, publisher from book where status = 1")
        data = self.cursor.fetchall()
        for i in range(len(data)):
            self.BookTable.insertRow(i)
            for j in range(4):
                self.BookTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))
        self.BookTable.verticalHeader().setVisible(False)
        self.BookTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.BookTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def searchBook(self):
        bid = self.selectBid.text()
        bname = self.selectBname.text()
        author = self.selectAuthor.text()
        # 选择的状态
        status = self.selectStatus.currentText()
        if status == "在馆":
            status = 0
        elif status == "已预约":
            status = 1
        # print(bid, bname, author, status)
        self.BookTable.setRowCount(0)
        sql = "select bid, bname, author, publisher from book where bid like '%{}%' and bname like '%{}%' and author like '%{}%' and status = {}".format(bid, bname, author, status)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        data = self.cursor.fetchall()
        for i in range(len(data)):
            self.BookTable.insertRow(i)
            for j in range(4):
                self.BookTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))

    def viewBook(self):
        row = self.BookTable.currentRow()
        bid = self.BookTable.item(row, 0).text()
        sql = "select * from book where bid = {}".format(bid)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        self.viewBid.setText(str(data[0]))
        self.viewBname.setText(data[2])
        self.viewAuthor.setText(data[3])
        self.viewPublisher.setText(data[4])
        cover = QtGui.QPixmap('./img/' + data[1]).scaled(self.viewCover.width() - 10, self.viewCover.height() - 10)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(cover)
        self.viewCover.setScene(scene)

    def borrowBook(self):
        bid = self.viewBid.text()
        from borrowForm import Ui_Form
        self.borrowForm = Ui_Form(self.cursor, bid)
        self.borrowForm.show()


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
    ui = Ui_Form(cursor)
    ui.show()
    sys.exit(app.exec())