#Point d'entree de notre application 

from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow
from packages.gui.splash_screen import SplashScreen
from PySide2.QtGui import QIcon

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = SplashScreen(appctxt)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)