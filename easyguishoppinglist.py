from easygui import *

shopping_list = {
    "banana": {"price": 5, "quantity": 5},
    "watermelon": {"price": 9, "quantity": 2},
    "apple": {"price": 5, "quantity": 4}
}

func = "a"
go = True

def adding (shopping_list, item, price, quantity):
    if item in list:
        sure = buttonbox("Item in list. Are you sure you wish to change price and quantity?", "Are you sure?", choices = ("Yes", "No"))
        if sure == "Yes":
            shopping_list[item] = {"price": price, "quantity": quantity}
            msgbox("Item price and quantity updated successfully!")
        else:
            msgbox("Price and quantity not updated")
    else:
        shopping_list[item] = {"price": price, "quantity": quantity}
        msgbox("Item added")
    return shopping_list

def main_menu():
    func = enterbox("Welcome. What do you wish to do?", "Main Menu", choices = ("Add items", "remove items", "see total price", "see items price", "exit"))
    return func

def total_price(shopping_list):
    total = 0
    for item in shopping_list:
        total += shopping_list[item]["price"] * shopping_list[item]["quantity"] 
    msgbox(f"The price is {total}")

def item_price(shopping_list, item):
    if item in shopping_list:
        msgbox(f"The price of {item} is ${shopping_list[item]['price']} and you have {shopping_list[item]['quantity']} of them for a total of ${shopping_list[item]['price'] * shopping_list[item]['quantity']}.")
    else:
        sure = enterbox("This item is not in your list. Do you want to add it instead?", "Are you sure", choices = ("Yes", "No"))
        if sure == "Yes":
            price = numberbox("Enter the price of the item without the dollar sign: ", "Price")
            quantity = integerbox("Enter the quantity of the item: ", "Quantity")
            shopping_list[item] = {"price": price, "quantity": quantity}
            msgbox("Item added")
        else:
            msgbox("Nothing changed")
    return shopping_list

def remove(shopping_list, item):
    pass


while func != "" or func != "exit":
    pass
