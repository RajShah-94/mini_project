import csv

test_field_names = ["customer_name", "customer_address", "customer_phone", "courier", "status"]
test_list = []

# with open("orders.txt", "r") as file:
#     for i in file:
#         dict = eval(str(i))
#         test_list.append(dict)
#
# with open("test.csv", "w") as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=test_field_names)
#     writer.writeheader()
#     for row in test_list:
#         writer.writerow(row)

with open("test.csv", "r") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        test_list.append(row)


# for i in test_list:
#     print(f"Customer: {i['customer_name']}, Order Status: {i['status']}")


# def add_to_orders(list_name):
#     print("Enter new order details")
#     name = str(input("Enter Name: "))
#     address = str(input("Enter Address: "))
#     phone = str(input("Enter Phone No: "))
#     courier = int(input("Courier No: "))
#     status = "Preparing"
#     items = ""
#     new_order = {"customer_name": name, "customer_address": address, "customer_phone": phone, "courier": courier,
#                  "status": status, "items": items}
#     list_name.append(new_order)
#
#
# add_to_orders(test_list)

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


def choose_order():
    j = 0
    for i in test_list:
        print(f"[{j}] {i['customer_name']}")
        j += 1
    selection = int(input("Enter Number Here: "))
    return test_list[selection]

# def update_orders(order_dict):
#     i = 1
#     print("Select field to update", "[0] Return to previous menu", sep="\n")
#     for k, v in order_dict.items():
#         print(f"[{i}] {k}")
#         i += 1
#     selection = int(input("Enter Selection Here: ")) - 1
#     if selection == -1:
#         return
#     elif selection == 0:


x = choose_order()
# print(test_list)
# def import_orders():
#     with open("test.csv", "r") as file:
#         csv_file = csv.DictReader(file)
#         for row in csv_file:
#             order_list.append(row)
