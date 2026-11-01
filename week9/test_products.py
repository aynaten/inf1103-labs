
# ============================================================
# WEEK 9 - PRODUCT CLASS TESTS
# ============================================================

from inventory_oop import (
    Product,
    PhysicalProduct,
    DigitalProduct,
    CanBeShipped
)


# ============================================================
# PHASE 1 - INHERITANCE AND METHOD OVERRIDING
# ============================================================

physical = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5)
digital = DigitalProduct("D001", "Software", 49.99, 100, 500)

print("=== Physical Product ===")
physical.display_information()

print("\n=== Digital Product ===")
digital.display_information()


# ============================================================
# PHASE 2 - ABSTRACT CLASSES
# ============================================================

print("\n=== Fulfilment Information ===")
print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())

# Verify that the abstract Product class cannot be instantiated
try:
    generic = Product("P999", "Generic", 10.0, 5)

except TypeError as error:
    print("\nAbstract class test passed.")
    print(error)


# ============================================================
# PHASE 3 - SHIPPING INTERFACE
# ============================================================

# Create two physical products with different weights
light_product = PhysicalProduct("P010", "Mouse", 25.50, 20, 0.2)
heavy_product = PhysicalProduct("P011", "Monitor", 299.99, 10, 5.0)

print("\n=== Shipping Cost Test ===")

print(f"Mouse shipping cost: ${light_product.calculate_shipping_cost():.2f}")
print(f"Monitor shipping cost: ${heavy_product.calculate_shipping_cost():.2f}")

# Check which products support the shipping interface
print("\n=== Interface Test ===")

print(f"PhysicalProduct supports CanBeShipped: {isinstance(light_product, CanBeShipped)}")
print(f"DigitalProduct supports CanBeShipped: {isinstance(digital, CanBeShipped)}")
