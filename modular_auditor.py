inventory = 0
failed = 0

def get_valid_input():
    stock_quantity = input("Enter stock quantity: ")
    if stock_quantity == "quit":
        return False
    if not stock_quantity.isdigit():
        print("The stock quantity entered was not a valid integer.")
        failed += 1
        return get_valid_input()
    try:
        stock_quantity = int(stock_quantity)
    except ValueError:
        print("The stock quantity entered was not a valid integer.")
        failed += 1
        return get_valid_input()
    if stock_quantity < 0:
        print("The stock quantity cannot be a negative number.")
        failed += 1
        return get_valid_input()
    return stock_quantity

while True:
    stock_quantity = get_valid_input()
    if not stock_quantity:
        break
    inventory += stock_quantity
    print("Updated inventory count:", inventory)
    if inventory > 500:
        print("Overstock alert: the inventory has exceeded 500 units (" + str(inventory) + ")")
        break
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed)