def dict_add(diction):
    print(diction)
    dict_name = eval(diction)
    print(type(dict_name))
        
orders_list = []
with open("orders.txt", "r") as file:
    for i in file:
        orders_list.append(i)

# for i in orders_list:
#     print(i)
    
#blablabla
    
for i in orders_list:
    dict_add(i)
    # print("\n")
    # print(i)
    # print(type)
    # for key, val in i:
    #     print(f"{key}: {val}")
    
