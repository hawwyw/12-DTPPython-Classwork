shopping_list = {
    "Bannana": 5,
    "Watermelon": 6,
    "Apple": 5
}
func = 1
go = True

def adding(shopping_list, item, price):
    if item in shopping_list:
        sure = input(f"Item is already in list. Are you sure you want to change the value of {item}. Enter 'Yes' for yes and anything else for no")
        if sure == "Yes":
            shopping_list [item] = price
            print("Price changed")
        else:
            print("Price not changed")
    else:
        shopping_list [item] = price
        print("Item added")
    return shopping_list

def price_check(shopping_list):
    total = sum(shopping_list.values())
    print(f"The price is {total}")

def item_price(shopping_list, item):
    if item in shopping_list:
        print(f"The price of {item} is {shopping_list[item]}")
    else:
        sure = input("This item is not in your list. Do you want to add it instead? Enter 'Yes' if you do and anything else if you don't: ")
        if sure == "Yes":
            go = True
            while go:
                try:
                    go = False
                    price = float(input("Enter the price of the item without the dollar sign: "))
                except:
                    go = True
                    print("Enter a real number")
            
            shopping_list[item] = price
            print("Item added")
        else:
            print("Item not added")
    return shopping_list

def remove (shopping_list, item):
    shopping_list.pop(item)
    return shopping_list


while func != 5:
    func = ""
    go = True
    while func == "":
        try:
            func = int(input("Enter what function you want to use. 1 for adding an item, 2 for checking the total price, 3 for checking an items price, 4 to remove an item and 5 to quit: "))
        except:
            func = ""
            print("Enter a number between 1 and 5")
    if func == 1:
        item = str(input("Enter the name of the item you wish to add (caps sensitive): "))
        while go:
            try:
                price = float(input("Enter the price of the item: "))
                go = False
            except:
                go = True
                print("Enter a real number")
        shopping_list = adding(shopping_list, item, price)

    elif func == 2:
        price_check(shopping_list)

    elif func == 3:
        item = str(input("What item do you wish to check the price of :"))
        item_price(shopping_list, item)
    elif func == 4:
        item = str(input("Enter the item you wish to remove from the list: "))
        if item in shopping_list:
            shopping_list = remove(shopping_list, item)
            print("Item removed")
        else:
            print("Item is not in list")

print("Thank you!")
