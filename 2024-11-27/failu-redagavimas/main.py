# a - append
# r - read
# w - write

data = open("pomegiai.txt", "a")

# data.write("Hello World")

zinute = input("Įveskite žinutę")

# write() metodas irašo į failą norimą informaciją
data.write(zinute + "\n")

