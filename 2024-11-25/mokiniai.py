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
    
    def new_grade(self, grade) :
        if grade > 0 and grade <= 10 :
            self.pazymiai.append(grade)
    
    def __str__(self) :
        return str({
            "vardas" : self.vardas, 
            "pavarde" : self.pavarde, 
            "pazymiai" : self.pazymiai
        })
    
    def __repr__(self) :
        return str({
            "vardas" : self.vardas, 
            "pavarde" : self.pavarde, 
            "pazymiai" : self.pazymiai
        })

mokinys = Mokinys("Jonas", "Jonaitis", [10, 8, 9, 5, 3, 2])

mokinys.new_grade(11)

print(mokinys)

# print(mokinys.get_average())
# print(mokinys.get_highest_grade())
# print(mokinys.get_lowest_grade())

# Sukurkite Abiturientas klasę, kuri paveldi Mokinys klasę ir 
# prideda papildomą funkcionalumą, pvz., gebėjimą pridėti egzamino 
# rezultatus ir skaičiuoti bendrą vidurkį, įskaitant ir egzamino rezultatus. 

class Abiturientas(Mokinys) :
    def __init__(self, vardas, pavarde, pazymiai) :
        super().__init__(vardas, pavarde, pazymiai)

    def set_exam_results(self, *results) :
        self.pazymiai = self.pazymiai + list(results)


abiturientas = Abiturientas("Giedrius", "Giedraitis", [5, 10, 9, 8, 7, 5, 10])

# print(abiturientas) 

# print(abiturientas.get_average())

abiturientas.set_exam_results(5, 8, 10)

# print(abiturientas) 

# print(abiturientas.get_average())


# Sukurkite Mokykla klasę, kuri turės sąrašą Mokinys objektų. 
# Įtraukite metodus, kurie leistų pridėti naują mokinį, pašalinti mokinį, 
# bei skaičiuoti visos mokyklos mokinių pažymių vidurkius.

class Mokykla() :
    students = []

    def new_student(self, student) :
        self.students.append(student)
        

    def delete_student(self, vardas, pavarde) :
        for idx, student in enumerate(self.students) :
            if student.vardas == vardas and student.pavarde == pavarde :
                del self.students[idx]

    def avergage(self) :
        combined_grades = []
        for student in self.students : 
            combined_grades += student.pazymiai

        return sum(combined_grades) / len(combined_grades)

    def __str__(self) :
        return str(mokykla.students)

    

mokykla = Mokykla()


mokykla.new_student(Mokinys("Antanas", "Antanaitis", [10, 8, 9, 5, 3, 2]))
mokykla.new_student(Mokinys("Giedrius", "Giedraitis", [5, 2, 10, 10, 10, 10]))
mokykla.new_student(Mokinys("Elena", "Elenaite", [9, 9, 9, 4, 4, 4]))

# print(mokykla.avergage())
# print(mokykla)

mokykla.delete_student("Antanas", "Antanaitis")


# Atnaujinkite Mokinys klasę. Sukurkite metodus, kurie leistų saugiai 
# pridėti ir gauti pažymius, užtikrinant, kad nebūtų galima pridėti 
# netinkamų pažymių (pvz., neigiamų ar didesnių nei 10).
