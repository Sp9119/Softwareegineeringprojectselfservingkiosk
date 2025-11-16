items = []  # list to store (item, price)
total = 0.0
tax_rate = 0.0825

print("Welcome to the Cafe!")
print("Enter your food or drink items. Type done when finished.\n")

# Loop to collect items
while True:
    receipt_item = input("Enter food or drink item name or done to finish: ")
    if receipt_item.lower() == "done":
        break
    try:
        price = float(input(f"Enter price for {receipt_item}: $"))
        items.append((receipt_item, price))
        total += price
    except ValueError:
        print("Invalid price. Please enter a number.")

# Ask user for tip percentage
try:
    tip_percentage = float(input("\nEnter tip percentage (e.g., 15 for 15%): "))
except ValueError:
    tip_percentage = 0.0

# Calculate amounts
tax = total * tax_rate
tip = total * (tip_percentage / 100)
total = total + tax + tip

# Ask if the user wants a receipt
receipt_choice = input("\nWould you like a receipt? (yes/no): ")

if receipt_choice.lower() == "yes":
    print("\n----- RECEIPT -----")
    for i, (item, price) in enumerate(items, start=1):
        print(f"{i}. {item:<15} ${price:.2f}")
    print("-------------------")
    print(f"TOTAL:           ${total:.2f}")
    print("-------------------")
    print("Thank you for shopping with us!")
else:
    print("Thank you for shopping with us!")
