def calc_upper_limit(dim):
    """Return upper limit of one dimension dictionary"""
    return dim['nominal'] + dim['plus_tol']


def calc_lower_limit(dim):
    """Return lower limit of one dimension dictionary"""
    return dim['nominal'] - (dim['minus_tol'])


def calc_nominal_gap(stack):
    """Return the nominal gap of a stack"""
    nominal_gap = 0
    for dim in stack:
        nominal_gap = nominal_gap + dim['direction'] * dim['nominal']
    return nominal_gap


housing_stack = [
    {"name": "Housing", "nominal": 50.00, "plus_tol": 0.10, "minus_tol": 0.10, "direction": 1},
    {"name": "Part A", "nominal": 12.00, "plus_tol": 0.05, "minus_tol": 0.05, "direction": -1},
    {"name": "Part B", "nominal": 15.50, "plus_tol": 0.05, "minus_tol": 0.05, "direction": -1},
    {"name": "Spacer", "nominal": 8.25, "plus_tol": 0.00, "minus_tol": 0.10, "direction": -1},
    {"name": "Part C", "nominal": 13.75, "plus_tol": 0.08, "minus_tol": 0.08, "direction": -1}
]

slot_stack = [
    {"name": "Slot", "nominal": 30.00, "plus_tol": 0.05, "minus_tol": 0.05, "direction": 1},
    {"name": "Shim 1", "nominal": 10.00, "plus_tol": 0.02, "minus_tol": 0.02, "direction": -1},
    {"name": "Shim 2", "nominal": 19.80, "plus_tol": 0.03, "minus_tol": 0.03, "direction": -1}
]

print('All values in mm')
print(f"{'Dimension':<10}{'Nominal':>10}{'Upper':>10}{'Lower':>10}")
for dim in housing_stack:
    upper_limit = calc_upper_limit(dim)
    lower_limit = calc_lower_limit(dim)
    print(f"{dim['name']:<10}{dim['nominal']:>10.3f}{upper_limit:>10.3f}{lower_limit:>10.3f}")

housing_gap = calc_nominal_gap(housing_stack)
slot_gap = calc_nominal_gap(slot_stack)
print(f"Housing nominal gap: {housing_gap:.3f} mm, Slot nominal gap: {slot_gap:.3f} mm")
