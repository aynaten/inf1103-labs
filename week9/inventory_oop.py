
import math

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from file_handler import save_inventory, load_inventory


# ============================================================
# MENU FUNCTION
# ============================================================

def display_menu():
    print("\n===== Inventory Management System =====")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    inventory = Inventory()

    # Load previously saved products
    load_inventory(inventory)

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        # OPTION 1: Display all products
        if choice == "1":
            inventory.display_all()

        # OPTION 2: Add a physical or digital product
        elif choice == "2":
            print("\nSelect Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Enter product type (1-2): ")

            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue

            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()

            if not product_id or not name:
                print("Product ID and name cannot be empty.")
                continue

            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            try:
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Stock Quantity: "))

                if not math.isfinite(price) or price < 0 or stock < 0:
                    print("Price and stock must be valid non-negative values.")
                    continue

                if product_type == "1":
                    weight = float(input("Enter Weight (kg): "))

                    if not math.isfinite(weight) or weight < 0:
                        print("Weight must be a valid non-negative number.")
                        continue

                    new_product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                else:
                    download_size = float(input("Enter Download Size (MB): "))

                    if not math.isfinite(download_size) or download_size < 0:
                        print("Download size must be a valid non-negative number.")
                        continue

                    new_product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

                inventory.add_product(new_product)

            except ValueError:
                print("Invalid input. Please enter valid numeric values.")

        # OPTION 3: Update stock
        elif choice == "3":
            product_id = input("Enter Product ID to update: ")
            product = inventory.search_product(product_id)

            if product is not None:
                try:
                    new_stock = int(input("Enter New Stock Quantity: "))
                    product.update_stock(new_stock)

                except ValueError:
                    print("Invalid input. Stock must be a whole number.")
            else:
                print("Product not found.")

        # OPTION 4: Search product
        elif choice == "4":
            product_id = input("Enter Product ID to search: ")
            product = inventory.search_product(product_id)

            if product is not None:
                print("\nProduct Found:")
                product.display_information()
                print(product.get_fulfilment_info())

                if isinstance(product, CanBeShipped):
                    print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
            else:
                print("Product not found.")

        # OPTION 5: Save inventory
        elif choice == "5":
            save_inventory(inventory)

        # OPTION 6: Exit
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
