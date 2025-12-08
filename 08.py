from itertools import combinations

with open("tests/08.txt") as f:
    boxes: list[tuple[int, ...]] = [
        tuple(int(x) for x in box.split(",")) for box in f.read().splitlines()
    ]


def get_distance(box_1: tuple[int, ...], box_2: tuple[int, ...]) -> int:
    x1, y1, z1 = box_1
    x2, y2, z2 = box_2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2


# A
total_circuits = 0

distances = []
for box_1, box_2 in combinations(boxes, 2):
    circuit = 0
    distance = get_distance(box_1, box_2)
    distances.append([box_1, box_2, distance, circuit])

distances.sort(key=lambda x: x[2])

print(distances)
