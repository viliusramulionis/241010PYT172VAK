from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    # skaiciuotuvas = 0 

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.mygtukas.clicked.connect(self.paspausta)

    def paspausta(self) :
        print(self.vardas.text())

        
aplikacija = QApplication([])

langas = Langas()

langas.show()
aplikacija.exec()

# Užduotis:
# Vartotojo prašome įvesti šias reikšmes:
# Vardas
# Pavardė
# Gimimo metai (2024 - 1980)

# Sveiki Jonas Jonaitis, Jums yra 44 metai