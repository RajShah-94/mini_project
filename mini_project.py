def import_products():
        with open("products.txt", "r") as file_products:
            for i in file_products:
                products.append(i.strip("\n"))

def import_couriers():
        with open("couriers.txt", "r") as file_couriers:
            for i in file_couriers:
                couriers.append(i.strip("\n"))

def import_orders():
    with open("orders.txt", "r") as file:
        for i in file:
            order_list.append(i)

def main_menu():
    print("\nMain menu", "Choose option:", "[0] Save and Exit", "[1] Products", "[2] Couriers", "[3] Orders", sep = "\n")
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
    print("\nSave and Exit", "Choose option:", "[0] Return to Main Menu", "[1] Save and Exit", "[2] Save", "[3] Exit without Saving", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    if options == 1:
        with open("products.txt", "w") as file2:
            f = []
            for product in products:
                f.append(product)
            for i in f:
                file2.write(i + "\n")
        with open("couriers.txt", "w") as file3:
            f = []
            for courier in couriers:
                f.append(courier)
            for i in f:
                file3.write(i + "\n")
        print("\nSaved! Goodbye")
        exit()
        main_menu()
    elif options == 2:
        with open("products.txt", "w") as file2:
            f = []
            for product in products:
                f.append(product)
            for i in f:
                file2.write(i + "\n")
        with open("couriers.txt", "w") as file3:
            f = []
            for courier in couriers:
                f.append(courier)
            for i in f:
                file3.write(i + "\n")
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
    print("\nProduct Menu","Choose option:", "[0] Return to Main Menu", "[1] Print Products", "[2] Add Product", "[3] Update Product", "[4] Delete Product", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print(products)
        product_menu()
    elif options == 2:
        add_to_list(products,"product")
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
    print("\nCourier Menu","Choose option:", "[0] Return to Main Menu", "[1] Print Couriers", "[2] Add Courier", "[3] Update Courier", "[4] Delete Courier", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        print(couriers)
        courier_menu()
    elif options == 2:
        add_to_list(couriers,"courier")
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
    print("\nOrder Menu","Choose option:", "[0] Return to Main Menu", "[1] Print Orders", "[2] Add Order", "[3] Update Order", "[4] Delete Order", sep = "\n")
    options = int(input("Enter number here: "))
    if options == 0:
        main_menu()
    elif options == 1:
        for i in order_list:
            print("\n")
            print(i)
        order_menu()
    # elif options == 2:
    #     add_to_list(orders,"courier")
    #     courier_menu()
    # elif options == 3:
    #     update_list(couriers, "courier")
    #     courier_menu()
    # elif options == 4:
    #     delete_from_list(couriers, "courier")
    #     courier_menu()
    else:
        print("\nEntry Error: Please try again")
        order_menu()

def add_to_list(list, name): #list is imported list[], name is list name
    new_item = str(input(f"Enter new {name}: "))
    list.append(new_item)
    return(list)

def update_list(list, name): #list is imported list[], name is list name
    print(f"\nChose {name} to update:")
    print(f"[0] Return to {name.capitalize()} Menu")
    for item in list:
        print(f"[{list.index(item) + 1}] {item}")
    options = int(input("Enter number here: "))
    if options == 0:
        return(list)
    elif (options >= 0) and (options <= len(list)):
        print(f"You have chosen: {list[options -1]}")
        updated_item = str(input(f"Enter updated {name}: "))
        list[options -1] = updated_item
        return(list)
    else:
        print("\nEntry Error: Please try again")
        return(list)

def delete_from_list(list, name): #list is imported list[], name is list name
    print(f"\nChose {name} to delete:")
    print(f"[0] Return to {name.capitalize()} Menu")
    for item in list:
        print(f"[{list.index(item) + 1}] {item}")
    options = int(input("Enter number here: "))
    if options == 0:
        return(list)
    elif (options >= 0) and (options) <= len(list):
        print(f"You have chosen: {list[options - 1]}. Are you sure you want to continue?")
        confirmation_dialogue = str(input("[Y] for yes, [N] for no: "))
        if confirmation_dialogue == "Y" or confirmation_dialogue == "y":
            print(f"You have deleted {list[options - 1]}")
            list.remove(list[options -1])
            return(list)
        elif confirmation_dialogue == "N" or confirmation_dialogue == "n":
            return(list)
        else:
            print(f"\nEntry Error: Returning to {name.capitalize()} Menu")
            return(list)
    else:
        print("\nEntry Error: Please try again")
        return(list)
    
products = []
couriers = []
order_list = []
import_products()
import_couriers()
import_orders()
main_menu()