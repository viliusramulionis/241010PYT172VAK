data = open("u2.txt", "r")

data = data.readlines()

sokejai = int(data[0].split()[0])
teisejai = int(data[0].split()[1])

def eilutesSumavimas(eilute) :
    eilute = eilute.replace("\n", "").split()
    
    maziausias = min(list(map(int, eilute)))
    didziausias = max(list(map(int, eilute)))

    return sum(list(map(int, eilute))) - maziausias - didziausias

rezultatas = []

for idx in range(1, sokejai * 3, 3) :
    vardai = data[idx].replace("\n", "")
    technika = eilutesSumavimas(data[idx + 1])
    artistiskumas = eilutesSumavimas(data[idx + 2])

    rezultatas.append([vardai, technika + artistiskumas])

    # rez.write(f"{vardai} {technika + artistiskumas}\n")
# rezultatas.sort(reverse=True)

rez = open("u2rez.txt", "a")

rezultatas = sorted(rezultatas, reverse=True, key=lambda value : value[1])

for eilute in rezultatas : 
    rez.write(f"{eilute[0]}\t{eilute[1]}\n")


