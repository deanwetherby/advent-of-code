import re

not_important_chars = "0123456789."

with open("input.txt", "r") as f:
    data = f.read().splitlines()

gear_ratios_total = 0
gears = {}
for i, line in enumerate(data):
    line_gears = re.finditer(r"\*", line)
    gears[i] = line_gears

for idx, line_gear in gears.items():
    for gear in line_gear:
        gear_window = set(range(gear.start()-1, gear.end()+1))
        gear_adjacent = []
        # print("resetting gear list")
        for num_idx in range(idx-1 if idx > 0 else 0, idx+2 if idx < len(data) else idx+1):
            line_numbers = re.finditer(r"\d+", data[num_idx])
            for num in line_numbers:
                num_range = range(num.start(), num.end())
                # print(num.group(), num_range, gear_window, gear_window.intersection(num_range))
                if(gear_window.intersection(num_range)):
                    # print(f"adding {num.group()}")
                    gear_adjacent.append(num.group()) #print(num.group())
                # input()
        # print(idx, gear_adjacent)
        if len(gear_adjacent) > 1:
            # print("possible multiply")
            gear_ratios_total += int(gear_adjacent[0]) * int(gear_adjacent[1])

print(f"gear_ratio_total={gear_ratios_total}")
