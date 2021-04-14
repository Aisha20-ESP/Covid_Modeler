# Code pour gerer l'authentification 
# Author: Mouhammad Sylla @mouha09

from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QMessageBox

from packages.ui_codes.login_window_ui import Ui_LoginWindow
from packages.gui.home_window import HomeWindow
from functools import partial


class LoginWindow(QMainWindow):
    def __init__(self,ctx):
        super().__init__()
        self.ctx = ctx
        self.ui = Ui_LoginWindow(ctx)
        self.ui.setupUi(self)
        self.setWindowTitle("Auhtentification")
        self.btn_login = self.ui.btn_login
        self.btn_login.clicked.connect(partial(self.authentication,self.ctx))
    
    #Fonction permettant d'autentifier l'utilisateur à partir des identifiants renseignés dans la base de données 
    def authentication(self,ctx):
        self.username = self.ui.te_username.toPlainText()
        self.mdp = self.ui.te_mdp.toPlainText()
        # self.displayError()
        self.home_window = HomeWindow(ctx,self.username)
        self.home_window.show()
        self.close()
        
    def displayError(self):
        message = QMessageBox(self)
        message.setWindowTitle("Erreur !")
        message.setIcon(QMessageBox.Critical)
        message.setText('Login ou mot de passe incorrect. Veuillez reessayer')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()
       
