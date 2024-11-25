import random

# Sukurkite klasę Vaisius, kuris turi: 
# savybę dydis rand 5 - 25; 
# savybę id rand 1000000 - 9999999 
# savybę prakastas False 

# Sukurkite metodą prakasti(), kuris savybės prakąstas reikšmę keistų į True. 
# 	Sukurkite klasę Krepšys, kuri turi statinę savybę vaisiai, kuri yra sąrašas. 
# Klasėje Krepšys sukurkite metodą pripildyti(), kuris savybę vaisiai užpildytų 20-timi vaisiaus objektų ir išrūšiuotų juos pagal vaisiaus dydį nuo didžiausio iki mažiausio. 
# Klasėje Krepšys sukurti statinį metodą isimti(), kuris iš vaisiai masyvo išimtų (ištrintų iš masyvo) pirmą (didžiausią) vaisių ir jį grąžintų. 
# Išėmus kelis vaisius ir vėl paleidus metodą papildyti(), jis turi padaryti tai ką sako metodo pavadinimas - papildyti masyvą iki pilno (20 elementų), o ne perrašyti visus vaisius iš naujo (tai galima stebėti pagal vaisių id). 
# Išorėje (globale) sukurti kintamąjį grauztukai kuris yra žodynas. 
# Iš krepšelio išimti vaisiai turi būti pridedami į šį objektą. Kaip raktus naudoti Vaisiaus objekte esančią id savybę. 
# Prieš patalpinant vaisių į grauztukai objektą, vaisius turi būti “prakąstas”, Vaisius objekte paleidžiant prakasti() metodą.

grauztukai = {}

class Vaisius() :
    prakastas = False

    def __init__(self) :
        self.dydis = random.randint(5, 25)
        self.id = random.randint(1000000, 9999999)
        
    def __str__(self) :
        return str({
            "dydis" : self.dydis,
            "id" : self.id,
            "prakastas" : self.prakastas
        })
    
    def __repr__(self) :
        return str({
            "dydis" : self.dydis,
            "id" : self.id,
            "prakastas" : self.prakastas
        })
    
    def prakasti(self) :
        self.prakastas = True


class Krepsys() :
    vaisiai = []

    def pripildyti(self) :
        for x in range(4) :
            self.vaisiai.append(Vaisius()) 

    def papildyti(self) :
        for x in range(len(self.vaisiai), 4) :
            self.vaisiai.append(Vaisius()) 

    def isimti(self) :
        # Guard (Sargo kūrimas)
        if len(self.vaisiai) == 0 :
            return

        dydziai = []

        for vaisius in self.vaisiai :
            dydziai.append(vaisius.dydis)

        didziausias = max(dydziai)

        for idx, vaisius in enumerate(self.vaisiai) :
            if vaisius.dydis == didziausias and vaisius.prakastas :
                grauztukai[vaisius.id] = vaisius
                del self.vaisiai[idx]

    def __str__(self) :
        return str({
            "vaisiai" : self.vaisiai
        })
    
    def __repr__(self) :
        return str({
            "vaisiai" : self.vaisiai
        })


krepsys = Krepsys()

# print(krepsys)

krepsys.pripildyti()

krepsys.vaisiai[0].prakasti()
krepsys.vaisiai[1].prakasti()
krepsys.vaisiai[2].prakasti()

krepsys.isimti()

krepsys.isimti()

krepsys.isimti()

krepsys.papildyti()

print(grauztukai)
