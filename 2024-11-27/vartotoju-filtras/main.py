class VartotojuFiltras() :
    def __init__(self, failas) :
        self.data = open(failas, "r").readlines()[1:]

    def skaiciu_tikrinimas(self, stringas) :
        for simbolis in stringas :
            if simbolis.isnumeric() :
                return True
    
    def tusti_gimimo_metai(self) :
        for line in self.data :
            l = line.split(";")
            
            if l[3] :
                print(line, end = "") 

    def slaptazodziai_be_skaiciu(self) :
        for line in self.data :
            l = line.split(";")
            
            if self.skaiciu_tikrinimas(l[4]) :
                print(line, end = "") 

    def amziaus_vidurkis(self) :
        amziaus_suma = 0
        asmenys = 0    

        for line in self.data :
            l = line.split(";")
            
            if l[3] :
                amziaus_suma += 2024 - int(l[3]) 
                asmenys += 1

        print(amziaus_suma / asmenys)
 
    def __str__(self) :
        return str(self.data)
    

vartotoju_filtras = VartotojuFiltras("vartotojai.txt")

vartotoju_filtras.amziaus_vidurkis()