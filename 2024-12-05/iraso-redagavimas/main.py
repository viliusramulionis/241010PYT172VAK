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

cur.execute("UPDATE filmas SET pavadinimas = 'Betmenas Sugrįžimas', aprasymas = 'Kristoferio Nolano filmas' WHERE id = 7")

cnx.commit()