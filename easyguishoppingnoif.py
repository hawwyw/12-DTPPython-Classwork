from easygui import *

shopping_list = {
    "banana": {"price": 5, "quantity": 5},
    "watermelon": {"price": 9, "quantity": 2},
    "apple": {"price": 5, "quantity": 4}
}

go = True

def adding (shopping_list):
    item = enterbox("What item do you wish to add?", "Item")
    go = True
    while go:
        try:
            price = float(enterbox("How much does it cost? (Without dollar sign)", "Price"))
            go = False
        except:
            go = True
            msgbox("Enter a valid number", "Enter a number")
    quantity = integerbox("How many items do you wish to add?", "Quantity")
    shopping_list[item] = {"price": price, "quantity": quantity}
    msgbox("Item added")
    return shopping_list

def main_menu():
    func = buttonbox("Welcome. What do you wish to do?", "Main Menu", choices = ["add items", "remove items", "see total price", "see items price", "print list", "exit"])
    return func

def total_price(shopping_list):
    total = 0
    for item in shopping_list:
        item_price = shopping_list[item]["price"]
        item_quantity = shopping_list[item]["quantity"]
        total += item_quantity * item_price
    msgbox(f"The total price is ${total}")

def item_price(shopping_list):
    shopping_keys = list(shopping_list.keys())
    item = choicebox("What item do you want to check the price of?", "Item for price check", choices = shopping_keys)
    item_price = shopping_list[item]['price'] 
    item_quantity = shopping_list[item]['quantity']
    msgbox(f"The price of each {item} is ${shopping_list[item]['price']} and you have {shopping_list[item]['quantity']} of them for a total of ${item_price * item_quantity}.", "Price Inquiry")

def remove(shopping_list):
    shopping_keys = list(shopping_list.keys())
    if len(shopping_keys) < 2:
        sure = buttonbox(item, "is the only item left, do you want to remove it?", title = "Are you sure", choices = ("Yes", "No"))
        if sure == "Yes":
            shopping_list.pop(item)
    else:
        item = choicebox("What item do you want to remove?", "Remove an item", choices = shopping_keys)
        shopping_list = remove(shopping_list, item)
        shopping_list.pop(item)
    msgbox("Item removed from list")
    return shopping_list

def print_list(shopping_list):
    shopping_keys = list(shopping_list)
    item = choicebox("Shopping list", "Your list", choices = shopping_keys)

def exit():
    return False

function_list = {
    "main menu": main_menu(),
    "add items": adding(shopping_list),
    "remove items": remove(shopping_list),
    "see total price": total_price(shopping_list),
    "print list": print_list(shopping_list),
    "see items price": item_price(shopping_list),
    "exit": exit()
}
choice = "main menu"
while True:
    get_item = function_list[choice]