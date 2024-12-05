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

rezimas = input("Įveskite raidę n jeigu norite norite pridėti naują filmą. Priešingu atveju bus grąžinti visi filmai duomenų bazėje.")

if rezimas == 'n' :
    # Naujo duomens pridejimas:7
    pavadinimas = input("Įveskite pavadinimą: ")
    aprasymas = input("Įveskite aprašymą: ")
    zanras = input("Įveskite žanrą: ")

    # Nurodome sql komandinę eilutę
    cur.execute(f"INSERT INTO filmas (pavadinimas, aprasymas, zanras) VALUES ('{pavadinimas}', '{aprasymas}', '{zanras}')")
    # # Užregistruojame pakeitimus
    cnx.commit()
else :
    # Visu filmu sarasas:
    cur.execute("SELECT * FROM filmas")

    data = cur.fetchall()

    for filmas in data :
        print(filmas)


# # Prisijungimo uždarymas
cnx.close()

