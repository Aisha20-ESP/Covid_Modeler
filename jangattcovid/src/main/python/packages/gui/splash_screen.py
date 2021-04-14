# Code du Splash Screen 
# Author : Mouhammad Sylla @mouha09

import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from packages.ui_codes.splash_ui import Ui_SplashScreen
from packages.gui.login import LoginWindow
from fbs_runtime.application_context.PySide2 import ApplicationContext

from functools import partial



counter = 0

class SplashScreen(QMainWindow):
    def __init__(self,ctx):
        super().__init__()
        self.ctx = ctx
        self.ui = Ui_SplashScreen(ctx)
        self.ui.setupUi(self)

        # On enleve le windowFlag, la barre avec les icones reduire,fermer...
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # On enlev les bordures et on cree une petite ombre pour faire jolie
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        # On cree un timer pour simuler le chargement et faire rouler le progressbar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(partial(self.progress, self.ctx))
         
        self.timer.start(35)

        
        # On change les texts au niveau du label_description
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("Chargement de la base de données"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("Chargement des paramétres"))

        # On affiche le loginWindow
        # self.show()
   

    #Cette fonction permet de faire varier la barre de progression et de la faire evoluer jusqu'à 100
    def progress(self,ctx):

        global counter
        
        self.ui.progressBar.setValue(counter)

        if counter > 100:
          
            self.timer.stop()
            self.main = LoginWindow(ctx)
            
            self.main.show()
            self.close()
            
        counter += 1
        
