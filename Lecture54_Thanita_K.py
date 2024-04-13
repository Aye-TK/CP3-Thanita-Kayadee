def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return menu()
    else:
        return print("Try again")

def menu():
    print("-----iShop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return selected()

def selected():
    userselected = int(input("Calculator >>"))
    if userselected == 1:
        cost = int(input("Price(THB)"))
        vat = 7
        result = cost + (cost * vat / 100)
        return print("Total :", result, "THB")
    elif userselected == 2:
        return print("Total :", price(), "THB")

def vat(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def price():
    price1 = int(input("First Product Price :"))
    price2 = int(input("Second Product Price :"))
    return  vat(price1 + price2)


print(login())



