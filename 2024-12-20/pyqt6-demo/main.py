from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow


class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # connect() metodas priskiriamas prie įvykio ir į jį 
        # yra perduodama funkcija kurią norime aktyvuoti įvykus įvykiui
        self.pirmas_mygtukas.clicked.connect(self.pirmas_paspaudimas)
        self.antras_mygtukas.clicked.connect(self.antras_paspaudimas)
        self.trecias_mygtukas.clicked.connect(self.trecias_paspaudimas)

    # Funkcija skirta nurodyti veiksmus kuriuos norime paleisti po paspaudimo įvykio
    def pirmas_paspaudimas(self) :
        self.zinute.setText("Pirmas mygtukas paspaustas")

    def antras_paspaudimas(self) :
        self.zinute.setText("Antras mygtukas paspaustas")

    def trecias_paspaudimas(self) :
        self.zinute.setText("Trečias mygtukas paspaustas")

aplikacija = QApplication([])

langas = Langas()

langas.show()
aplikacija.exec()