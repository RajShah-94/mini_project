print_couriers()
selection = int(input("Enter Number Here: "))
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mp_database"
)

cursor = connection.cursor()

cursor.execute(f"""
    DELETE FROM couriers
    WHERE courier_id = {selection}
""")

connection.commit()
connection.close()