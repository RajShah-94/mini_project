import pymysql
import os

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mp_database"
)

#customer_name,customer_address,customer_phone,courier,status,items
selection = int(input("Enter Number Here: "))

cursor = connection.cursor()
# cursor.execute('CREATE DATABASE mp_database')
# cursor.execute('USE mp_database')
# cursor.execute("""CREATE TABLE orders (
#     basket_id int,
#     product_id int,
#     PRIMARY KEY(basket_id),
#     FOREIGN KEY(product_id) REFERENCES products(product_id)
#     )
# """)

# FOREIGN KEY(status_id) REFERENCES status(status_id),
# FOREIGN KEY(basket_id) REFERENCES basket(basket_id)


# cursor.execute("""INSERT INTO couriers (courier_id, courier_name, courier_phone) VALUES (NULL,"Alice", 972166985)""")
# cursor.execute("""INSERT INTO couriers (courier_id, courier_name, courier_phone) VALUES (NULL,"Bob", 972166985)""")
# cursor.execute("""INSERT INTO couriers (courier_id, courier_name, courier_phone) VALUES (NULL,"Charli", 972166985)""")
# cursor.execute("SHOW TABLES")

# cursor.execute("SELECT * FROM couriers")
# results = cursor.fetchall()
#
# for record in results:
#     id=record[0]
#     name=record[1]
#     phone=record[2]
#     print(f"[{id}] {name}, {phone}")
# new_name = str(input("Enter New Product Name: "))
# new_price = float(input("Enter New Price: "))
#
# if new_name != "":
#     cursor.execute(f"""
#         UPDATE products
#         SET product_name = '{new_name}'
#         WHERE product_id = 1
#     """)
#
# if new_price != "":
#     cursor.execute(f"""
#         UPDATE products
#         SET price = {new_price}
#         WHERE product_id = 1
#     """)

cursor.execute(f"""
    DELETE FROM products
    WHERE product_id = {selection}
""")

connection.commit()
connection.close()