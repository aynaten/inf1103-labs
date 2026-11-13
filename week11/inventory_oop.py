
import math

from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory
from order import Order
from file_handler import save_inventory, load_inventory


# ============================================================
# INPUT VALIDATION
# ============================================================

def get_non_negative_float(message: str) -> float:
    while True:
        try:
            value = float(input(message))

            if not math.isfinite(value) or value < 0:
                print("Please enter a valid non-negative number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_negative_integer(message: str) -> int:
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_positive_integer(message: str) -> int:
    while True:
        value = get_non_negative_integer(message)

        if value > 0:
            return value

        print("Quantity must be greater than zero.")


# ============================================================
# SUPPLIER MANAGEMENT
# ============================================================

def choose_supplier(
    suppliers: dict[str, Supplier]
) -> Supplier:
    if suppliers:
        print("\nExisting Suppliers:")

        for supplier in suppliers.values():
            supplier.display_information()
            print("-" * 40)

    while True:
        supplier_id = input("Enter Supplier ID: ").strip()

        if not supplier_id:
            print("Supplier ID cannot be empty.")
            continue

        if supplier_id in suppliers:
            print("Using existing supplier.")
            return suppliers[supplier_id]

        print("Creating new supplier.")

        name = input("Supplier Name: ").strip()
        email = input("Contact Email: ").strip()

        if not name or not email:
            print("Supplier name and email cannot be empty.")
            continue

        supplier = Supplier(supplier_id, name, email)
        suppliers[supplier_id] = supplier

        print("Supplier created successfully.")
        return supplier


# ============================================================
# PRODUCT MANAGEMENT
# ============================================================

def add_product(
    inventory: Inventory,
    suppliers: dict[str, Supplier]
) -> None:
    print("\n1. Physical Product")
    print("2. Digital Product")

    product_choice = input("Select Product Type: ").strip()

    if product_choice == "1":
        product_type = "physical"

    elif product_choice == "2":
        product_type = "digital"

    else:
        print("Invalid product type.")
        return

    product_id = input("Product ID: ").strip()

    if not product_id:
        print("Product ID cannot be empty.")
        return

    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Product Name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    price = get_non_negative_float("Price: $")
    stock = get_non_negative_integer("Stock Quantity: ")
    supplier = choose_supplier(suppliers)

    if product_type == "physical":
        weight = get_non_negative_float("Weight (kg): ")

        product = ProductFactory.create(
            product_type,
            product_id,
            name,
            price,
            stock,
            supplier,
            weight=weight
        )

    else:
        download_size = get_non_negative_float(
            "Download Size (MB): "
        )

        product = ProductFactory.create(
            product_type,
            product_id,
            name,
            price,
            stock,
            supplier,
            download_size=download_size
        )

    inventory.add_product(product)


def update_product_stock(inventory: Inventory) -> None:
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    quantity = get_non_negative_integer("New Stock Quantity: ")
    product.update_stock(quantity)


def search_product(inventory: Inventory) -> None:
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    product.display_information()
    print(product.get_fulfilment_info())

    print("\nSupplier Information:")
    product.display_supplier_information()


def display_suppliers(
    suppliers: dict[str, Supplier]
) -> None:
    if not suppliers:
        print("No suppliers found.")
        return

    for supplier in suppliers.values():
        supplier.display_information()
        print("-" * 40)


# ============================================================
# ORDER MANAGEMENT
# ============================================================

def create_order(
    inventory: Inventory,
    orders: list[Order]
) -> None:
    if not inventory.get_products():
        print("Cannot create an order without products.")
        return

    order_id = input("Order ID: ").strip()

    if not order_id:
        print("Order ID cannot be empty.")
        return

    for existing_order in orders:
        if existing_order.order_id == order_id:
            print("Order ID already exists.")
            return

    order = Order(order_id)

    while True:
        print("\nAvailable Products:")
        inventory.display_all()

        product_id = input(
            "Enter Product ID (or 'done' to finish): "
        ).strip()

        if product_id.lower() == "done":
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        quantity = get_positive_integer("Quantity: ")
        order.add_order_line(product, quantity)

    if not order.get_order_lines():
        print("Order cancelled because no items were added.")
        return

    orders.append(order)

    print("\nOrder created successfully.")
    order.display_order()


def display_orders(orders: list[Order]) -> None:
    if not orders:
        print("No orders found.")
        return

    for order in orders:
        order.display_order()
        print("-" * 40)


# ============================================================
# MAIN MENU
# ============================================================

def display_menu() -> None:
    print("\n========== INVENTORY MANAGEMENT ==========")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory and Orders")
    print("6. Display Suppliers")
    print("7. Create Order")
    print("8. Display Orders")
    print("9. Exit")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main() -> None:
    inventory = Inventory()
    orders: list[Order] = []
    suppliers: dict[str, Supplier] = {}

    load_inventory(inventory, orders, suppliers)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product(inventory, suppliers)

        elif choice == "3":
            update_product_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(inventory, orders)

        elif choice == "6":
            display_suppliers(suppliers)

        elif choice == "7":
            create_order(inventory, orders)

        elif choice == "8":
            display_orders(orders)

        elif choice == "9":
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
