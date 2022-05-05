def main(input_string: str) -> bool:
    size: int = len(input_string)
    if size == 0:
        return False

    last_index_of_a: int | None = None
    last_index_of_b: int | None = None

    for index, char in enumerate(input_string):
        if char == 'a':
            last_index_of_a = index
        if char == 'b':
            last_index_of_b = index
        if last_index_of_a is not None and last_index_of_b is not None:
            if last_index_of_b < last_index_of_a:
                return False
    return True
