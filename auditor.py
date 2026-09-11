inventory = 0

while True:
    stock_quantity = input("Enter a stock quantity: ")
    if stock_quantity == "quit":
        break
    if not stock_quantity.isdigit():
        print("The stock quantity entered was not a valid integer.")
        continue
    try:
        stock_quantity = int(stock_quantity)
    except ValueError:
        print("The stock quantity entered was not a valid integer.")
        continue
    if stock_quantity < 0:
        print("The stock quantity cannot be a negative number.")
        failed += 1
        continue
    inventory += stock_quantity
    print("Updated inventory count:", inventory)