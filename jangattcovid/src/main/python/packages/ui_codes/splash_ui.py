#Code de l'UI du  SplashScreen 
#Author: Mouhammad Sylla @mouha09


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2 import QtWidgets,QtCore,QtGui




class Ui_SplashScreen(object):
    def __init__(self,ctx):
        self.ctx = ctx
        super().__init__()
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color : #000F1B;\n"
"    border-radius: 10px;\n"
"    color: white\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(120, 220, 431, 21))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: #0E416E;\n"
"    color : white;\n"
"    border-radius: 10px;\n"
"    text-align : center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    /*background-color: #EC6E7D;*/\n"
"    background-color: #FF0000;\n"
"    border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.frame)
        self.label_loading.setGeometry(QtCore.QRect(310, 250, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color:rgb(208, 206, 210);")
        self.label_loading.setObjectName("label_loading")
        self.label_author = QtWidgets.QLabel(self.frame)
        self.label_author.setGeometry(QtCore.QRect(450, 350, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setKerning(True)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("/*color:#EC6E7D*/\n"
"color:rgb(208, 206, 210);")
        self.label_author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_author.setObjectName("label_author")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 40, 278, 99))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.ctx.get_resource('logo.png')))
        self.label.setObjectName("label")
        self.label_description = QtWidgets.QLabel(self.frame)
        self.label_description.setGeometry(QtCore.QRect(230, 160, 225, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("/*color:rgb(208, 206, 210);*/\n"
"/*color : #FF0000;*/\n" "color:white;")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.frame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_loading.setText(_translate("SplashScreen", "Chargement..."))
        self.label_author.setText(_translate("SplashScreen", "Designed By G-X SGBD-PROJECT "))
        self.label_description.setText(_translate("SplashScreen", "Initialisation..."))
