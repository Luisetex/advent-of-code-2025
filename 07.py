with open("inputs/07.txt", "r") as f:
    diagram = f.read().splitlines()

# A


def split_beam(
    beam_index: tuple[int, int], diagram: list[str]
) -> tuple[list[tuple[int, int]], bool]:
    next_indices = beam_index[0] + 1, beam_index[1]
    is_split = False
    if diagram[next_indices[0]][next_indices[1]] == ".":
        return [(next_indices[0] + 1, next_indices[1])], is_split
    is_split = True
    left = next_indices[0] + 1, next_indices[1] - 1
    right = next_indices[0] + 1, next_indices[1] + 1
    splits = []
    if 0 < left[0] < len(diagram) and 0 < left[1] < len(diagram[0]):
        splits.append(left)
    if 0 < right[0] < len(diagram) and 0 < right[1] < len(diagram[0]):
        splits.append(right)
    return splits, is_split


start_column = diagram[0].index("S")
beams: set[tuple[int, int]] = set()
beams.add((1, start_column))

total_splits = 0
for row in diagram[1:-1:2]:
    next_beams = set()
    for beam in beams:
        splits, is_split = split_beam(beam, diagram)
        total_splits += int(is_split)
        [next_beams.add(split_) for split_ in splits]
    beams = next_beams

print(total_splits)

# B


def find_timelines(
    beam_index: tuple[int, int], diagram: list[str], cache: dict[str, int]
):
    row, col = beam_index
    for next_row in range(row + 1, len(diagram)):
        if diagram[next_row][col] != ".":
            timelines = 0
            for offset in [-1, 1]:
                next_col = col + offset
                if 0 < next_col < len(diagram[0]):
                    key = f"{next_row}-{next_col}"
                    if key not in cache:
                        cache[key] = find_timelines(
                            (next_row, next_col), diagram, cache
                        )
                    timelines += cache[key]
            return timelines
    return 1


start_column = diagram[0].index("S")
start_index = (1, start_column)

print(find_timelines(start_index, diagram, {}) + 1)
