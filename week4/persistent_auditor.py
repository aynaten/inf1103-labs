import os

INVENTORY_FILE = "inventory.txt"

def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        print("No saved inventory found. Starting fresh.")
        return 0, []

    with open(INVENTORY_FILE, "r") as f:
        lines = f.read().splitlines()

    total = int(lines[0])
    history = []
    if len(lines) > 1 and lines[1].strip():
        history = [int(x) for x in lines[1].split(",")]

    print(f"Loaded saved inventory: total = {total}")
    return total, history

def save_inventory(total, history):
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"{total}\n")
        f.write(",".join(str(x) for x in history) + "\n")
    print(f"Inventory saved to {INVENTORY_FILE}")

def get_valid_input():
    entry = input("Enter stock quantity (or 'quit' to stop): ").strip()

    if entry.lower() == "quit":
        return "quit"

    if not entry.isdigit():
        print("Error: Please enter a valid whole number.")
        return None

    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative numbers are not allowed.")
        return None

    return quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(deliveries_processed, failed_attempts, history):
    print("\n--- Report ---")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print(f"Transaction History: {history}")
    

def main():
    total_inventory, history = load_inventory()
    deliveries_processed = 0
    failed_entries = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        total_inventory = process_delivery(total_inventory, quantity)
        history.append(quantity)
        tax = calculate_tax(quantity)
        deliveries_processed += 1

        print(f"Added {quantity} units. Tax on this delivery: {tax:.2f}. Current total: {total_inventory}")

    generate_report(deliveries_processed, failed_entries, history)
    save_inventory(total_inventory, history)


if __name__ == "__main__":
    main()