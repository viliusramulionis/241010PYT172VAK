data = open("u2.txt", "r")

data = data.readlines()

sokejai = int(data[0].split()[0])
teisejai = int(data[0].split()[1])

print(sokejai, teisejai)

print(data[1:])

for idx in range(1, sokejai * 3, 3) :
    print(data[idx].replace("\n", ""), data[idx + 1], data[idx + 2])