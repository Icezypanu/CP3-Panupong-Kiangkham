menuList = []
priceList = []


def showBill():
    print("---- My Food----")
    sum_price = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        sum_price += int(priceList[number])
    print('Food Price:',sum_price)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
