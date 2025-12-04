def read_lines(path: str) -> list[str]:
    with open(path, "r") as text_file:
        lines = text_file.read().splitlines()
    return lines
