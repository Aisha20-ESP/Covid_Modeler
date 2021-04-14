#Code de l'interface d'authentification 
#Author: Mouhammad Sylla @mouha09

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2 import QtWidgets,QtCore,QtGui




class Ui_LoginWindow(object):
    def __init__(self,ctx):
            super().__init__()
            self.ctx = ctx

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.onbaord_image = QtWidgets.QLabel(self.centralwidget)
        self.onbaord_image.setGeometry(QtCore.QRect(0, 0, 1051, 1080))
        self.onbaord_image.setStyleSheet("background-color:white;")
        self.onbaord_image.setText("")
        self.onbaord_image.setPixmap(QtGui.QPixmap(self.ctx.get_resource("images/onboard.png")))
        self.onbaord_image.setObjectName("onbaord_image")
        self.login_frame = QtWidgets.QFrame(self.centralwidget)
        self.login_frame.setGeometry(QtCore.QRect(990, -1, 951, 1111))
        self.login_frame.setStyleSheet("background-color: #000F1B")
        self.login_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.login_frame.setObjectName("login_frame")
        self.label_logo = QtWidgets.QLabel(self.login_frame)
        self.label_logo.setGeometry(QtCore.QRect(210, 50, 291, 91))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(self.ctx.get_resource("images/logo.png")))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.frame = QtWidgets.QFrame(self.login_frame)
        self.frame.setGeometry(QtCore.QRect(140, 380, 481, 461))
        self.frame.setStyleSheet("background-color:white;\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.te_username = QtWidgets.QTextEdit(self.frame)
        self.te_username.setPlaceholderText('Username')
        self.te_username.setGeometry(QtCore.QRect(80, 160, 321, 41))
        self.te_username.setStyleSheet("border:1px solid black;\n"
"text-align:center;\n"
"padding-top:7px;\n"
"color : black;\n"
"padding-left:8px;")
        self.te_username.setObjectName("te_username")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 60, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color : black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.te_mdp = QtWidgets.QTextEdit(self.frame)
        # self.te_mdp = QtWidgets.QLineEdit(self.frame)
        # self.te_mdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.te_mdp.setPlaceholderText('Mot de passe')
        self.te_mdp.setGeometry(QtCore.QRect(80, 260, 321, 41))
        self.te_mdp.setStyleSheet("border:1px solid black;\n"
"text-align:center;\n"
"padding-top:7px;\n"
"color : black;\n"
"padding-left:8px;")
        self.te_mdp.setObjectName("te_mdp")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(152, 350, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_login.setStyleSheet("QPushButton{\n"
"    /*background-color:#FF0000;*/\n"
"    background-color:#EF3F3F;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#000F1B;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 61, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(self.ctx.get_resource("images/login3.png")))
        self.label_2.setObjectName("label_2")
        self.label_user = QtWidgets.QLabel(self.login_frame)
        self.label_user.setGeometry(QtCore.QRect(310, 260, 141, 141))
        self.label_user.setStyleSheet("background-color:none;")
        self.label_user.setText("")
        self.label_user.setPixmap(QtGui.QPixmap(self.ctx.get_resource("images/user2.png")))
        self.label_user.setObjectName("label_user")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Authentification"))
        self.btn_login.setText(_translate("LoginWindow", "Se Connecter"))
