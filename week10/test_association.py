
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# ============================================================
# PHASE 1 - ASSOCIATION TEST
# ============================================================

def main():
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

    print("=== Physical Product ===")
    physical.display_information()
    physical.display_supplier_information()

    print("\n=== Digital Product ===")
    digital.display_information()
    digital.display_supplier_information()

    print("\n=== Association Test ===")

    print("Both products reference the same supplier:")
    print(physical.get_supplier() is digital.get_supplier())

    print("\nDeleting the supplier variable...")
    del supplier

    print("\nSupplier information after deletion:")
    physical.display_supplier_information()
    digital.display_supplier_information()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
