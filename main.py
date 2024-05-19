import sys
import pymysql
from PyQt6 import QtWidgets
import Login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="10086",
        database="library",
        charset="utf8"
    )
    cursor = db.cursor()
    ui = Login.Ui_Form(cursor)
    ui.show()
    sys.exit(app.exec())
