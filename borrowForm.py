# Form implementation generated from reading ui file 'borrowForm.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, cursor, bid, parent):
        super().__init__()
        self.cursor = cursor
        self.bid = bid
        self.parent = parent
        self.setupUi(self)
        self.initBorrowForm()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 70, 351, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.borrowSid = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.borrowSid.setObjectName("borrowSid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.borrowSid)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.borrowBid = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.borrowBid.setObjectName("borrowBid")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.borrowBid)
        self.dueDate = QtWidgets.QDateEdit(parent=self.formLayoutWidget)
        self.dueDate.setObjectName("dueDate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dueDate)
        self.borrowSure = QtWidgets.QPushButton(parent=Form)
        self.borrowSure.setGeometry(QtCore.QRect(290, 230, 81, 31))
        self.borrowSure.setObjectName("borrowSure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 设置预览书号不可编辑
        self.borrowBid.setReadOnly(True)
        self.borrowBid.setStyleSheet("background-color: #eee;")
        # 设置日期选择框只能选择当前日期之后的日期
        self.dueDate.setMinimumDate(QtCore.QDate.currentDate())
        # 设置默认日期为当前日期
        self.dueDate.setDate(QtCore.QDate.currentDate())
        # 确认预约按钮绑定事件
        self.borrowSure.clicked.connect(self.borrowBook)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "借阅表单"))
        self.label.setText(_translate("Form", "学   号："))
        self.label_2.setText(_translate("Form", "还书日期："))
        self.label_3.setText(_translate("Form", "书   号："))
        self.borrowSure.setText(_translate("Form", "确认借阅"))

    def initBorrowForm(self):
        self.borrowBid.setText(str(self.bid))

    def borrowBook(self):
        sid = self.borrowSid.text()
        dueDate = self.dueDate.text()
        bid = self.borrowBid.text()
        if sid == "" or dueDate == "":
            QtWidgets.QMessageBox.warning(self, "警告", "请填写完整信息")
            return
        # 调用存储过程
        try:
            self.cursor.callproc("borrowBook", (sid, bid, dueDate))
            QtWidgets.QMessageBox.information(self, "提示", "借阅成功")
            self.close()
            self.parent.searchBook()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "警告", e.args[1])
            return


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
    ui = Ui_Form(cursor, 1)
    ui.show()
    sys.exit(app.exec())
