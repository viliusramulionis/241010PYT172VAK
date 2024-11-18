# Sukurkite Mokinys klasę, kuri turės mokinio vardą, 
# pavardę ir sąrašą pažymių. Įtraukite metodus, kurie skaičiuotų vidurkį, 
# didžiausią ir mažiausią pažymį. 

class Mokinys() :
    def __init__(self, vardas, pavarde, pazymiai) :
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = pazymiai

    def get_average(self) :
        return sum(self.pazymiai) / len(self.pazymiai)
    
    def get_highest_grade(self) :
        return max(self.pazymiai)
    
    def get_lowest_grade(self) :
        return min(self.pazymiai)


mokinys = Mokinys("Jonas", "Jonaitis", [10, 8, 9, 5, 3, 2])

print(mokinys.get_average())
print(mokinys.get_highest_grade())
print(mokinys.get_lowest_grade())