
from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from packages.ui_codes.home_window_ui import Ui_HomeWindow

from random import randrange

class HomeWindow(QMainWindow):
    def __init__(self,ctx,username):
        super().__init__()
        
        self.ui = Ui_HomeWindow(ctx)
        self.username = username
        self.ui.setupUi(self)
        self.setWindowTitle("Accueil")
        
        self.createWidgets()
        self.modifyWigets()
        self.createLayout()
        self.addWidgetsToLayout()
        self.setUpConnexion()
        self.initProfile()
        
      
        
    
    
    def createWidgets(self):
        self.label_username = self.ui.label
        self.btn_accueil  = self.ui.btn_accueil
        self.btn_new_data = self.ui.btn_new_data
        self.btn_stats = self.ui.btn_statistiques
        self.nombre_cas = self.ui.label_nombre_cas
        self.nombre_gueris = self.ui.label_nombre_gueris
        self.nombre_deces = self.ui.label_nombre_deces
        
    def modifyWigets(self):
        pass
    
    def createLayout(self):
        pass
    
    def addWidgetsToLayout(self):
        pass
    
    def setUpConnexion(self):
        self.btn_new_data.clicked.connect(self.initializeNewData)
    
    def initProfile(self):
        self.label_username.setText(self.username)
    
    def initializeNewData(self):
        nombre_gueris = randrange(10000,50000)
        nombre_deces =  randrange(10000,50000)
        nombre_cas = randrange(50000,100000)
        self.nombre_gueris.setText(str(nombre_gueris))
        self.nombre_cas.setText(str(nombre_cas))
        self.nombre_deces.setText(str(nombre_deces))