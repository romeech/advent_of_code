def read_input(file_name):
    trees = []
    with open(file_name, 'r+') as f:
        for line in f:
            trees.append([int(height) for height in list(line.strip())])

    return trees


def count_visible_trees(trees):
    count = 0
    row_size = len(trees[0])
    col_size = len(trees)
    top_and_botton_rows = row_size * 2
    left_and_right_column = col_size * 2 - 4  # trees at corners have already been counted.
    count += top_and_botton_rows + left_and_right_column

    for row in range(1, col_size - 1):
        for col in range(1, row_size - 1):
            cur_tree = trees[row][col]

            # scan tree to top
            found_cover = False
            for i in range(0, row):
                if trees[i][col] >= cur_tree:
                    found_cover = True
                    break

            if not found_cover:
                count += 1
                continue

            # scan tree to bottow
            found_cover = False
            for i in range(row + 1, col_size):
                if trees[i][col] >= cur_tree:
                    found_cover = True
                    break

            if not found_cover:
                count += 1
                continue

            # scan tree to left
            found_cover = False
            for j in range(0, col):
                if trees[row][j] >= cur_tree:
                    found_cover = True
                    break

            if not found_cover:
                count += 1
                continue

            # scan tree to right
            found_cover = False
            for j in range(col + 1, row_size):
                if trees[row][j] >= cur_tree:
                    found_cover = True
                    break

            if not found_cover:
                count += 1

    return count


if __name__ == '__main__':
    trees = read_input('control.txt')

    control1 = count_visible_trees(trees)
    assert control1 == 21, control1

    trees = read_input('input.txt')
    part1 = count_visible_trees(trees)
    print(f'Trees are visible from outside the grid: {part1}')
