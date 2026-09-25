def load_inventory():
    inv = []
    try:
        with open('inventory.txt', 'r') as file:
            for item in file:
                inv.append(int(item.strip()))
        return inv
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        for item in inventory:
            file.write(str(item) + '\n')

# get_valid_input(): takes no input, returns "quit", False, or a valid integer
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

# process_delivery(current_total, new_value): takes the current running total, the new value to be added, and returns the sum
def process_delivery(inventory, new_value):
    inventory.append(new_value)
    return sum(inventory)

# calculate_tax(amount): takes the amount, returns the tax for the amount (10%)
def calculate_tax(amount):
    return 0.1 * amount

# generate_report(total_units, failed_attempts): takes the current running total, number of failed attempts, and prints the final totals
def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = load_inventory()
failed = 0

while True:
    stock_quantity = get_valid_input()
    if stock_quantity == "quit":
        save_inventory(inventory)
        break
    if not stock_quantity:
        failed += 1
        continue
    processed_result = process_delivery(inventory, stock_quantity)
    print("Updated inventory count:", processed_result)
    tax_amount = calculate_tax(stock_quantity)
    print("Tax amount (10%):", tax_amount)
    # if inventory > 500:
    #     print("Overstock alert: the inventory has exceeded 500 units (" + str(inventory) + ")")
    #     break
generate_report(sum(inventory), failed)