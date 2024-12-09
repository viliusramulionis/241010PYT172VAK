# Paleista programa atspausdina visus įrašus esančius lentelėje.
# Tuomet vartotojo paprašome įvesti norima veiksmą:
# N - Naujas įrašas
# E - Įrašo redagavimas
# D - Įrašo ištrynimas
# Jeigu pasirenkama E arba D raide, tuomet paprašoma įvesti norimo įrašo ID.
# Jeigu vykdomas redagavimo veiksmas, tuomet paprašoma įvesti stulpelius kuriuos norima redaguoti ir vėliau stulpelių reikšmes.
# Jeigu norima tik ištrinti įrašą, užtenka tik įrašo ID.


# Pralėskite programą:
# Leiskite ištrinti tik tuos įrašus kurie turi žanrą "Country"
# Leiskite įrašyti tik tas dainas kurių atlikėjo pavadinime yra vardas "Virgis"
# Dainų pavadinimuose išfiltruokite žodį "American" vietoje jų palikdami "Lithuanian"

import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="spotify")
    
    # Kursoriaus sukūrimas
    cur = cnx.cursor()
    
    rezimas = input("Įveskite ką norėtumėte atlikti N - Naujas įrašas, E - Redagavimas, D - Įrašo ištrynimas, S - Dainų sąrašas: ")
    
    # if rezimas.lower() == "d" :
    #     print("Trynimas")
    
    # elif rezimas.lower() == "e" :
    #     print("Redagavimas")
    
    # elif rezimas.lower() == "n" :
    #     print("Naujas irasas")

    # else :
    #     cur.execute("SELECT * FROM dainos")

    #     for daina in cur.fetchall() :
    #         print(daina)

    match rezimas.lower() :
        case "d" :
            id = input("Įveskite įrašo ID: ")

            cur.execute(f"DELETE FROM dainos WHERE id = {id}")

            cnx.commit()
        case "e" :
            id = input("Įveskite įrašo ID: ")
            stulpeliai = input("Įveskite norimus redaguoti stulpelius atskirtus kableliais (pavadinimas, atlikejas, zanras): ")
            reiksmes = input("Įveskite reikšmes atskirtas kableliais: ")

            stulpeliai = stulpeliai.split(",")
            reiksmes = reiksmes.split(",")

            set = ""

            for idx in range(0, len(stulpeliai)) :
                set += f"{stulpeliai[idx]} = '{reiksmes[idx]}',"

            cur.execute(f"UPDATE dainos SET {set[:-1]} WHERE id = {id}")
            
            cnx.commit()
        case "n" :
            pavadinimas = input("Įveskite dainos pavadinimą: ")
            atlikejas = input("Įveskite dainos atlikėją: ")
            zanras = input("Įveskite dainos žanrą: ")

            cur.execute(f"INSERT INTO dainos (pavadinimas, atlikejas, zanras) VALUES('{pavadinimas}', '{atlikejas}', '{zanras}')")
            
            cnx.commit()
        case _ :
            cur.execute("SELECT * FROM dainos")

            for daina in cur.fetchall() :
                print(daina)

    # cnx.commit()

    cnx.close()
except :
    # print(e)
    print("Prisijungimo klaida")



