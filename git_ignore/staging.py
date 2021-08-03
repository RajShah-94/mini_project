print_orders()
selection = int(input("Enter Number Here: "))
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mp_database"
)

cursor = connection.cursor()

print_status()
status = int(input("Enter Status: "))

cursor.execute(f"""
    UPDATE orders
    SET status = '{status}'
    WHERE order_id = {selection}
""")

connection.commit()
connection.close()