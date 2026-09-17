def get_valid_input():
    stock_quantity = input("Enter stock quantity: ")
    if stock_quantity == "quit":
        return stock_quantity
    if not stock_quantity.isdigit():
        print("The stock quantity entered was not a valid integer.")
        return False
    try:
        stock_quantity = int(stock_quantity)
    except ValueError:
        print("The stock quantity entered was not a valid integer.")
        return False
    if stock_quantity <= 0:
        print("The stock quantity cannot be a negative number.")
        return False
    return stock_quantity

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return 0.1 * amount

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = 0
failed = 0

while True:
    stock_quantity = get_valid_input()
    if stock_quantity == "quit":
        break
    if not stock_quantity:
        failed += 1
        continue
    processed_result = process_delivery(inventory, stock_quantity)
    inventory = processed_result
    print("Updated inventory count:", inventory)
    tax_amount = calculate_tax(stock_quantity)
    print("Tax amount (10%):", tax_amount)
    if inventory > 500:
        print("Overstock alert: the inventory has exceeded 500 units (" + str(inventory) + ")")
        break
generate_report(inventory, failed)