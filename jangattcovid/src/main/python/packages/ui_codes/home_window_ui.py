#Code de l'interface d'accueil 
#Author: Mouhammad Sylla @mouhaO9

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2 import QtWidgets,QtCore,QtGui



class Ui_HomeWindow(object):
    def __init__(self,ctx):
        self.ctx = ctx
        super().__init__()
        
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1700, 1080)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, -10, 1969, 91))
        self.header_frame.setStyleSheet("QFrame{\n"
"    background-color: #000F1B;\n"
"}")
        self.header_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_frame.setObjectName("header_frame")
        self.logo_label = QtWidgets.QLabel(self.header_frame)
        self.logo_label.setGeometry(QtCore.QRect(20, 20, 121, 71))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/logo_small.png")))
        self.logo_label.setObjectName("logo_label")
        self.label = QtWidgets.QLabel(self.header_frame)
        self.label.setGeometry(QtCore.QRect(1500, 41, 145, 20))
        self.label.setStyleSheet("QLabel{\n"
"    color:white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.header_frame)
        self.label_2.setGeometry(QtCore.QRect(1480, 40, 21, 20))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/user_icon.png")))
        self.label_2.setObjectName("label_2")
        self.menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.menu_frame.setGeometry(QtCore.QRect(0, 80, 231, 1001))
        self.menu_frame.setStyleSheet("QFrame{\n"
"    background-color: #000F1B;\n"
"    border:none;\n"
"}")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.btn_new_data = QtWidgets.QPushButton(self.menu_frame)
        self.btn_new_data.setGeometry(QtCore.QRect(20, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_new_data.setFont(font)
        self.btn_new_data.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_new_data.setStyleSheet("QPushButton{\n"
"    background-color:#000F1B;\n"
"    border : none;\n"
"    color: #EC6E7D;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:#EC6E7D;\n"
"    color : white;\n"
"    border-radius:7px;\n"
"    padding:20px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/icons/stat_icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_new_data.setIcon(icon)
        self.btn_new_data.setObjectName("btn_new_data")
        self.btn_edit_profile = QtWidgets.QPushButton(self.menu_frame)
        self.btn_edit_profile.setGeometry(QtCore.QRect(0, 160, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_edit_profile.setFont(font)
        self.btn_edit_profile.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_edit_profile.setStyleSheet("QPushButton{\n"
"    background-color:#000F1B;\n"
"    border : none;\n"
"    color: #EC6E7D;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:#EC6E7D;\n"
"    color : white;\n"
"    border-radius:7px;\n"
"    padding:20px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/icons/cogs_icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_edit_profile.setIcon(icon1)
        self.btn_edit_profile.setObjectName("btn_edit_profile")
        self.btn_accueil = QtWidgets.QPushButton(self.menu_frame)
        self.btn_accueil.setGeometry(QtCore.QRect(0, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_accueil.setFont(font)
        self.btn_accueil.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_accueil.setStyleSheet("QPushButton{\n"
"    background-color:#000F1B;\n"
"    border : none;\n"
"    color: #EC6E7D;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:#EC6E7D;\n"
"    color : white;\n"
"    border-radius:7px;\n"
"    padding:20px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/icons/home_icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_accueil.setIcon(icon2)
        self.btn_accueil.setObjectName("btn_accueil")
        self.btn_statistiques = QtWidgets.QPushButton(self.menu_frame)
        self.btn_statistiques.setGeometry(QtCore.QRect(0, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_statistiques.setFont(font)
        self.btn_statistiques.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_statistiques.setStyleSheet("QPushButton{\n"
"    background-color:#000F1B;\n"
"    border : none;\n"
"    color: #EC6E7D;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:#EC6E7D;\n"
"    color : white;\n"
"    border-radius:7px;\n"
"    padding:20px;\n"
"}")
        self.btn_statistiques.setIcon(icon)
        self.btn_statistiques.setObjectName("btn_statistiques")
        self.btn_aide = QtWidgets.QPushButton(self.menu_frame)
        self.btn_aide.setGeometry(QtCore.QRect(-20, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_aide.setFont(font)
        self.btn_aide.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_aide.setStyleSheet("QPushButton{\n"
"    background-color:#000F1B;\n"
"    border : none;\n"
"    color: #EC6E7D;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:#EC6E7D;\n"
"    color : white;\n"
"    border-radius:7px;\n"
"    padding:20px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/icons/help_icon.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_aide.setIcon(icon3)
        self.btn_aide.setObjectName("btn_aide")
        
        #Button Deconnexion
        
        self.btn_logout = QtWidgets.QPushButton(self.menu_frame)
        self.btn_logout.setGeometry(QtCore.QRect(10, 310, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_logout.setStyleSheet("QPushButton{\n"
"    background-color:#000F1B;\n"
"    border : none;\n"
"    color: #EC6E7D;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:#EC6E7D;\n"
"    color : white;\n"
"    border-radius:7px;\n"
"    padding:20px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/icons/logout.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_logout.setIcon(icon4)
        self.btn_logout.setObjectName("btn_logout")
        
        
        #End Button Deconnexion
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(229, 79, 1471, 1001))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color : #F4F7FC;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(60, 100, 421, 141))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color:white;\n"
"    border-radius:10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label_4.setStyleSheet("QLabel{\n"
"    color:#7E84A3;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_nombre_cas = QtWidgets.QLabel(self.frame_2)
        self.label_nombre_cas.setGeometry(QtCore.QRect(19, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre_cas.setFont(font)
        self.label_nombre_cas.setObjectName("label_nombre_cas")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(289, 20, 111, 101))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/corona.png")))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(950, 100, 421, 141))
        self.frame_3.setStyleSheet("QFrame{\n"
"    background-color:white;\n"
"    border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_7.setStyleSheet("QLabel{\n"
"    color:#7E84A3;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_nombre_deces = QtWidgets.QLabel(self.frame_3)
        self.label_nombre_deces.setGeometry(QtCore.QRect(19, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre_deces.setFont(font)
        self.label_nombre_deces.setObjectName("label_nombre_deces")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(289, 20, 111, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/mask.png")))
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(505, 100, 421, 141))
        self.frame_4.setStyleSheet("QFrame{\n"
"    background-color:white;\n"
"    border-radius:10px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_10.setStyleSheet("QLabel{\n"
"    color:#7E84A3;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_nombre_gueris = QtWidgets.QLabel(self.frame_4)
        self.label_nombre_gueris.setGeometry(QtCore.QRect(19, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombre_gueris.setFont(font)
        self.label_nombre_gueris.setObjectName("label_nombre_gueris")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(279, 20, 121, 101))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/gueri_icon.png")))
        self.label_12.setObjectName("label_12")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 260, 1471, 741))
        self.scrollArea.setStyleSheet("background-color:#F4F7FC;\n"
"border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1471, 741))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_carte_senegal = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_carte_senegal.setGeometry(QtCore.QRect(270, 10, 901, 691))
        self.label_carte_senegal.setText("")
        self.label_carte_senegal.setPixmap(QtGui.QPixmap(self.ctx.get_resource("assets/senegal_card.png")))
        self.label_carte_senegal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_carte_senegal.setObjectName("label_carte_senegal")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "MainWindow"))
        self.label.setText(_translate("HomeWindow", "Nom Utilisateur"))
        self.btn_new_data.setText(_translate("HomeWindow", "   Nouvelles  Données"))
        self.btn_edit_profile.setText(_translate("HomeWindow", "   Modifier Profil"))
        self.btn_accueil.setText(_translate("HomeWindow", "   Accueil"))
        self.btn_statistiques.setText(_translate("HomeWindow", "  Statistiques"))
        self.btn_aide.setText(_translate("HomeWindow", "   Aide"))
        self.btn_logout.setText(_translate("HomeWindow", "   Deconnexion"))
        
        self.label_4.setText(_translate("HomeWindow", "Nombre Total de Cas "))
        self.label_nombre_cas.setText(_translate("HomeWindow", "0"))
        self.label_3.setText(_translate("HomeWindow", "Aperçu"))
        self.label_7.setText(_translate("HomeWindow", "Nombre Total de Deces"))
        self.label_nombre_deces.setText(_translate("HomeWindow", "0"))
        self.label_10.setText(_translate("HomeWindow", "Nombre Total de Guéris"))
        self.label_nombre_gueris.setText(_translate("HomeWindow", "0"))
