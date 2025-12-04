with open("input_03.txt") as f:
    banks = f.read().splitlines()

# A
joltage = 0
for bank in banks:
    batteries = [int(battery) for battery in bank]
    max_battery = 0
    max_index = -1
    for index, battery in enumerate(batteries[:-1]):
        if battery > max_battery:
            max_battery = battery
            max_index = index
    second_battery = max(batteries[max_index + 1 :])
    joltage += int("".join([str(max_battery), str(second_battery)]))

print(joltage)

#
# B
joltage = 0
selected_batteries_banks = []
for bank in banks:
    selected_batteries = ""
    batteries = [int(battery) for battery in bank]
    remaining_batteries = batteries
    while len(selected_batteries) < 12:
        for max_value in range(9, 0, -1):
            selected_batteries_length = len(selected_batteries)
            try:
                max_val_first_index = remaining_batteries.index(max_value)
            except:
                continue
            if len(remaining_batteries[max_val_first_index + 1 :]) >= 12 - (
                selected_batteries_length + 1
            ):
                selected_batteries += str(max_value)
                remaining_batteries = remaining_batteries[max_val_first_index + 1 :]
                break
    selected_batteries_banks.append(int(selected_batteries))

print(sum(selected_batteries_banks))
