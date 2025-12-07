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


def find_timelines(beam_index: tuple[int, int], grid, cache: dict[str, int]):
    timelines = 0
    found = False
    for next_row_index in range(beam_index[0] + 1, len(grid)):
        if grid[next_row_index][beam_index[1]] == ".":
            continue
        left = next_row_index, beam_index[1] - 1
        right = next_row_index, beam_index[1] + 1
        left_key = str(left[0]) + "-" + str(left[1])
        right_key = str(right[0]) + "-" + str(right[1])
        if 0 < beam_index[1] - 1 < len(grid[0]):
            if left_key in cache:
                timelines += cache[left_key]
            else:
                found_timelines = find_timelines(left, grid, cache)
                cache[left_key] = found_timelines
                timelines += found_timelines
            found = True
        if 0 < beam_index[1] + 1 < len(grid[0]):
            if right_key in cache:
                timelines += cache[right_key]
            else:
                found_timelines = find_timelines(right, grid, cache)
                cache[right_key] = found_timelines
                timelines += found_timelines
            found = True
        if found:
            break
    if next_row_index == len(grid) - 1:
        timelines += 1
    return timelines


start_column = diagram[0].index("S")
start_index = (1, start_column)

print(find_timelines(start_index, diagram, {}) + 1)
