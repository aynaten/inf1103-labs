
from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


# ============================================================
# PHASE 2 - AGGREGATION TEST
# ============================================================

def main():
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    product = PhysicalProduct(
        "P001",
        "Laptop",
        1200.00,
        10,
        2.5,
        supplier
    )

    print("=== Step 1: Product Exists Independently ===")
    product.display_information()

    inventory_a = Inventory()
    inventory_b = Inventory()

    print("\n=== Step 2: Add Product to Inventory A ===")
    inventory_a.add_product(product)

    print("\n=== Step 3: Find Product in Inventory A ===")
    found_product = inventory_a.find_product("P001")
    print("Found same Product object:", found_product is product)

    print("\n=== Step 4: Remove Product from Inventory A ===")
    removed_product = inventory_a.remove_product("P001")

    print("Inventory A has product:",
          inventory_a.find_product("P001") is not None)

    print("Removed object is original:",
          removed_product is product)

    print("\n=== Step 5: Product Still Works ===")
    product.display_information()

    print("\n=== Step 6: Transfer to Inventory B ===")
    inventory_b.add_product(product)

    print("Inventory B has original object:",
          inventory_b.find_product("P001") is product)

    print("\n=== Step 7: Display Inventory B ===")
    inventory_b.display_all()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()



