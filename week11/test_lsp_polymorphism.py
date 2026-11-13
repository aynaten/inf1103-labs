
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# ============================================================
# LSP TEST FUNCTION
# ============================================================

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# ============================================================
# PHASE 4 - LSP AND POLYMORPHISM TEST
# ============================================================

def main() -> None:
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    physical = PhysicalProduct(
        "P001", "Laptop", 1200.00, 10, 2.5, supplier
    )

    digital = DigitalProduct(
        "D001", "Software", 49.99, 100, 500, supplier
    )

    print("=== Step 1: LSP Test ===")

    print("\nPhysical Product:")
    show_product_details(physical)

    print("\nDigital Product:")
    show_product_details(digital)

    print("\n=== Step 2: Polymorphism Test ===")

    inventory = Inventory()

    inventory.add_product(physical)
    inventory.add_product(digital)

    for product in inventory.get_products():
        print(f"\nProduct ID: {product.get_product_id()}")
        print(product.get_fulfilment_info())

    print("\n=== Step 3: Inventory Display ===")

    inventory.display_all()

    print("\n=== Step 4: Stock Update LSP Test ===")

    physical.update_stock(20)
    digital.update_stock(200)

    print("\nPhysical after stock update:")
    physical.display_information()

    print("\nDigital after stock update:")
    digital.display_information()

    print("\n=== Step 5: Substitution Test ===")

    print("PhysicalProduct is Product:", isinstance(physical, Product))
    print("DigitalProduct is Product:", isinstance(digital, Product))


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
