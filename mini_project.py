import csv


def import_products():
    with open("products.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            products_list.append(row)


def import_couriers():
    with open("couriers.txt", "r") as file_couriers:
        for i in file_couriers:
            couriers_list.append(i.strip("\n"))


def import_orders():
    with open("orders.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            order_list.append(row)


def main_menu():
    print("\nMain menu", "Choose option:", "[0] Save and Exit", "[1] Products", "[2] Couriers", "[3] Orders", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        save_exit()
    elif options == 1:
        product_menu()
    elif options == 2:
        courier_menu()
    elif options == 3:
        order_menu()
    else:
        print("\nEntry Error: Please try again")
        main_menu()


def save_exit():
    print("\nSave and Exit", "Choose option:", "[0] Return to Main Menu", "[1] Save and Exit", "[2] Save",
          "[3] Exit without Saving", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    if options == 1:
        with open("products.csv", "w") as products_file:
            writer = csv.DictWriter(products_file, fieldnames=products_fieldnames)
            writer.writeheader()
            for row in products_file:
                writer.writerow(row)
        with open("couriers.csv", "w") as couriers_file:
            writer = csv.DictWriter(couriers_file, fieldnames=couriers_fieldnames)
            writer.writeheader()
            for row in couriers_file:
                writer.writerow(row)
        with open("orders.csv", "w") as orders_file:
            writer = csv.DictWriter(orders_file, fieldnames=orders_fieldnames)
            writer.writeheader()
            for row in orders_list:
                writer.writerow(row)
        print("\nSaved! Goodbye")
        exit()
        main_menu()
    elif options == 2:
        with open("products.csv", "w") as products_file:
            writer = csv.DictWriter(products_file, fieldnames=products_fieldnames)
            writer.writeheader()
            for row in products_file:
                writer.writerow(row)
        with open("couriers.csv", "w") as couriers_file:
            writer = csv.DictWriter(couriers_file, fieldnames=couriers_fieldnames)
            writer.writeheader()
            for row in couriers_file:
                writer.writerow(row)
        with open("orders.csv", "w") as orders_file:
            writer = csv.DictWriter(orders_file, fieldnames=orders_fieldnames)
            writer.writeheader()
            for row in orders_list:
                writer.writerow(row)
        print("\nSaved!")
        main_menu()
    elif options == 3:
        print("Are you sure? All changes from this session will be lost!")
        confirmation_dialogue = str(input("[Y] for yes, [N] for no: "))
        if confirmation_dialogue == "Y" or confirmation_dialogue == "y":
            print("Goodbye")
            exit()
        elif confirmation_dialogue == "N" or confirmation_dialogue == "n":
            main_menu()
        else:
            print("\nEntry Error: Returning to Product Menu")
            main_menu()
    else:
        print("\nEntry Error: Returning to Product Menu")
        main_menu()


def product_menu():
    print("\nProduct Menu", "Choose option:", "[0] Return to Main Menu", "[1] Print Products", "[2] Add Product",
          "[3] Update Product", "[4] Delete Product", sep="\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        for i in products_list:
            print(f"{i['name']}: £{i['price']}")
        product_menu()
    elif options == 2:
        add_to_list(products, "product")
        product_menu()
    elif options == 3:
        update_list(products, "product")
        product_menu()
    elif options == 4:
        delete_from_list(products, "product")
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
        for i in couriers_list:
            print(f"{i['name']}: £{i['phone']}")
        courier_menu()
    elif options == 2:
        add_to_list(couriers, "courier")
        courier_menu()
    elif options == 3:
        update_list(couriers, "courier")
        courier_menu()
    elif options == 4:
        delete_from_list(couriers, "courier")
        courier_menu()
    else:
        print("\nEntry Error: Please try again")
        courier_menu()


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


def add_to_list(list, name):  # list is imported list[], name is list name
    new_item = str(input(f"Enter new {name}: "))
    list.append(new_item)
    return list


def update_list(list, name):  # list is imported list[], name is list name
    print(f"\nChose {name} to update:")
    print(f"[0] Return to {name.capitalize()} Menu")
    for item in list:
        print(f"[{list.index(item) + 1}] {item}")
    options = int(input("Enter number here: "))
    if options == 0:
        return list
    elif (options >= 0) and (options <= len(list)):
        print(f"You have chosen: {list[options - 1]}")
        updated_item = str(input(f"Enter updated {name}: "))
        list[options - 1] = updated_item
        return list
    else:
        print("\nEntry Error: Please try again")
        return list


def delete_from_list(list, name):  # list is imported list[], name is list name
    print(f"\nChose {name} to delete:")
    print(f"[0] Return to {name.capitalize()} Menu")
    for item in list:
        print(f"[{list.index(item) + 1}] {item}")
    options = int(input("Enter number here: "))
    if options == 0:
        return list
    elif (options >= 0) and options <= len(list):
        print(f"You have chosen: {list[options - 1]}. Are you sure you want to continue?")
        confirmation_dialogue = str(input("[Y] for yes, [N] for no: "))
        if confirmation_dialogue == "Y" or confirmation_dialogue == "y":
            print(f"You have deleted {list[options - 1]}")
            list.remove(list[options - 1])
            return list
        elif confirmation_dialogue == "N" or confirmation_dialogue == "n":
            return list
        else:
            print(f"\nEntry Error: Returning to {name.capitalize()} Menu")
            return list
    else:
        print("\nEntry Error: Please try again")
        return list


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


products_list = []
couriers_list = []
order_list = []
products_fieldnames = ["name", "price"]
couriers_fieldnames = ["name", "phone"]
orders_fieldnames = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
import_products()
import_couriers()
import_orders()
main_menu()
