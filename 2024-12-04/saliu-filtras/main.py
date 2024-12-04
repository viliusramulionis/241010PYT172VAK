import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="naujas")
    
    # Kursoriaus sukūrimas
    cur = cnx.cursor()

    # Suraskite visas šalis kurių vidutinės pajamos yra didesnės nei x, o bendras vidaus produktas mažesnis nei x;

    def first_example() :
        pirmas = input("Įveskite vidutines pajamas:")
        antras = input("Įveskite bendrą vidaus produktą:")

        cur.execute(f"SELECT country_name FROM country_data WHERE income > {pirmas} AND gdpp < {antras}")

        data = cur.fetchall()

        for name in data :
            print(name)

    # Suraskite šalių infliacijos indeksą, kurių pavadinime yra raidė "x".
    def second_example() :
        pavadinimas = input("Įveskite šalies pavadinimą: ")

        cur.execute(f"SELECT inflation FROM country_data WHERE country_name LIKE '%{pavadinimas}%'")

        data = cur.fetchall()

        for index in data :
            print(index)

    # second_example()
    # Suraskite šalių infliacijos indeksą, kurių pavadinime yra raidė "x", bet vidutinė gyvenimo trukmė yra mažesnė nei x metų.
    def third_example() :
        pavadinimas = input("Įveskite šalies pavadinimą: ")
        trukme = input("Įveskite vidutinę gyvenimo trukmę: ")

        cur.execute(f"SELECT inflation FROM country_data WHERE country_name LIKE '%{pavadinimas}%' AND life_expectancy < {trukme}")

        data = cur.fetchall()

        for index in data :
            print(index)

    third_example()

except ConnectionError as e :
    # print(e)
    print("Prisijungimo klaida")
