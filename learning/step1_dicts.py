stack = [
    {"name": "Housing", "nominal": 50.00, "plus_tol": 0.10, "minus_tol": 0.10, "direction": 1},
    {"name": "Part A", "nominal": 12.00, "plus_tol": 0.05, "minus_tol": 0.05, "direction": -1},
    {"name": "Part B", "nominal": 15.50, "plus_tol": 0.05, "minus_tol": 0.05, "direction": -1},
    {"name": "Spacer", "nominal": 8.25, "plus_tol": 0.00, "minus_tol": 0.10, "direction": -1},
    {"name": "Part C", "nominal": 13.75, "plus_tol": 0.08, "minus_tol": 0.08, "direction": -1}
]

print("All values in mm")
print(f"{'Dimension':<10}{'Nominal':>10}{'Upper':>10}{'Lower':>10}")
for dim in stack:
    upper_limit = dim['nominal'] + dim['plus_tol']
    lower_limit = dim['nominal'] - dim['minus_tol']
    print(f"{dim['name']:<10}{dim['nominal']:>10.3f}{upper_limit:>10.3f}{lower_limit:>10.3f} mm")

nominal_gap = 0
for dim in stack:
    nominal_gap = nominal_gap + dim['direction'] * dim['nominal']

print(f"Nominal gap: {nominal_gap:.3f} mm")
