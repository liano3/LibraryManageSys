# Form implementation generated from reading ui file 'alterProfile.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, cursor, username):
        super(Ui_Form, self).__init__()
        self.cursor = cursor
        self.username = username
        sql = "select role from user where username = '{}'".format(username)
        cursor.execute(sql)
        role = cursor.fetchone()[0]
        self.role = role
        self.setupUi(self)
        self.initUserInfo()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 361, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.alterUsername = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterUsername.setObjectName("alterUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterUsername)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.alterName = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterName.setObjectName("alterName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterName)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.alterTel = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.alterTel.setObjectName("alterTel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.alterTel)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.verifyPassword = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.verifyPassword.setObjectName("verifyPassword")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verifyPassword)
        self.alterSure = QtWidgets.QPushButton(parent=Form)
        self.alterSure.setGeometry(QtCore.QRect(300, 240, 81, 31))
        self.alterSure.setObjectName("alterSure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 确认修改
        self.alterSure.clicked.connect(self.alterUserInfo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改资料"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "姓   名："))
        self.label_3.setText(_translate("Form", "联系方式："))
        self.label_4.setText(_translate("Form", "验证密码："))
        self.alterSure.setText(_translate("Form", "确认修改"))

    # 初始化用户信息
    def initUserInfo(self):
        if self.role == 1:
            sql = "select username, aname, tel, password from user, admin where user.uid = admin.aid and user.username = %s"
        else:
            sql = "select username, sname, tel, password from user, student where user.uid = student.sid and user.username = %s"
        self.cursor.execute(sql, (self.username,))
        result = self.cursor.fetchone()
        self.alterUsername.setText(result[0])
        self.alterName.setText(result[1])
        self.alterTel.setText(result[2])

    # 修改用户信息
    def alterUserInfo(self):
        username = self.alterUsername.text()
        name = self.alterName.text()
        tel = self.alterTel.text()
        password = self.verifyPassword.text()
        if not username or not name or not tel or not password:
            QtWidgets.QMessageBox.warning(self, "警告", "请填写完整信息！")
            return
        # 验证密码
        sql = "select password from user where username = %s"
        self.cursor.execute(sql, (self.username,))
        result = self.cursor.fetchone()
        if password != result[0]:
            QtWidgets.QMessageBox.warning(self, "警告", "密码错误！")
            return
        # 修改信息
        if self.role == 1:
            sql = "update user, admin set user.username = %s, aname = %s, tel = %s where user.uid = admin.aid and user.username = %s"
        else:
            sql = "update user, student set user.username = %s, sname = %s, tel = %s where user.uid = student.sid and user.username = %s"
        try:
            self.cursor.execute(sql, (username, name, tel, self.username))
            self.cursor.connection.commit()
            QtWidgets.QMessageBox.information(self, "提示", "修改成功！")
            self.close()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "警告", "修改失败！")
            print(e)


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
    ui = Ui_Form(cursor, "admin1")
    ui.show()
    sys.exit(app.exec())
