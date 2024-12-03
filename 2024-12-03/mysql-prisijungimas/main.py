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

    # Operacijos nurodymas:

    cur.execute("SELECT * FROM country_data")

    # Jeigu norime susigrąžinti daugiau nei vieną eilutę:
    data = cur.fetchall()
    # print(data)

    # Jeigu norime susigrąžinti tik vieną eilutę:
    cur.execute(f"SELECT country_name FROM country_data WHERE gdpp = 17100")
    
    # Grąžinamas vienas rinkinys:
    data = cur.fetchone()

    # print(data)

    number = input("Įveskite norimą bendrą vidaus produktą:")

    # Jeigu norime susigrąžinti tik vieną eilutę:
    cur.execute(f"SELECT country_name FROM country_data WHERE gdpp > {number}")

    data = cur.fetchall()
    
    for name in data :
        print(name[0])
        
except ConnectionError as e :
    # print(e)
    print("Prisijungimo klaida")
