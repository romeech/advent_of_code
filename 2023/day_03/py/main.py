from itertools import chain
from collections import defaultdict


class Number:
    def __init__(self, value, row_id, start_cell, end_cell):
        self.value = value
        self.row = row_id
        self.cell_start = start_cell
        self.cell_end = end_cell

    def __str__(self):
        return f"{self.value} ({self.row}, {self.cell_start} - {self.cell_end})"


def read_input(path):
    with open(path) as f:
        numbers = defaultdict(list)
        rows = []

        for row_id, line in enumerate(f):
            cells = []
            num_str = ''
            start = -1
            end = -1
            tracing = False

            for i, char in enumerate(line):
                if char.isdigit():
                    # start or continue process number parsing
                    if not tracing:
                        num_str = char
                        start = i
                        tracing = True
                    else:
                        num_str += char

                    cells.append(char)
                else:
                    # dot or a symbol
                    if tracing:
                        # finish parsing of a number
                        end = i
                        numbers[row_id].append(Number(int(num_str), row_id, start, end))
                        tracing = False

                    if char == '.':
                        cells.append(None)  # optimize storing chars
                    elif char != '\n':
                        cells.append(char)

            rows.append(cells)
    return rows, numbers


def sum_part_numbers(char_map, numbers):
    row_len = len(char_map[0])
    acc = 0
    asterisk_pairs = defaultdict(list)

    for num in chain.from_iterable(numbers.values()):
        cells_to_check = []
        # upper neighbours
        if num.row > 0:
            upper_row = [
                (num.row - 1, i)
                for i in range(num.cell_start - 1, num.cell_end + 1)
                if i >= 0 and i < row_len
            ]
            cells_to_check.extend(upper_row)

        # left neighbour
        if num.cell_start > 0:
            left_sibling = (num.row, num.cell_start - 1)
            cells_to_check.append(left_sibling)

        # right neighbour
        if num.cell_end < row_len - 1:
            right_sibling = (num.row, num.cell_end)
            cells_to_check.append(right_sibling)

        # lower neighbours
        if num.row < len(char_map) - 1:
            lower_row = [
                (num.row + 1, i)
                for i in range(num.cell_start - 1, num.cell_end + 1)
                if i >= 0 and i < row_len
            ]
            cells_to_check.extend(lower_row)

        is_part = False
        for i, j in cells_to_check:
            if (
                char_map[i][j] is not None
                and not char_map[i][j].isdigit()
            ):
                is_part = True
                if char_map[i][j] == '*':
                    asterisk_pairs[(i, j)].append(num.value)

        if is_part:
            acc += num.value

    gears_power = sum(nums[0] * nums[1] for key, nums in asterisk_pairs.items() if len(nums) == 2)
    return acc, gears_power


if __name__ == '__main__':
    char_map, numbers = read_input('data/control.txt')
    parts_sum, gears_power = sum_part_numbers(char_map, numbers)
    assert parts_sum == 4361, parts_sum
    assert gears_power == 467835, gears_power

    char_map, numbers = read_input('data/input.txt')
    parts_sum, gears_power = sum_part_numbers(char_map, numbers)
    print(f"The sum of all of the part numbers in the engine schematic: {parts_sum}")
    print(f"The sum of all of the gear ratios: {gears_power}")
