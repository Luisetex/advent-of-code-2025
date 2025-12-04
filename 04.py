import itertools

with open("input_04.txt", "r") as f:
    grid = [
        [True if el == "@" else False for el in line] for line in f.read().splitlines()
    ]

MAX_ROWS = len(grid)
MAX_COLS = len(grid[0])


def check_adjacents(pos_x: int, pos_y: int, grid: list[list[bool]], threshold: int):
    DX = (-1, 0, 1)
    DY = (-1, 0, 1)

    valid_positions = [
        (pos_x + dx, pos_y + dy)
        for dx, dy in itertools.product(DX, DY)
        if (
            0 <= (pos_x + dx) < MAX_COLS
            and (0 <= (pos_y + dy) < MAX_ROWS)
            and not (dx == 0 and dy == 0)
        )
    ]

    adjacents = sum([grid[position[1]][position[0]] for position in valid_positions])
    is_ok = adjacents < threshold
    return is_ok, [pos_x, pos_y]


def remove_grid(results: list[tuple[bool, list[int]]], grid: list[list[bool]]):
    removables = [result for result in results if result[0]]
    pos_to_remove = [removable[1] for removable in removables]
    for pos in pos_to_remove:
        grid[pos[1]][pos[0]] = False
    return grid


# A

results = [
    check_adjacents(x, y, grid, 4)
    for y, row in enumerate(grid)
    for x, col in enumerate(grid[y])
    if grid[y][x]
]

print(sum([result[0] for result in results]))

# B

to_remove = 999999
removed = 0
while to_remove != 0:
    results = [
        check_adjacents(x, y, grid, 4)
        for y, row in enumerate(grid)
        for x, col in enumerate(grid[y])
        if grid[y][x]
    ]
    to_remove = sum([result[0] for result in results])
    removed += to_remove
    grid = remove_grid(results, grid)
print(removed)
