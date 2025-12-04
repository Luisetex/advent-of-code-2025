from utils import read_lines

# A
current_position = 50
dial_operations = read_lines("input_01.txt")
password = 0
for operation in dial_operations:
    SIGN = 1 if operation[0] == "R" else -1
    STEPS = int(operation[1:])
    current_position = (current_position + (STEPS * SIGN)) % 100
    if current_position == 0:
        password += 1
print(password)

# B

current_position = 50
dial_operations = read_lines("input_01.txt")
password = 0
for operation in dial_operations:
    SIGN = 1 if operation[0] == "R" else -1
    STEPS = int(operation[1:])
    if SIGN == 1:
        crosses = ((current_position + STEPS) // 100) - (current_position // 100)
    else:
        crosses = ((100 - current_position + STEPS) // 100) - (
            (100 - current_position) // 100
        )

    password += crosses
    current_position = (current_position + SIGN * STEPS) % 100

print(password)
