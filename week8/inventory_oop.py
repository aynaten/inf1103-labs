
from product import Product
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
    # Create an empty Inventory object
    inventory = Inventory()

    # Load previously saved products when the program starts
    load_inventory(inventory)

    # Keep displaying the menu until the user exits
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        # OPTION 1: Display all products
        if choice == "1":
            inventory.display_all()

        # OPTION 2: Add a new product
        elif choice == "2":
            # Collect product details from the user
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")

            try:
                # Convert input into appropriate data types
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Stock Quantity: "))

                # Check that the values are valid
                if price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")

                # Prevent duplicate product IDs
                elif inventory.search_product(product_id) is not None:
                    print("Product ID already exists.")

                else:
                    # Create a new Product object
                    new_product = Product(product_id, name, price, stock)

                    # Add the Product object to Inventory
                    inventory.add_product(new_product)

            except ValueError:
                print("Invalid input. Price must be a number and stock must be a whole number.")

        # OPTION 3: Update stock quantity
        elif choice == "3":
            product_id = input("Enter Product ID to update: ")

            # Search for the existing product
            product = inventory.search_product(product_id)

            if product is not None:
                try:
                    new_stock = int(input("Enter New Stock Quantity: "))
                    product.update_stock(new_stock)

                except ValueError:
                    print("Invalid input. Stock must be a whole number.")
            else:
                print("Product not found.")

        # OPTION 4: Search for a product
        elif choice == "4":
            # Ask the user which product to search for
            product_id = input("Enter Product ID to search: ")

            # Search the inventory for the product
            product = inventory.search_product(product_id)

            # Display the product if found
            if product is not None:
                print("\nProduct Found:")
                product.display_information()
            else:
                print("Product not found.")

        # OPTION 5: Save inventory to JSON
        elif choice == "5":
            save_inventory(inventory)

        # OPTION 6: Exit program
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break

        # Handle invalid menu selections
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
