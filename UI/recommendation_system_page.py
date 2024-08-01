from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1057, 958)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        # self.setMouseTracking(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1071, 961))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background: rgb(238, 233, 233)")
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 170, 301, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 30, 400, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(700, 110, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setStyleSheet("color:red")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(760, 30, 271, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")

        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setGeometry(QtCore.QRect(270, 110, 400, 41))
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)

        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(70, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(230, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(780, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(650, 260, 381, 631))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(10, 260, 421, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_27.setLineWidth(3)
        self.label_27.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                    "background-color: #fafafa;")
        self.label_27.setObjectName("label_27")

        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(610, 260, 421, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setFrameShape(QtWidgets.QFrame.Box)
        self.label_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_28.setLineWidth(3)
        self.label_28.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                    "background-color: #fafafa;")
        self.label_28.setObjectName("label_28")
        self.tabWidget.addTab(self.tab_2, "")

        self.tabWidget.setStyleSheet("pane{top:-1px;};")
        self.tabWidget.setStyleSheet("background-color:#fafafa;")
        # self.tabWidget.setStyleSheet("background-image: url(./resources/picture/background.png);")  # 设置背景图片
        Form.setStyleSheet("background-color:#fafafa;")  # 设置背景颜色

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_9.clicked.connect(self.wipedata3)
        # self.lineEdit_3.leaveEvent.connect(self.leaveEvent)

    def enterEvent(self, QEvent):
        print("鼠标进来了")

    def leaveEvent(self, event):
        print("鼠标出去了")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form","电影推荐系统"))
        Form.setWindowIcon(QIcon('image/heu.jpg'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "电影推荐"))
        self.label_6.setText(_translate("Form", "请选择推荐算法"))
        self.label_6.setStyleSheet("background: transparent;")
        self.label_4.setText(_translate("Form", "请输入用户id"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "请输入用户id"))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "基于深度学习ALS推荐算法"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "基于SVD推荐算法"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "基于用户的推荐算法"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "基于项目的推荐算法"))
        self.label_27.setText(_translate("Form", "+显示用户已观看电影"))
        self.label_28.setText(_translate("Form", "+显示用户推荐电影"))

        self.label_4.setStyleSheet("background: transparent;")
        self.pushButton_9.setText(_translate("Form", "清空输入"))
        self.pushButton_9.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")
        self.pushButton_5.setText(_translate("Form", "点击进行推荐"))
        self.pushButton_5.setStyleSheet(
            "QPushButton{border-radius:5px;background:rgb(100, 157, 200);color:black}")

    def wipedata3(self):
        self.lineEdit_3.setText('')
        self.label_27.setPixmap(QPixmap(""))

    def tip1(self):
        QMessageBox().warning(None, "警告", "请确保信息输入完整！", QMessageBox.Close)

    def showResult(self):
       self.label_28.setText();