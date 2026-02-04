# ---------- LOAD ITEMS ----------
def load_items():
    items = {}
    file = open("items.txt", "r")
    for line in file:
        name, price = line.strip().split(",")
        items[name] = int(price)
    file.close()
    return items


# ---------- SAVE BILL ----------
def save_bill(bill):
    file = open("bills.txt", "a")
    file.write(bill + "\n")
    file.close()


# ---------- SHOW ITEMS ----------
def show_items(items):
    print("\n--- AVAILABLE ITEMS ---")
    for item, price in items.items():
        print(item, ":", price)


# ---------- ADD ITEM ----------
def add_item(cart, items):
    name = input("Enter item name: ")
    if name in items:
        qty = int(input("Enter quantity: "))
        cart[name] = qty
        print("Item Added Successfully!")
    else:
        print("Item Not Found!")


# ---------- REMOVE ITEM ----------
def remove_item(cart):
    name = input("Enter item to remove: ")
    if name in cart:
        del cart[name]
        print("Item Removed!")
    else:
        print("Item not in cart!")


# ---------- PAYMENT SYSTEM ----------
def payment(amount):
    print("\nTotal Amount: Rs.", amount)
    print("1. Cash")
    print("2. UPI")

    choice = input("Choose payment method: ")

    if choice == "1":
        print("Cash Payment Successful!")
        return "Cash"

    elif choice == "2":
        upi = input("Enter UPI ID: ")
        print("Processing...")
        print("UPI Payment Successful!")
        return "UPI"

    else:
        print("Invalid Payment Option!")
        return None


# ---------- GENERATE BILL ----------
def generate_bill(cart, items):
    if len(cart) == 0:
        print("Cart is empty!")
        return

    total = 0
    bill = "\n------ GROCERY RECEIPT ------\n"

    for item, qty in cart.items():
        price = items[item] * qty
        total += price
        bill += f"{item} x {qty} = {price}\n"

    bill += "-----------------------------\n"
    bill += f"TOTAL = {total}\n"

    method = payment(total)

    if method:
        bill += f"Payment Method: {method}\n"
        bill += "Payment Status: SUCCESS\n"
        bill += "-----------------------------\n"
        print(bill)
        save_bill(bill)
        cart.clear()
    else:
        print("Payment Failed!")


# ---------- MAIN PROGRAM ----------
items = load_items()
cart = {}

while True:
    print("\n===== GROCERY STORE SYSTEM =====")
    print("1. Show Items")
    print("2. Add Item to Cart")
    print("3. Remove Item")
    print("4. Generate Bill & Pay")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_items(items)

    elif choice == "2":
        add_item(cart, items)

    elif choice == "3":
        remove_item(cart)

    elif choice == "4":
        generate_bill(cart, items)

    elif choice == "5":
        print("Thank You for Shopping!")
        break

    else:
        print("Invalid Choice!")