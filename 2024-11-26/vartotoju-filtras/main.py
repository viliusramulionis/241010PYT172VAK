# Išfiltruokite vartotojus kurie neturi gimimo metų.

data = open("vartotojai.txt", "r")

for line in data.readlines()[1:] :
    l = line.split(";")
    
    if l[3] :
        print(line, end = "")