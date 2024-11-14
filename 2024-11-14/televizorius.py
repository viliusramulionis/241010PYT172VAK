class Televizorius() :
    kanalas = 1
    garsas = 50

    def __init__(self, gamintojas) :
        self.gamintojas = gamintojas

    def get_reiksmes(self) :
        return f"Televizorius ‘{self.gamintojas}’ šiuo metu rodo {self.kanalas} kanalą. Garso lygis {self.garsas}."
    
    def set_garsas(self, garsas) :
        if garsas <= 100 and garsas >= 0 :
            self.garsas = garsas

    def set_kanalas(self, kanalas) :
        if kanalas <= 50 and kanalas > 0 :
            self.kanalas = kanalas
        else :
            self.kanalas = 1

    def get_kanalas(self) :
        return "Šiuo metu rodomas kanalas" + str(self.kanalas)

    
sony = Televizorius("Sony")

sony.set_garsas(85)
sony.set_garsas(-5)
sony.set_kanalas(24)

print(sony.get_reiksmes())

lg = Televizorius("LG")

lg.set_garsas(12)
lg.set_kanalas(49)
lg.set_kanalas(0)

print(lg.get_reiksmes())

print(lg.get_kanalas())