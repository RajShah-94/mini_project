import csv
import pymysql
import os


def import_orders():
    with open("orders.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            order_list.append(row)


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


def goodbye_exit():
    print("\nExit Options", "Choose option:", "[0] Return to Main Menu", "[1] Exit", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print("Goodbye")
        exit()


def product_menu():
    print("\nProduct Menu", "Choose option:", "[0] Return to Main Menu", "[1] Print Products", "[2] Add Product",
          "[3] Update Product", "[4] Delete Product", sep="\n")
    options = int(input("Enter number here: "))
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
        print("\nEntry Error: Please try again")
        product_menu()


def courier_menu():
    print("\nCourier Menu", "Choose option:", "[0] Return to Main Menu", "[1] Print Couriers", "[2] Add Courier",
          "[3] Update Courier", "[4] Delete Courier", sep="\n")
    options = int(input("Enter number here: "))
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
        print("\nEntry Error: Please try again")
        courier_menu()


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
          "[3] Update Order", "[4] Delete Order", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        for i in order_list:
            print(f"Customer: {i['customer_name']}, Order Status: {i['status']}")
        order_menu()
    elif options == 2:
        add_to_orders(order_list)
        order_menu()
    elif options == 3:
        selected = choose_order()
        update_orders(selected)
        order_menu()
    elif options == 4:
        selected = choose_order()
        order_list.pop(selected)
        order_menu()
    else:
        print("\nEntry Error: Please try again")
        order_menu()


def add_to_orders(list_name):
    print("Enter new order details")
    name = str(input("Enter Name: "))
    address = str(input("Enter Address: "))
    phone = str(input("Enter Phone No: "))
    courier = int(input("Courier No: "))
    status = "Preparing"
    items = ""
    new_order = {"customer_name": name, "customer_address": address, "customer_phone": phone, "courier": courier,
                 "status": status, "items": items}
    list_name.append(new_order)


def choose_order():
    j = 0
    for i in order_list:
        print(f"[{j}] {i['customer_name']}")
        j += 1
    selection = int(input("Enter Number Here: "))
    return order_list[selection]


def update_orders(order_dict):
    print("Select field to update", "[0] Return to previous menu", f"[1] Name: {order_dict['customer_name']}",
          f"[2] Address: {order_dict['customer_address']}", f"[3] Phone Number: {order_dict['customer_phone']}",
          f"[4] Order Status: {order_dict['status']}", sep="\n")
    selection = int(input("Enter Field Number: "))
    if selection == 0:
        # order_menu()
        return
    elif selection == 1:
        new_name = str(input("Enter New Name: "))
        if new_name != "":
            order_dict['customer_name'] = new_name
    elif selection == 2:
        new_address = str(input("Enter New Address: "))
        if new_address != "":
            order_dict['customer_address'] = new_address
    elif selection == 3:
        new_phone = str(input("Enter New Phone Number: "))
        if new_phone != "":
            order_dict['customer_phone'] = new_phone
    elif selection == 4:
        new_status = str(input("Enter New Order Status: "))
        if new_status != "":
            order_dict['status'] = new_status


main_menu()
