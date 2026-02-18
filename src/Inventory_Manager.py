# Our current stock: {Item Name: [Quantity, Price]}
inventory = {
    "Laptop": [5, 1200],
    "Mouse": [15, 25],
    "Keyboard": [2, 45]
}


def process_order(item, quantity):
    if item not in inventory:
        return f"Error: {item} is not sold here."

    stock_qty = inventory[item][0]
    price = inventory[item][1]

    # Rule 1: Check if we have enough stock
    if quantity > stock_qty:
        return f"Order Denied: Only {stock_qty} {item}s left in stock."

    # Rule 2: Update stock and check for low-stock warning
    inventory[item][0] -= quantity
    remaining = inventory[item][0]

    total_cost = quantity * price
    message = f"Success: {quantity} {item}(s) sold for ${total_cost}."

    # Logic: Alert the manager if stock falls to 2 or less
    if remaining <= 2:
        message += f"\n ALERT: Low stock on {item}! Only {remaining} left."

    return message


# Test the system
print(process_order("Laptop", 1))  # Successful sale
print(process_order("Keyboard", 2))  # Successful sale + Low Stock Alert
print(process_order("Mouse", 50))  # Order Denied (Not enough stock)
