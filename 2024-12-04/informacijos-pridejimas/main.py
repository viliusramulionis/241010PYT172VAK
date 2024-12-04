import mysql.connector

cnx = None

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="filmai")
except :
    # print(e)
    print("Prisijungimo klaida")


# Kursoriaus sukūrimas
cur = cnx.cursor()

pavadinimas = input("Įveskite pavadinimą: ")
aprasymas = input("Įveskite aprašymą: ")
zanras = input("Įveskite žanrą: ")

# Nurodome sql komandinę eilutę
cur.execute(f"INSERT INTO filmas (pavadinimas, aprasymas, zanras) VALUES ('{pavadinimas}', '{aprasymas}', '{zanras}')")

# Užregistruojame pakeitimus
cnx.commit()

# Prisijungimo uždarymas
cnx.close()

