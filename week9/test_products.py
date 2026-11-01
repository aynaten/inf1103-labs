
# ============================================================
# WEEK 9 - PHASE 1 TEST
# Test inheritance and method overriding
# ============================================================

from inventory_oop import PhysicalProduct, DigitalProduct

# Create a physical product
physical = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5)

# Create a digital product
digital = DigitalProduct("D001", "Software", 49.99, 100, 500)

# Display both products
print("=== Physical Product ===")
physical.display_information()

print("\n=== Digital Product ===")
digital.display_information()


# ============================================================
# PHASE 2 TEST - ABSTRACT CLASSES
# ============================================================

print("\n=== Fulfilment Information ===")
print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())

# Check that Product cannot be created directly
from inventory_oop import Product

try:
    generic = Product("P999", "Generic", 10.0, 5)
except TypeError as error:
    print("\nAbstract class test passed.")
    print(error)
