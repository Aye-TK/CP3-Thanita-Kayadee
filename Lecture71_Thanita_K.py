menuList = []
priceList = []
def showBill():
    print('-----My Food-----')
    for num in range(len(menuList)):
        print(menuList[num], priceList[num])
    print("Total", int(priceList[num]), "THB")

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()


