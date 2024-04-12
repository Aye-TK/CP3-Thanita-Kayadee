usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "Candy" and passwordInput == "1234":
    print("--------Welcome--------")
    print("Menu")
    print("______________________")
    print("1. water    20  THB")
    print("2. cake     120 THB")
    print("3. juice    190  THB")
    selected = input("order :")
    if selected == "water" :
        num = int(input("amount :"))
        result = num * 20
        print("total price :", result, "THB")
    elif selected == "cake" :
        num = int(input("amount :"))
        result = num * 120
        print("total price :", result, "THB")
    elif selected == "juice" :
        num = int(input("amount :"))
        result = num * 190
        print("total price :", result, "THB")
else:
    print("Oops!! something wrong, please try again")
