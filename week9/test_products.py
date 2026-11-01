
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
