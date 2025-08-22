from datetime import datetime
 # --- Inventory Data ---
inventory = {
     "Chips": {"quantity": 200, "price": 9.99, "category": "Snacks"},
     "Chocolates": {"quantity": 500, "price": 5, "category": "Snacks"},
     "Special Chocolates": {"quantity": 200, "price": 25, "category": "Snacks"},
     "Maggi": {"quantity": 150, "price": 11.99, "category": "Food"},
     "Perfumes": {"quantity": 50, "price": 114, "category": "Cosmetics"},
     "Shoes": {"quantity": 600, "price": 799, "category": "Footwear"},
     "Icecreams": {"quantity": 350, "price": 20, "category": "Snacks"},
     "Pens": {"quantity": 200, "price": 5, "category": "Stationery"},
     "Pencils": {"quantity": 100, "price": 3, "category": "Stationery"},
     "Protractors": {"quantity": 100, "price": 10, "category": "Stationery"},
     "Cool Drinks": {"quantity": 300, "price": 9, "category": "Beverages"}
 } 
 # --- Store Info ---
store_name = "Student Mart"
door_no = "22c/1/59"
city = "POWERPET Eluru-534001"
state = "ANDHRA PRADESH" 
# --- Customer Info ---
print(f"\n{store_name}\n{door_no}\n{city}\n{state}")
customer_name = input("\nEnter Customer Name: ")
phone_number = input("Enter Phone Number: ") 
# --- Date and Time ---
now = datetime.now()
date_time = now.strftime("%d-%m-%Y %I:%M %p") 
# --- Show Inventory Before Shopping ---
print("\n📦 Available Inventory:\n")
print("--------------------------------------------------------")
print("| {:<18} | {:<12} | {:<7} | {:<7} |".format("Product", "Category", "Price", "Stock"))
print("--------------------------------------------------------")
for item, details in inventory.items():
    print(item)
print("| {:<18} | {:<12} | ₹{:<6.2f} | {:<7} |".format(
           item, details["category"], details["price"], details["quantity"]))
print("--------------------------------------------------------")
# --- Shopping Cart ---
cart = {}
shoe_discount = 0
subtotal = 0
while True:
    item = input("\nEnter item name (or type 'done' to finish): ").strip()
    if item.lower() == "done":
        break
    if item.lower() == "shoes":
        item_key = "Shoes"
        size = input("Enter Shoe Size (e.g., 6, 7, 8, 9, 10): ").strip()
        item_display_name = f"Shoes (Size {size})"
    else:
        if item not in inventory:
            print("❌ Item not found in inventory.")
            continue
        item_key = item
        item_display_name = item
    max_available = inventory[item_key]["quantity"]
    if max_available == 0:
        print("❌ This item is out of stock.")
        continue
    while True:
        try:
            quantity = int(input(f"Enter quantity for {item_display_name} (Available: {max_available}): "))
            if quantity <= 0:
                print("❌ Quantity must be greater than zero.")
                continue
            if quantity > max_available:
                print(f"❌ Only {max_available} in stock. Try a lower quantity.")
            else:
                break
        except ValueError:
            print("❌ Please enter a valid number.")

    price = inventory[item_key]["price"] * quantity
    # Apply 15% discount for shoes
    if item_key == "Shoes":
        discount = price * 0.15
        shoe_discount += discount
        price -= discount

    cart[item_display_name] = {
        "quantity": quantity,
        "price": price,
        "unit_price": inventory[item_key]["price"],
        "category": inventory[item_key]["category"]
    }
    subtotal += price
    inventory[item_key]["quantity"] -= quantity
# ✅ Show Remaining Inventory BEFORE Billing
print("\n📦 Remaining Inventory BEFORE Billing:\n")
print("--------------------------------------------------------")
print("| {:<18} | {:<12} | {:<7} | {:<7} |".format("Product", "Category", "Price", "Stock"))
print("--------------------------------------------------------")
for item, details in inventory.items():
    print("| {:<18} | {:<12} | ₹{:<6.2f} | {:<7} |".format(
        item, details["category"], details["price"], details["quantity"]))
print("--------------------------------------------------------")
# --- General Discount if applicable ---
general_discount = 0
if subtotal >= 299:
    general_discount = subtotal * 0.10
subtotal_after_discounts = subtotal - general_discount
# --- GST Calculation ---
gst = subtotal_after_discounts * 0.18
grand_total = subtotal_after_discounts + gst
# --- Print Bill ---
print("\n" + "=" * 55)
print(f"{store_name.center(55)}")
print(f"{('Door No: ' + door_no + ', ' + city + ', ' + state).center(55)}")
print(f"Date & Time: {date_time}")
print(f"Customer Name: {customer_name}")
print(f"Phone Number: {phone_number}")
print("-" * 55)
print("{:<20}{:<12}{:<8}{:<10}".format("Item", "Category", "Qty", "Price"))
print("-" * 55)
for item, data in cart.items():
    print("{:<20}{:<12}{:<8}{:<10.2f}".format(
        item, data["category"], data["quantity"], data["price"]))

print("-" * 55)
print(f"{'Subtotal:':<40} Rs {subtotal:.2f}")

# --- Discounts Section ---
print("\n------ Discounts ------")
print(f"{'Shoe Discount (15%):':<40} -Rs {shoe_discount:.2f}")
print(f"{'General Discount (10% if bill ≥ 299):':<40} -Rs {general_discount:.2f}")

# --- GST & Final Total ---
print("\n------ Taxes & Total ------")
print(f"{'GST (18%):':<40} Rs {gst:.2f}")
print(f"{'Grand Total:':<40} Rs {grand_total:.2f}")
print("=" * 55)
print("       ✅ Thank You! Visit Again :)")
print("=" * 55)
