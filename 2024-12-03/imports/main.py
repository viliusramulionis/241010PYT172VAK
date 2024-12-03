import skaiciai
# Vienos funkcijos importavimas
from skaiciai import suma
# Kelių funkcijų importavimas
from skaiciai import atimtis, dalyba
# Importuojamos funkcijos pervadinimas norint išvengti duplikatų:
from operacijos import suma as formatuotaSuma

print(skaiciai.suma(15, 25))
print(skaiciai.atimtis(15, 25))
print(skaiciai.daugyba(15, 25))
print(skaiciai.dalyba(15, 25))

print(suma(25, 88))
print(atimtis(15, 5))
print(dalyba(15, 5))

print(formatuotaSuma(88, 55))