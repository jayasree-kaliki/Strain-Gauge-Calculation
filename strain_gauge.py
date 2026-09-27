# strain_gauge.py
# Program to calculate strain and change in resistance
# using a strain gauge

print("=== Strain Gauge Measurement ===")

# Input values
initial_resistance = float(input("Enter initial resistance of strain gauge (Ohm): "))
gauge_factor = float(input("Enter gauge factor: "))
change_resistance = float(input("Enter change in resistance (Ohm): "))

# Calculate strain
strain = change_resistance / (gauge_factor * initial_resistance)

# Calculate strain in microstrain
microstrain = strain * 1e6

# Display results
print("\n--- Strain Gauge Results ---")
print(f"Initial Resistance = {initial_resistance:.3f} Ohm")
print(f"Gauge Factor       = {gauge_factor:.3f}")
print(f"Change in Resistance = {change_resistance:.6f} Ohm")
print(f"Strain             = {strain:.6e}")
print(f"Strain             = {microstrain:.2f} microstrain")
