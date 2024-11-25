# open funkcija atidaro failą,
# pirmas parametras kelias iki failo
# antras parametras rėžimo pasirinkimas
# r - read (susigrąžinti failo turinį)
# w - write (perrašyti failo turinį)
# a - append (failo papildymas)

data = open("vardai.txt", "r")

new_data = []

for eilute in data :
    e = eilute.replace("\n", "").split()
    e[1] = e[1].upper()
    
    new_data.append(" ".join(e))

print(new_data)
