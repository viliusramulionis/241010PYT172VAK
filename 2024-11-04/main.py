# kintamasis = "Labas"

if 10 == 10 :
    kintamasis = "Viso"

print(kintamasis)

# Jeigu kintamasis yra sukurtas funkcijoje jis yra patalpinamas į funkcijos apimtį (local scope)

def funkcija() :
    pasisveikinimas = "Labas"

# Toks kintamasis yra neprieinamas (gaunama klaida)
# print(pasisveikinimas)

zinute = ""

def kitaFunkcija() :
    zinute = "Neperduoti jokie argumentai"

print(zinute)

# Visi kintamieji kurie deklaruojami už funkcijos ribų yra globalūs (global scrope)


zinute = ""

def kitaFunkcija() :
    global zinute
    
    zinute = "Neperduoti jokie argumentai"


kitaFunkcija()
print(zinute)


def kitaFunkcija() :
    return "Neperduoti jokie argumentai"

zinute = kitaFunkcija()
print(zinute)


# Funkcijų deklaravimas yra asinchroniškas
def konfiguracija():
    print("Konfiguracijos paleidimas")

def duomenuStruktura():
    print("Duomenu struktura")
    duomenuBazesServeris()
    modeliuStruktura()

def routerioPrijungimas():
    print("Prijungiamas routeris")

def duomenuBazesServeris() :
    global pin
    print("PINAS gautas", pin)
    print('Prijungiamas duombazes serveris')

def modeliuStruktura() :
    print("Prijungiami modeliai")

pin = "1234"

def serveris() :
    # Serverio paleidimas
    konfiguracija()
    duomenuStruktura()
    routerioPrijungimas()

serveris()