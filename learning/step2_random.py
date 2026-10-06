import numpy as np
np.set_printoptions(precision=3, floatmode="fixed")

rng = np.random.default_rng(seed=7)
normal_samples = rng.normal(12.00, 0.05 / 3, 100_000)

mean = np.mean(normal_samples)
standard_dev = np.std(normal_samples)
sample_min = np.min(normal_samples)
sample_max = np.max(normal_samples)
print(f"Mean: {mean:.4f} mm, Standard Deviation: {standard_dev:.4f} mm. Minimum: {sample_min:.4f} mm, Maximum: {sample_max:.4f} mm")

outside_normal = (normal_samples < 11.95) | (normal_samples > 12.05)
pct_normal = np.mean(outside_normal) * 100
count_normal = np.sum(outside_normal)
print(f"Normal {count_normal} outside ({pct_normal}%)")

uniform_samples = rng.uniform(11.95, 12.05, 100_000)

mean_uniform = np.mean(uniform_samples)
standard_dev_uniform = np.std(uniform_samples)
print(f"Uniform Mean: {mean:.4f} mm, Uniform Standard Deviation: {standard_dev_uniform:.4f} mm")

outside_uniform = (uniform_samples < 11.95) | (uniform_samples > 12.05)
pct_uniform = np.mean(outside_uniform) * 100
count_uniform = np.sum(outside_uniform)
print(f"Uniform {count_uniform} outside ({pct_uniform}%)")