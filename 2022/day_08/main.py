def read_input(file_name):
    trees = []
    with open(file_name, 'r+') as f:
        for line in f:
            trees.append([int(height) for height in list(line.strip())])

    return trees


def is_visible(row, col, trees):
    cur_tree = trees[row][col]
    row_size = len(trees[0])
    col_size = len(trees)

    # scan tree to top
    found_cover = False
    for i in range(row - 1, -1, -1):
        if trees[i][col] >= cur_tree:
            found_cover = True
            break

    if not found_cover:
        return True

    # scan tree to bottow
    found_cover = False
    for i in range(row + 1, col_size):
        if trees[i][col] >= cur_tree:
            found_cover = True
            break

    if not found_cover:
        return True

    # scan tree to left
    found_cover = False
    for j in range(col - 1, -1, -1):
        if trees[row][j] >= cur_tree:
            found_cover = True
            break

    if not found_cover:
        return True

    # scan tree to right
    found_cover = False
    for j in range(col + 1, row_size):
        if trees[row][j] >= cur_tree:
            found_cover = True
            break

    if not found_cover:
        return True

    return False


def calc_scenic_score(row, col, trees):
    cur_tree = trees[row][col]
    row_size = len(trees[0])
    col_size = len(trees)
    scenic_score = 1

    # scan tree to top
    score = 0
    for i in range(row - 1, -1, -1):
        score += 1
        if trees[i][col] >= cur_tree:
            break
    scenic_score *= score

    # scan tree to bottow
    score = 0
    for i in range(row + 1, col_size):
        score += 1
        if trees[i][col] >= cur_tree:
            break
    scenic_score *= score

    # scan tree to left
    score = 0
    for j in range(col - 1, -1, -1):
        score += 1
        if trees[row][j] >= cur_tree:
            break
    scenic_score *= score

    # scan tree to right
    score = 0
    for j in range(col + 1, row_size):
        score += 1
        if trees[row][j] >= cur_tree:
            break
    scenic_score *= score

    return scenic_score


def count_visible_trees(trees):
    count = 0
    row_size = len(trees[0])
    col_size = len(trees)
    top_and_botton_rows = row_size * 2
    left_and_right_column = col_size * 2 - 4  # trees at corners have already been counted.
    count += top_and_botton_rows + left_and_right_column

    for row in range(1, col_size - 1):
        for col in range(1, row_size - 1):
            if is_visible(row, col, trees):
                count += 1

    return count


def find_best_scenic_score(trees):
    scenic_scores = []
    row_size = len(trees[0])
    col_size = len(trees)

    # skip trees at edges - their scores will be apriory less than ones of trees inside.
    for row in range(1, col_size - 1):
        for col in range(1, row_size - 1):
            scenic_scores.append(calc_scenic_score(row, col, trees))

    return max(scenic_scores)


if __name__ == '__main__':
    trees = read_input('control.txt')

    control1 = count_visible_trees(trees)
    assert control1 == 21, control1

    for row, col, expected in (
        (1, 2, 4),
        (3, 2, 8),
    ):
        score = calc_scenic_score(row, col, trees)
        err_msg = f'scenic score for [{row}][{col}] failed:\nExpected: {expected}\nGot: {score}'
        assert score == expected, err_msg

    trees = read_input('input.txt')
    part1 = count_visible_trees(trees)
    print(f'Trees are visible from outside the grid: {part1}')  # 1803

    part2 = find_best_scenic_score(trees)
    print(f'Highest scenic score: {part2}')
