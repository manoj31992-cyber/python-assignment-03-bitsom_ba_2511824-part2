
# ─────────────────────────────────────────────
#  PROVIDED DATA 
# ─────────────────────────────────────────────

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# ═══════════════════════════════════════════════════════════════
#  TASK 1 — Explore the Menu
# ═══════════════════════════════════════════════════════════════

print("\n" + "═" * 50)
print("  TASK 1 — Explore the Menu")
print("═" * 50)

# --- 1a. Print menu grouped by category ---

# Collect unique categories while preserving order of appearance
categories = []
for item_details in menu.values():
    cat = item_details["category"]
    if cat not in categories:
        categories.append(cat)

for category in categories:
    print(f"\n{'=' * 5} {category} {'=' * 5}")
    for item_name, item_details in menu.items():
        if item_details["category"] == category:
            status = "[Available]" if item_details["available"] else "[Unavailable]"
            # Left-align name in 16 chars, price right-aligned
            print(f"  {item_name:<16} ₹{item_details['price']:.2f}   {status}")

# --- 1b. Menu statistics ---

total_items     = len(menu)
available_items = sum(1 for d in menu.values() if d["available"])

# Most expensive item
most_expensive_name  = max(menu, key=lambda name: menu[name]["price"])
most_expensive_price = menu[most_expensive_name]["price"]

# Items priced under ₹150
cheap_items = {name: d for name, d in menu.items() if d["price"] < 150}

print(f"\n--- Menu Statistics ---")
print(f"Total items on menu   : {total_items}")
print(f"Available items       : {available_items}")
print(f"Most expensive item   : {most_expensive_name} (₹{most_expensive_price:.2f})")
print(f"Items priced under ₹150:")
for name, d in cheap_items.items():
    print(f"  {name:<16} ₹{d['price']:.2f}")


# I need to group items by category, so first I collect unique categories
# by looping through the menu values. I use a list instead of a set
# so the order stays the same as in the original menu.

# For each category, I loop through the whole menu again and only print
# items that belong to that category — basically filtering on the fly.

# available items — I use sum() with a condition inside.
# For each item, if available is True it counts as 1, else 0.
# max() with a lambda lets me find the item with the highest price.


# ═══════════════════════════════════════════════════════════════
#  TASK 2 — Cart Operations
# ═══════════════════════════════════════════════════════════════

print("\n" + "═" * 50)
print("  TASK 2 — Cart Operations")
print("═" * 50)

cart = []   # list of {"item": str, "quantity": int, "price": float}


def add_to_cart(cart, item_name, quantity=1):
    """Add item to cart. Merges quantity if item already exists."""
    if item_name not in menu:
        print(f"  ✗ '{item_name}' does not exist in the menu.")
        return
    if not menu[item_name]["available"]:
        print(f"  ✗ '{item_name}' is currently unavailable.")
        return

    # Check if item is already in cart
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += quantity
            print(f"  ✓ Updated '{item_name}' quantity to {entry['quantity']}.")
            return

    # New entry
    cart.append({
        "item":     item_name,
        "quantity": quantity,
        "price":    menu[item_name]["price"]
    })
    print(f"  ✓ Added '{item_name}' × {quantity} to cart.")


def remove_from_cart(cart, item_name):
    """Remove an item from the cart by name."""
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f"  ✓ Removed '{item_name}' from cart.")
            return
    print(f"  ✗ '{item_name}' is not in the cart.")


def update_quantity(cart, item_name, new_quantity):
    """Update the quantity of an existing cart item."""
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_quantity
            print(f"  ✓ '{item_name}' quantity updated to {new_quantity}.")
            return
    print(f"  ✗ '{item_name}' is not in the cart.")


def print_cart(cart):
    """Display current cart contents."""
    if not cart:
        print("  Cart is empty.")
        return
    print("  Current cart:")
    for entry in cart:
        line_total = entry["quantity"] * entry["price"]
        print(f"    {entry['item']:<18} x{entry['quantity']}  ₹{line_total:.2f}")


# --- Simulate the order sequence ---

print("\n>> Step 1: Add 'Paneer Tikka' × 2")
add_to_cart(cart, "Paneer Tikka", 2)
print_cart(cart)

print("\n>> Step 2: Add 'Gulab Jamun' × 1")
add_to_cart(cart, "Gulab Jamun", 1)
print_cart(cart)

print("\n>> Step 3: Add 'Paneer Tikka' × 1  (should merge → quantity 3)")
add_to_cart(cart, "Paneer Tikka", 1)
print_cart(cart)

print("\n>> Step 4: Try to add 'Mystery Burger' (does not exist)")
add_to_cart(cart, "Mystery Burger", 1)
print_cart(cart)

print("\n>> Step 5: Try to add 'Chicken Wings' (unavailable)")
add_to_cart(cart, "Chicken Wings", 1)
print_cart(cart)

print("\n>> Step 6: Remove 'Gulab Jamun'")
remove_from_cart(cart, "Gulab Jamun")
print_cart(cart)

# --- Final Order Summary ---

subtotal = sum(e["quantity"] * e["price"] for e in cart)
gst      = subtotal * 0.05
total    = subtotal + gst

print("\n" + "=" * 38)
print("         Order Summary")
print("=" * 38)
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    print(f"  {entry['item']:<18} x{entry['quantity']}  ₹{line_total:.2f}")
print("-" * 38)
print(f"  {'Subtotal:':<25} ₹{subtotal:.2f}")
print(f"  {'GST (5%):':<25} ₹{gst:.2f}")
print(f"  {'Total Payable:':<25} ₹{total:.2f}")
print("=" * 38)

