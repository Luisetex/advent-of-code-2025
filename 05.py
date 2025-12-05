with open("inputs/05.txt") as f:
    lines = f.read().split("\n\n")
    ranges = lines[0].splitlines()
    ingredients = lines[1].splitlines()


# A
def check_in_range(ranges: list[str], ing: str):
    for range_ in ranges:
        min_range, max_range = [int(ran) for ran in range_.split("-")]
        if min_range <= int(ing) <= max_range:
            return True
    return False


print(sum([check_in_range(ranges, ing) for ing in ingredients]))


# B
def merge_ranges(ranges: list[str]):
    parsed_ranges = []
    for range_ in ranges:
        min_range, max_range = [int(ran) for ran in range_.split("-")]
        parsed_ranges.append([min_range, max_range])
    parsed_ranges.sort()

    merged_ranges = [parsed_ranges[0]]
    for parsed_range in parsed_ranges[1:]:
        last_merged = merged_ranges[-1]
        if parsed_range[0] <= last_merged[1] + 1:
            last_merged[1] = max(last_merged[1], parsed_range[1])
        else:
            merged_ranges.append(parsed_range)

    return merged_ranges


merged_ranges = merge_ranges(ranges)
print(sum((range_[1] - range_[0] + 1) for range_ in merged_ranges))
