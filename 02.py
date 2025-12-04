import math

with open("input_02.txt", "r") as input_file:
    ranges = [
        tuple(map(int, range_.split("-"))) for range_ in input_file.read().split(",")
    ]


def generate_palindromes(start, end):
    valid = []

    min_digits = len(str(start))
    max_digits = len(str(end))

    for num_digits in range(min_digits, max_digits + 1):
        if num_digits % 2 != 0:
            continue

        half_digits = num_digits // 2
        half_start = 10 ** (half_digits - 1) if half_digits > 1 else 0
        half_end = 10**half_digits

        for half in range(half_start, half_end):
            number = int(str(half) + str(half))
            if start <= number <= end:
                valid.append(number)

    return valid


total_a = 0
for start, end in ranges:
    total_a += sum(generate_palindromes(start, end))

print(total_a)


def generate_repeating_patterns(start, end):
    valid = set()

    min_digits = len(str(start))
    max_digits = len(str(end))

    for num_digits in range(min_digits, max_digits + 1):
        divisors = []
        for i in range(1, int(math.sqrt(num_digits)) + 1):
            if num_digits % i == 0:
                divisors.append(i)
                if i != num_digits // i and num_digits // i != num_digits:
                    divisors.append(num_digits // i)

        divisors = [d for d in divisors if d != num_digits]

        for pattern_len in divisors:
            repeats = num_digits // pattern_len

            pattern_start = 10 ** (pattern_len - 1) if pattern_len > 1 else 0
            pattern_end = 10**pattern_len

            for pattern in range(pattern_start, pattern_end):
                number = int(str(pattern) * repeats)

                if start <= number <= end and len(str(number)) == num_digits:
                    valid.add(number)

    return valid


total_b = 0
valid_all = set()
for start, end in ranges:
    valid_all.update(generate_repeating_patterns(start, end))

print(sum(valid_all))
