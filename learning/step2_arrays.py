import numpy as np
np.set_printoptions(precision=3, floatmode="fixed")

nominals = np.array([50.00, 12.00, 15.50, 8.25, 13.75])
plus_tols = np.array([0.10, 0.05, 0.05, 0.00, 0.08])
minus_tols = np.array([0.10, 0.05, 0.05, 0.10, 0.08])
directions = np.array([1, -1, -1, -1, -1])

upper_limits = nominals + plus_tols
lower_limits = nominals - minus_tols

nominal_gap = np.sum(nominals * directions)

print("Upper limits (mm):", upper_limits)
print("Lower limits (mm):", lower_limits)
print(f"Nominal gap: {nominal_gap:.3f} mm")