# Before adding, I check two things: does the item exist in menu?
# And is it marked available? If either fails, I skip and warn the user.

# The tricky part: if the item is already in the cart, I shouldn't
# add a new entry — I just increase the quantity of the existing one.
# So I loop through the cart first to check.

# For removal, I loop through cart and match by item name.
# list.remove() deletes the first matching element.

# ═══════════════════════════════════════════════════════════════
#  TASK 3 — Inventory Tracker with Deep Copy
# ═══════════════════════════════════════════════════════════════

print("\n" + "═" * 50)
print("  TASK 3 — Inventory Tracker with Deep Copy")
print("═" * 50)

# --- 3a. Deep copy inventory before any changes ---
inventory_backup = copy.deepcopy(inventory)

# Demonstrate deep copy works: temporarily change a value
print("\n>> Demonstrating deep copy — changing inventory['Paneer Tikka']['stock'] to 999")
inventory["Paneer Tikka"]["stock"] = 999
print(f"   inventory['Paneer Tikka']['stock']        = {inventory['Paneer Tikka']['stock']}")
print(f"   inventory_backup['Paneer Tikka']['stock'] = {inventory_backup['Paneer Tikka']['stock']}")
print("   ✓ Backup is unaffected — deep copy confirmed.")

# Restore original value
inventory["Paneer Tikka"]["stock"] = 10
print(">> inventory restored to original stock (10).")

# --- 3b. Deduct cart quantities from inventory ---

print("\n>> Deducting cart items from inventory...")
for entry in cart:
    item_name = entry["item"]
    qty_needed = entry["quantity"]
    available_stock = inventory[item_name]["stock"]

    if qty_needed > available_stock:
        print(f"  ⚠ Insufficient stock for '{item_name}': "
              f"needed {qty_needed}, available {available_stock}. Deducting {available_stock}.")
        inventory[item_name]["stock"] = 0
    else:
        inventory[item_name]["stock"] -= qty_needed
        print(f"  ✓ Deducted {qty_needed} of '{item_name}'. "
              f"Remaining stock: {inventory[item_name]['stock']}")

# --- 3c. Reorder alerts ---

print("\n--- Reorder Alerts ---")
alert_found = False
for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"  ⚠ Reorder Alert: {item_name} — "
              f"Only {details['stock']} unit(s) left "
              f"(reorder level: {details['reorder_level']})")
        alert_found = True
if not alert_found:
    print("  All items are sufficiently stocked.")

# --- 3d. Compare inventory vs backup ---

print("\n--- inventory vs inventory_backup (stocks) ---")
print(f"  {'Item':<18} {'Current Stock':>15} {'Backup Stock':>13}")
print("  " + "-" * 48)
for item_name in inventory:
    curr  = inventory[item_name]["stock"]
    bkup  = inventory_backup[item_name]["stock"]
    diff  = " ← changed" if curr != bkup else ""
    print(f"  {item_name:<18} {curr:>15} {bkup:>13}{diff}")

# If I just write inventory_backup = inventory, both variables point
# to the SAME dictionary in memory. Changing one changes the other.
# deepcopy() creates a completely independent copy — changes to
# inventory won't touch inventory_backup at all.

# I temporarily set a stock value to 999 just to PROVE the backup
# didn't change. Then I restore it before doing real deductions.


# ═══════════════════════════════════════════════════════════════
#  TASK 4 — Daily Sales Log Analysis
# ═══════════════════════════════════════════════════════════════

print("\n" + "═" * 50)
print("  TASK 4 — Daily Sales Log Analysis")
print("═" * 50)


def print_revenue_per_day(log):
    """Print total revenue for each day and identify the best-selling day."""
    print("\n--- Revenue Per Day ---")
    best_day     = None
    best_revenue = 0.0
    for date, orders in log.items():
        day_revenue = sum(order["total"] for order in orders)
        print(f"  {date}  ₹{day_revenue:.2f}")
        if day_revenue > best_revenue:
            best_revenue = day_revenue
            best_day     = date
    print(f"\n  🏆 Best-selling day: {best_day}  (₹{best_revenue:.2f})")


# --- 4a & 4b. Revenue per day + best day (original data) ---
print_revenue_per_day(sales_log)

# --- 4c. Most ordered item ---

item_counter = Counter()
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_counter[item] += 1

most_ordered_item, most_ordered_count = item_counter.most_common(1)[0]
print(f"\n  🥇 Most ordered item: {most_ordered_item} "
      f"(appears in {most_ordered_count} orders)")

# --- 4d. Add new day and reprint stats ---

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\n>> Added 2025-01-05. Updated stats:")
print_revenue_per_day(sales_log)

# --- 4e. Numbered list of all orders using enumerate ---

print("\n--- All Orders (numbered) ---")
order_number = 1
for date, orders in sales_log.items():
    for order in orders:
        items_str = ", ".join(order["items"])
        print(f"  {order_number}. [{date}] Order #{order['order_id']:<3}"
              f" — ₹{order['total']:.2f}"
              f" — Items: {items_str}")
        order_number += 1

print("\n" + "═" * 50)
print("  All tasks completed successfully!")
print("═" * 50)


# To get daily revenue, I loop through each date and sum up
# the "total" field from every order on that day.

# For most ordered item, I need to count how many ORDERS each
# item appears in (not total quantity). So I loop through every
# order's items list and keep a running count in a dictionary.

# enumerate() gives me both an index and the value at the same time,
# which is perfect for printing a numbered list without a manual counter.
