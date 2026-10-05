housing_inside_length = 50.0
part_lengths = [12.0, 15.5, 8.25, 13.75]
number_of_parts = len(part_lengths)
print(f"Number of parts: {number_of_parts}")
print(f"First part: {part_lengths[0]:.2f} mm, last part: {part_lengths[-1]:.2f} mm")
for part in part_lengths:
    print(f"Part: {part:.2f} mm")

total_length = 0
for part_length in part_lengths:
    total_length = total_length + part_length

nominal_gap = housing_inside_length - total_length
print(f"Total (loop): {total_length:.3f} mm")
print(f"Total (sum): {sum(part_lengths):.3f} mm")
print(f"Nominal gap: {nominal_gap:.3f} mm")
