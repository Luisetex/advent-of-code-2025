with open("tests/06.txt", "r") as f:
    problems = [line.split() for line in f.read().splitlines()]


def multiply(numbers: list[int]) -> int:
    prev = 1
    current = 1
    for number in numbers:
        current = prev * number
        prev = current
    return current


# A
results = []

for column in range(len(problems[0])):
    problem = [problems[row][column] for row in range(len(problems))]
    numbers = [int(number) for number in problem[:-1]]
    operand = problem[-1]
    results.append(sum(numbers) if operand == "+" else multiply(numbers))
print(sum(results))


# B
def parse_problems(problems: list[str]):
    parsed_problems = []
    parsed_problem = ""
    operator = ""
    for column in range(len(problems[0])):
        current_column = " "
        for row in range(len(problems)):
            char = (
                problems[row][column]
                if row != len(problems) - 1
                else problems[row][column] + " "
            )
            if "*" in char or "+" in char:
                operator = char.strip()
                continue
            current_column += char
        if current_column.split():
            parsed_problem += current_column
        else:
            parsed_problem += operator
            parsed_problems.append(parsed_problem)
            parsed_problem = ""
    parsed_problem += operator
    parsed_problems.append(parsed_problem)
    return parsed_problems


with open("inputs/06.txt", "r") as f:
    problems = [line for line in f.read().splitlines()]

parsed_problems = parse_problems(problems)
results = []
for parsed_problem in parsed_problems:
    numbers = [int(val) for val in parsed_problem[:-1].split()]
    operation = parsed_problem[-1]
    result = sum(numbers) if operation == "+" else multiply(numbers)
    results.append(result)

print(sum(results))
