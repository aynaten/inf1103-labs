
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


# ============================================================
# PHASE 3 - COMPOSITION TEST
# ============================================================

def main():
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    laptop = PhysicalProduct(
        "P001", "Laptop", 1200.00, 10, 2.5, supplier
    )

    software = DigitalProduct(
        "D001", "Software", 49.99, 100, 500, supplier
    )

    print("=== Step 1: Create Order A ===")

    order_a = Order("O001")

    order_a.add_order_line(laptop, 2)
    order_a.add_order_line(software, 3)

    order_a.display_order()

    print("\n=== Step 2: Create Order B ===")

    order_b = Order("O002")

    order_b.add_order_line(laptop, 1)

    order_b.display_order()

    print("\n=== Step 3: Test Object Identity ===")

    line_a = order_a.get_order_lines()[0]
    line_b = order_b.get_order_lines()[0]

    print("Same OrderLine object:", line_a is line_b)
    print("Same Product object:", line_a.product is line_b.product)

    print("\n=== Step 4: Remove Order Line ===")

    order_a.remove_order_line("P001")

    print("\nOrder A after removal:")
    order_a.display_order()

    print("\nOrder B remains unchanged:")
    order_b.display_order()

    print("\n=== Step 5: Product Still Exists ===")
    laptop.display_information()

    print("\n=== Step 6: Validate Quantity ===")

    try:
        order_a.add_order_line(laptop, 0)
    except ValueError as error:
        print(f"Invalid quantity rejected: {error}")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
