# Form implementation generated from reading ui file 'alterStudent.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, cursor):
        super(Ui_Form, self).__init__()
        self.cursor = cursor
        self.setupUi(self)
        self.initStudentTable()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.StudentTable = QtWidgets.QTableWidget(parent=Form)
        self.StudentTable.setGeometry(QtCore.QRect(40, 111, 721, 211))
        self.StudentTable.setObjectName("StudentTable")
        self.StudentTable.setColumnCount(5)
        self.StudentTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StudentTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StudentTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StudentTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.StudentTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.StudentTable.setHorizontalHeaderItem(4, item)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 721, 71))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 53, 15))
        self.label.setObjectName("label")
        self.selectSid = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectSid.setGeometry(QtCore.QRect(70, 30, 121, 21))
        self.selectSid.setObjectName("selectSid")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 30, 53, 15))
        self.label_2.setObjectName("label_2")
        self.selectSname = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectSname.setGeometry(QtCore.QRect(260, 30, 121, 21))
        self.selectSname.setObjectName("selectSname")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 53, 15))
        self.label_3.setObjectName("label_3")
        self.selectMajor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectMajor.setGeometry(QtCore.QRect(450, 30, 131, 21))
        self.selectMajor.setObjectName("selectMajor")
        self.searchSure = QtWidgets.QPushButton(parent=self.groupBox)
        self.searchSure.setGeometry(QtCore.QRect(640, 20, 81, 31))
        self.searchSure.setObjectName("searchSure")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 330, 721, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.alterSid = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterSid.setObjectName("alterSid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterSid)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.alterSname = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterSname.setObjectName("alterSname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterSname)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.alterMajor = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterMajor.setObjectName("alterMajor")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterMajor)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.alterTel = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterTel.setObjectName("alterTel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterTel)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.alterStatus = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.alterStatus.setObjectName("alterStatus")
        self.alterStatus.addItem("")
        self.alterStatus.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterStatus)
        self.alterSure = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.alterSure.setGeometry(QtCore.QRect(530, 180, 81, 31))
        self.alterSure.setObjectName("alterSure")
        self.deleteSure = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.deleteSure.setGeometry(QtCore.QRect(640, 180, 81, 31))
        self.deleteSure.setObjectName("deleteSure")
        self.addSure = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.addSure.setGeometry(QtCore.QRect(420, 180, 81, 31))
        self.addSure.setObjectName("addSure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 选中行绑定事件
        self.StudentTable.clicked.connect(self.selectStudent)
        # 搜索按钮绑定事件
        self.searchSure.clicked.connect(self.searchStudent)
        # 修改按钮绑定事件
        self.alterSure.clicked.connect(self.alterStudent)
        # 删除按钮绑定事件
        self.deleteSure.clicked.connect(self.deleteStudent)
        # 添加按钮绑定事件
        self.addSure.clicked.connect(self.addStudent)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生信息维护"))
        item = self.StudentTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "学号"))
        item = self.StudentTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.StudentTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "专业"))
        item = self.StudentTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "电话号码"))
        item = self.StudentTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "状态"))
        self.groupBox.setTitle(_translate("Form", "筛选"))
        self.label.setText(_translate("Form", "学   号："))
        self.label_2.setText(_translate("Form", "姓   名："))
        self.label_3.setText(_translate("Form", "专   业："))
        self.searchSure.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "表单"))
        self.label_5.setText(_translate("Form", "学   号："))
        self.label_6.setText(_translate("Form", "姓   名："))
        self.label_7.setText(_translate("Form", "专   业："))
        self.label_8.setText(_translate("Form", "电   话："))
        self.label_4.setText(_translate("Form", "状   态："))
        self.alterStatus.setItemText(0, _translate("Form", "正常"))
        self.alterStatus.setItemText(1, _translate("Form", "冻结"))
        self.alterSure.setText(_translate("Form", "修改"))
        self.deleteSure.setText(_translate("Form", "删除"))
        self.addSure.setText(_translate("Form", "添加"))

    def initStudentTable(self):
        self.StudentTable.setRowCount(0)
        sql = "select sid, sname, major, tel, status from student, user where student.sid = user.uid and user.role = 0"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            rowPosition = self.StudentTable.rowCount()
            self.StudentTable.insertRow(rowPosition)
            for i in range(len(row) - 1):
                self.StudentTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(row[i])))
            if row[4] == 0:
                self.StudentTable.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem("正常"))
            else:
                self.StudentTable.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem("冻结"))
        # 隐藏行号
        self.StudentTable.verticalHeader().setVisible(False)
        # 不可编辑
        self.StudentTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        # 均匀拉伸列宽
        self.StudentTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def searchStudent(self):
        sid = self.selectSid.text()
        sname = self.selectSname.text()
        major = self.selectMajor.text()
        sql = "select * from student where sid like '%{}%' and sname like '%{}%' and major like '%{}%'".format(sid, sname, major)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.StudentTable.setRowCount(0)
        for row in result:
            rowPosition = self.StudentTable.rowCount()
            self.StudentTable.insertRow(rowPosition)
            for i in range(len(row)):
                self.StudentTable.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(row[i])))

    def addStudent(self):
        sid = self.alterSid.text()
        sname = self.alterSname.text()
        major = self.alterMajor.text()
        tel = self.alterTel.text()
        sql = "insert into student values ('{}', '{}', '{}', '{}')".format(sid, sname, major, tel)
        try:
            self.cursor.execute(sql)
            QtWidgets.QMessageBox.information(self, "提示", "添加成功")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "添加失败")
        self.cursor.connection.commit()
        self.initStudentTable()

    def selectStudent(self):
        row = self.StudentTable.currentRow()
        self.alterSid.setText(self.StudentTable.item(row, 0).text())
        self.alterSname.setText(self.StudentTable.item(row, 1).text())
        self.alterMajor.setText(self.StudentTable.item(row, 2).text())
        self.alterTel.setText(self.StudentTable.item(row, 3).text())
        # 设置状态下拉框
        status = self.StudentTable.item(row, 4).text()
        if status == "正常":
            self.alterStatus.setCurrentIndex(0)
        else:
            self.alterStatus.setCurrentIndex(1)

    def alterStudent(self):
        sid = self.alterSid.text()
        # 如果 sid 不等于当前选中的 sid，说明 sid 被修改
        oldSid = self.StudentTable.item(self.StudentTable.currentRow(), 0).text()
        if sid != oldSid:
            # 调用存储过程 updateStudentId
            sql = "call updateStudentId('{}', '{}')".format(oldSid, sid)
            try:
                self.cursor.execute(sql)
            except Exception as e:
                QtWidgets.QMessageBox.information(self, "提示", "id修改失败，请检查id是否重复")
                return
        sname = self.alterSname.text()
        major = self.alterMajor.text()
        tel = self.alterTel.text()
        status = self.alterStatus.currentIndex()
        oldStatus = self.StudentTable.item(self.StudentTable.currentRow(), 4).text()
        oldStatus = 0 if oldStatus == "正常" else 1
        if status != oldStatus:
            sql = "call unkillUser({}, {})".format(sid, status)
            try:
                self.cursor.execute(sql)
            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.information(self, "提示", "状态修改失败")
        sql = "update student set sname = '{}', major = '{}', tel = '{}' where sid = '{}'".format(sname, major, tel, sid)
        try:
            self.cursor.execute(sql)
            QtWidgets.QMessageBox.information(self, "提示", "修改成功")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "修改失败")
        self.cursor.connection.commit()
        self.initStudentTable()

    def deleteStudent(self):
        sid = self.alterSid.text()
        sql = "CALL deleteStudent('{}')".format(sid)
        try:
            self.cursor.execute(sql)
            QtWidgets.QMessageBox.information(self, "提示", "删除成功")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "删除失败")
        self.cursor.connection.commit()
        self.initStudentTable()

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
