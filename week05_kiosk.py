# ISHS CAFFE
# Americano 1500, Latte 2500원

beverage = ["americano", "latte"]
prices = [1500, 2500]

while True:
    menu = int(input("1) Americano   2) Latte    3) End order button: "))
    if menu == 3:
        print("Exit program")
        break
    elif menu == 1:
        print("You ordered Americano coffee. The price is 1,500 won")
    elif menu == 1:
        print("You ordered Americano cafe latte. The price is 2,500 won")
