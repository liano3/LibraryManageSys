# Form implementation generated from reading ui file 'Manage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, cursor, sid=None):
        super().__init__()
        self.cursor = cursor
        self.sid = sid
        self.setupUi(self)
        self.initTable()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 741, 331))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 53, 15))
        self.label.setObjectName("label")
        self.RselectSid = QtWidgets.QLineEdit(parent=self.groupBox)
        self.RselectSid.setGeometry(QtCore.QRect(70, 30, 113, 21))
        self.RselectSid.setObjectName("RselectSid")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 53, 15))
        self.label_2.setObjectName("label_2")
        self.RselectBid = QtWidgets.QLineEdit(parent=self.groupBox)
        self.RselectBid.setGeometry(QtCore.QRect(260, 30, 113, 21))
        self.RselectBid.setObjectName("RselectBid")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 53, 15))
        self.label_3.setObjectName("label_3")
        self.RselectStatus = QtWidgets.QComboBox(parent=self.groupBox)
        self.RselectStatus.setGeometry(QtCore.QRect(450, 30, 69, 22))
        self.RselectStatus.setObjectName("RselectStatus")
        self.RselectStatus.addItem("")
        self.RselectStatus.addItem("")
        self.RselectStatus.addItem("")
        self.RselectSure = QtWidgets.QPushButton(parent=self.groupBox)
        self.RselectSure.setGeometry(QtCore.QRect(640, 20, 81, 31))
        self.RselectSure.setObjectName("RselectSure")
        self.RTable = QtWidgets.QTableWidget(parent=self.groupBox)
        self.RTable.setGeometry(QtCore.QRect(20, 70, 701, 211))
        self.RTable.setObjectName("RTable")
        self.RTable.setColumnCount(5)
        self.RTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.RTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RTable.setHorizontalHeaderItem(4, item)
        self.Rcancel = QtWidgets.QPushButton(parent=self.groupBox)
        self.Rcancel.setGeometry(QtCore.QRect(640, 290, 81, 31))
        self.Rcancel.setObjectName("Rcancel")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 370, 741, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 53, 15))
        self.label_4.setObjectName("label_4")
        self.BselectSid = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.BselectSid.setGeometry(QtCore.QRect(70, 30, 113, 21))
        self.BselectSid.setObjectName("BselectSid")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(210, 30, 53, 15))
        self.label_5.setObjectName("label_5")
        self.BselectBid = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.BselectBid.setGeometry(QtCore.QRect(260, 30, 113, 21))
        self.BselectBid.setObjectName("BselectBid")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(400, 30, 53, 15))
        self.label_6.setObjectName("label_6")
        self.BselectStatus = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.BselectStatus.setGeometry(QtCore.QRect(450, 30, 69, 22))
        self.BselectStatus.setObjectName("BselectStatus")
        self.BselectStatus.addItem("")
        self.BselectStatus.addItem("")
        self.BselectStatus.addItem("")
        self.BselectSure = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.BselectSure.setGeometry(QtCore.QRect(640, 20, 81, 31))
        self.BselectSure.setObjectName("BselectSure")
        self.BTable = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.BTable.setGeometry(QtCore.QRect(20, 70, 701, 231))
        self.BTable.setObjectName("BTable")
        self.BTable.setColumnCount(5)
        self.BTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.BTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BTable.setHorizontalHeaderItem(4, item)
        self.Bkeep = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.Bkeep.setGeometry(QtCore.QRect(420, 310, 81, 31))
        self.Bkeep.setObjectName("Bkeep")
        self.Bcancel = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.Bcancel.setGeometry(QtCore.QRect(640, 310, 81, 31))
        self.Bcancel.setObjectName("Bcancel")
        self.Breturn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.Breturn.setGeometry(QtCore.QRect(530, 310, 81, 31))
        self.Breturn.setObjectName("Breturn")
        self.Bat = QtWidgets.QPushButton(parent=Form)
        self.Bat.setGeometry(QtCore.QRect(340, 740, 91, 51))
        self.Bat.setObjectName("Bat")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 设置表格隐藏行号
        self.RTable.verticalHeader().setVisible(False)
        self.BTable.verticalHeader().setVisible(False)
        # 设置表格不可编辑
        self.RTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.BTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        # 拉伸表格
        self.RTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.BTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        # 绑定事件
        self.RselectSure.clicked.connect(self.Rselect)
        self.BselectSure.clicked.connect(self.Bselect)
        self.Rcancel.clicked.connect(self.cancelReserve)
        self.Bkeep.clicked.connect(self.keepBorrow)
        self.Breturn.clicked.connect(self.returnBook)
        self.Bcancel.clicked.connect(self.cancelBorrow)
        self.Bat.clicked.connect(self.Kill)
        # 如果self.sid!=None，则设置学号搜索框不可编辑,并设置搜索框内容为self.sid
        if self.sid:
            self.RselectSid.setReadOnly(True)
            self.RselectSid.setText(str(self.sid))
            self.RselectSid.setStyleSheet("background-color: #eee;")
            self.BselectSid.setReadOnly(True)
            self.BselectSid.setText(str(self.sid))
            self.BselectSid.setStyleSheet("background-color: #eee;")
            # 隐藏批处理违期按钮
            self.Bat.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理页面"))
        self.groupBox.setTitle(_translate("Form", "预约管理"))
        self.label.setText(_translate("Form", "学   号："))
        self.label_2.setText(_translate("Form", "书   号："))
        self.label_3.setText(_translate("Form", "状   态："))
        self.RselectStatus.setItemText(0, _translate("Form", "全部"))
        self.RselectStatus.setItemText(1, _translate("Form", "正常"))
        self.RselectStatus.setItemText(2, _translate("Form", "违期"))
        self.RselectSure.setText(_translate("Form", "搜索"))
        item = self.RTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "学号"))
        item = self.RTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "书号"))
        item = self.RTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "预约日期"))
        item = self.RTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "取书日期"))
        item = self.RTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "过期日期"))
        self.Rcancel.setText(_translate("Form", "取消预约"))
        self.groupBox_2.setTitle(_translate("Form", "借阅管理"))
        self.label_4.setText(_translate("Form", "学   号："))
        self.label_5.setText(_translate("Form", "书   号："))
        self.label_6.setText(_translate("Form", "状   态："))
        self.BselectStatus.setItemText(0, _translate("Form", "全部"))
        self.BselectStatus.setItemText(1, _translate("Form", "正常"))
        self.BselectStatus.setItemText(2, _translate("Form", "违期"))
        self.BselectSure.setText(_translate("Form", "搜索"))
        item = self.BTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "学号"))
        item = self.BTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "书号"))
        item = self.BTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "借书日期"))
        item = self.BTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "截止日期"))
        item = self.BTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "还书日期"))
        self.Bkeep.setText(_translate("Form", "续借"))
        self.Bcancel.setText(_translate("Form", "取消借阅"))
        self.Breturn.setText(_translate("Form", "还书"))
        self.Bat.setText(_translate("Form", "批处理违期"))

    def initTable(self):
        self.RTable.setRowCount(0)
        self.BTable.setRowCount(0)
        sql = "select * from reserve"
        if self.sid:
            sql += " where sid = '{}'".format(self.sid)
        # 按照预约日期降序
        sql += " order by reserve_date desc"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            self.RTable.setRowCount(self.RTable.rowCount() + 1)
            for j in range(len(result[i])):
                self.RTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
        sql = "select * from borrow"
        if self.sid:
            sql += " where sid = '{}'".format(self.sid)
        sql += " order by borrow_date desc"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            self.BTable.setRowCount(self.BTable.rowCount() + 1)
            for j in range(len(result[i])):
                self.BTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    def Rselect(self):
        sid = self.RselectSid.text()
        bid = self.RselectBid.text()
        status = self.RselectStatus.currentText()
        if status == "全部":
            sql = "select * from reserve where sid like '%{}%' and bid like '%{}%'".format(sid, bid)
        elif status == "正常":
            sql = "select * from reserve where sid like '%{}%' and bid like '%{}%' and (take_date > CURDATE() or take_date > pass_date)".format(sid, bid)
        elif status == "违期":
            sql = "select * from reserve where sid like '%{}%' and bid like '%{}%' and (take_date < CURDATE() and (pass_date is NULL or take_date < pass_date))".format(sid, bid)
        sql += " order by reserve_date desc"
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        result = self.cursor.fetchall()
        self.RTable.setRowCount(0)
        for i in range(len(result)):
            self.RTable.setRowCount(self.RTable.rowCount() + 1)
            for j in range(len(result[i])):
                self.RTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    # 取消预约
    def cancelReserve(self):
        row = self.RTable.currentRow()
        sid = self.RTable.item(row, 0).text()
        bid = self.RTable.item(row, 1).text()
        reserveDate = self.RTable.item(row, 2).text()
        passDate = self.RTable.item(row, 4).text()
        # 过期的预约不可取消
        print(passDate)
        if passDate != 'None':
            QtWidgets.QMessageBox.warning(self, "警告", "预约已过期，不可取消")
            return
        sql = "delete from reserve where sid = '{}' and bid = '{}' and reserve_date = '{}'".format(sid, bid, reserveDate)
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
        except Exception as e:
            print(e)
        self.Rselect()

    def Bselect(self):
        sid = self.BselectSid.text()
        bid = self.BselectBid.text()
        status = self.BselectStatus.currentText()
        if status == "全部":
            sql = "select * from borrow where sid like '%{}%' and bid like '%{}%'".format(sid, bid)
        elif status == "正常":
            sql = "select * from borrow where sid like '%{}%' and bid like '%{}%' and due_date >= return_date".format(sid, bid)
        elif status == "违期":
            sql = "select * from borrow where sid like '%{}%' and bid like '%{}%' and due_date < return_date".format(sid, bid)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        result = self.cursor.fetchall()
        self.BTable.setRowCount(0)
        for i in range(len(result)):
            self.BTable.setRowCount(self.BTable.rowCount() + 1)
            for j in range(len(result[i])):
                self.BTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    # 续借
    def keepBorrow(self):
        row = self.BTable.currentRow()
        sid = self.BTable.item(row, 0).text()
        bid = self.BTable.item(row, 1).text()
        # 默认续借7天
        # 已经还书的书不可续借
        if self.BTable.item(row, 4).text() != 'None':
            QtWidgets.QMessageBox.warning(self, "警告", "已经还书，不可续借")
            return
        sql = "update borrow set due_date = due_date + 7 where sid = '{}' and bid = '{}'".format(sid, bid)
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
        except Exception as e:
            print(e)
        self.Bselect()

    # 还书
    def returnBook(self):
        row = self.BTable.currentRow()
        sid = self.BTable.item(row, 0).text()
        bid = self.BTable.item(row, 1).text()
        borrowDate = self.BTable.item(row, 2).text()
        # 已经还书的书不可再次还书
        if self.BTable.item(row, 4).text() != 'None':
            QtWidgets.QMessageBox.warning(self, "警告", "已经还书，不可再次还书")
            return
        sql = "update borrow set return_date = CURDATE() where sid = '{}' and bid = '{}' and borrow_date = '{}'".format(sid, bid, borrowDate)
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
        except Exception as e:
            print(e)
        self.Bselect()

    # 取消借阅
    def cancelBorrow(self):
        row = self.BTable.currentRow()
        sid = self.BTable.item(row, 0).text()
        bid = self.BTable.item(row, 1).text()
        borrowDate = self.BTable.item(row, 2).text()
        # 已经还书的书不可取消借阅
        if self.BTable.item(row, 4).text() != 'None':
            QtWidgets.QMessageBox.warning(self, "警告", "已经还书，不可取消借阅")
            return
        sql = "delete from borrow where sid = '{}' and bid = '{}' and borrow_date = '{}'".format(sid, bid, borrowDate)
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
        except Exception as e:
            print(e)
        self.Bselect()

    # 批处理违期，调用存储过程Kill
    def Kill(self):
        sql = "select sid from reserve where take_date < CURDATE() and pass_date is NULL \
            union select sid from borrow where due_date < CURDATE() and return_date is NULL"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            sid = result[i][0]
            sql = "call killUser('{}')".format(sid)
            try:
                self.cursor.execute(sql)
                self.cursor.connection.commit()
            except Exception as e:
                print(e)
        self.Bselect()
        self.Rselect()


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
