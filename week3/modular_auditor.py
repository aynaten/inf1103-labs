# auditor.py

total_inventory = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or 'quit' to stop): ").strip()

    if entry.lower() == "quit":
        break

    if not entry.isdigit():
        print("Error: Please enter a valid whole number.")
        failed_entries += 1
        continue

    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative numbers are not allowed.")
        failed_entries += 1
        continue

    total_inventory += quantity
    print(f"Added {quantity} units. Current total: {total_inventory}")

    if total_inventory > 500:
        print("ALERT: Overstock! Total inventory exceeds 500 units.")
        break

print("\n--- Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")