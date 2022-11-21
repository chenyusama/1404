total = 0

number_items = int(input("Number of items:"))
if number_items < 0:
    print("Invalid number")
else:
    for i in range(1, number_items+1):
        Price = float(input("Price of item: "))
        while Price < 0:
            print("Invalid number of items!")
            Price = float(input("Price of item: "))
        if Price > 0:
            total = total+Price
    print("Total price for {} items is ${}".format(number_items, total))



