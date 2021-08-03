import csv
import pymysql
import os


def import_orders():
    with open("orders.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            order_list.append(row)


def goodbye_exit():
    print("\nExit Options", "Choose option:", "[0] Return to Main Menu", "[1] Exit", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print("Goodbye")
        exit()


def main_menu():
    print("\nMain menu", "Choose option:", "[0] Exit", "[1] Products", "[2] Couriers", "[3] Orders", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        goodbye_exit()
    elif options == 1:
        product_menu()
    elif options == 2:
        courier_menu()
    elif options == 3:
        order_menu()
    else:
        print("\nEntry Error: Please try again")
        main_menu()


def product_menu():
    print("\nProduct Menu", "Choose Option:", "[0] Return To Main Menu", "[1] Print Products", "[2] Add Product",
          "[3] Update Product", "[4] Delete Product", sep="\n")
    options = int(input("Enter Number Here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print_products()
        product_menu()
    elif options == 2:
        add_product()
        product_menu()
    elif options == 3:
        update_product()
        product_menu()
    elif options == 4:
        delete_product()
        product_menu()
    else:
        print("\nEntry Error: Please Try Again")
        product_menu()


def print_products():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()

    for record in results:
        id = record[0]
        name = record[1]
        price = record[2]
        print(f"[{id}] {name}: £{price}")

    connection.close()


def add_product():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    name = str(input("Enter Product Name: "))
    price = float(input("Enter Price: "))

    cursor = connection.cursor()

    cursor.execute(f"""INSERT INTO products (product_id, product_name, price) 
        VALUES (NULL, '{name}', '{price}')
    """)

    connection.commit()
    connection.close()


def update_product():
    print_products()
    selection = int(input("Enter Number Here: "))

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()

    new_name = str(input("Enter New Product Name: "))
    new_price = input("Enter New Price: ")

    if new_name != "":
        cursor.execute(f"""
            UPDATE products
            SET product_name = '{new_name}'
            WHERE product_id = {selection}
        """)

    if new_price != "":
        cursor.execute(f"""
            UPDATE products
            SET price = {new_price}
            WHERE product_id = {selection}
        """)

    connection.commit()
    connection.close()


def delete_product():
    print_products()
    selection = int(input("Enter Number Here: "))
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()

    cursor.execute(f"""
            DELETE FROM products
            WHERE product_id = {selection}
        """)

    connection.commit()
    connection.close()


def courier_menu():
    print("\nCourier Menu", "Choose Option:", "[0] Return To Main Menu", "[1] Print Couriers", "[2] Add Courier",
          "[3] Update Courier", "[4] Delete Courier", sep="\n")
    options = int(input("Enter Number Here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print_couriers()
        courier_menu()
    elif options == 2:
        add_courier()
        courier_menu()
    elif options == 3:
        update_courier()
        courier_menu()
    elif options == 4:
        delete_courier()
        courier_menu()
    else:
        print("\nEntry Error: Please Try Again")
        courier_menu()


def print_couriers():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM couriers")
    results = cursor.fetchall()

    for record in results:
        id = record[0]
        name = record[1]
        phone = record[2]
        print(f"[{id}] {name}, {phone}")

    connection.close()


def add_courier():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    name = str(input("Enter Courier Name: "))
    phone = int(input("Enter Phone Number: "))

    cursor = connection.cursor()

    cursor.execute(f"""INSERT INTO couriers (courier_id, courier_name, courier_phone) 
        VALUES (NULL, '{name}', '{phone}')
    """)

    connection.commit()
    connection.close()


def update_courier():
    print_couriers()
    selection = int(input("Enter Number Here: "))
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()

    new_name = str(input("Enter New Courier Name: "))
    new_phone = input("Enter New Phone Number: ")

    if new_name != "":
        cursor.execute(f"""
            UPDATE couriers
            SET courier_name = '{new_name}'
            WHERE courier_id = {selection}
        """)

    if new_phone != "":
        cursor.execute(f"""
            UPDATE couriers
            SET courier_phone = {new_phone}
            WHERE courier_id = {selection}
        """)

    connection.commit()
    connection.close()


def delete_courier():
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


def order_menu():
    print("\nOrder Menu", "Choose option:", "[0] Return to Main Menu", "[1] Print Orders", "[2] Add Order",
          "[3] Update Customer Details", "[4] Update Order Status", "[5] Delete Order", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print_orders()
        order_menu()
    elif options == 2:
        add_order()
        order_menu()
    elif options == 3:
        update_order("customer")
        order_menu()
    elif options == 4:
        update_order("status")
        order_menu()
    elif options == 5:
        delete_order()
        order_menu()
    else:
        print("\nEntry Error: Please try again")
        order_menu()


def print_orders():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()

    for record in results:
        id = record[0]
        name = record[1]
        # address = record[2]
        # phone = record[3]
        courier = record[4]
        status = record[5]
        # basket = record[6]
        print(f"[{id}] Name: {name}, Courier:{courier}, Status:{status}")

    connection.close()


def add_order():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    name = str(input("Enter Customer Name: "))
    address = str(input("Enter Address: "))
    phone = int(input("Enter Phone Number: "))
    print_couriers()
    courier = int(input("Enter Courier: "))
    print_status()
    status = int(input("Enter Status: "))
    basket = 1

    cursor = connection.cursor()

    cursor.execute(f"""INSERT INTO orders (order_id, customer_name, customer_address, customer_phone, 
        courier_id, status_id, basket_id) 
        VALUES (NULL, '{name}', '{address}', '{phone}', '{courier}', '{status}', '{basket}')
    """)

    connection.commit()
    connection.close()


def update_order(fields):
    if fields == "customer":
        print_orders()
        selection = int(input("Enter Number Here: "))
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="password",
            database="mp_database"
        )

        cursor = connection.cursor()

        new_name = str(input("Enter New Name: "))
        new_address = str(input("Enter New Address: "))
        new_phone = input("Enter New Phone Number: ")

        if new_name != "":
            cursor.execute(f"""
                UPDATE orders
                SET customer_name = '{new_name}'
                WHERE order_id = {selection}
            """)

        if new_address != "":
            cursor.execute(f"""
                UPDATE orders
                SET customer_address = '{new_name}'
                WHERE order_id = {selection}
            """)

        if new_phone != "":
            cursor.execute(f"""
                UPDATE orders
                SET customer_phone = {new_phone}
                WHERE order_id = {selection}
            """)

        connection.commit()
        connection.close()

    elif fields == "status":
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
            SET status_id = {status}
            WHERE order_id = {selection}
        """)

        connection.commit()
        connection.close()


def delete_order():
    print_orders()
    selection = int(input("Enter Number Here: "))
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()

    cursor.execute(f"""
        DELETE FROM orders
        WHERE order_id = {selection}
    """)

    connection.commit()
    connection.close()


def print_status():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mp_database"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM status")
    results = cursor.fetchall()

    for record in results:
        id = record[0]
        status = record[1]
        print(f"[{id}] {status}")

    connection.close()


main_menu()
