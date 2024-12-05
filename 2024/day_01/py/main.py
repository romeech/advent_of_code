def read_input(filepath):
    left_side, right_side = [], []

    with open(filepath) as f:
        for line in f.readlines():
            left, right = line.split('   ')
            left_side.append(int(left))
            right_side.append(int(right))

    left_side.sort()
    right_side.sort()
    return left_side, right_side


def sum_minimals(left, right):
    assert len(left) == len(right)

    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])

    return result


def calc_similarity_score(left, right):
    similarity_score = 0

    for lv in left:
        try:
            r_idx = right.index(lv)
        except ValueError:
            r_idx = -1

        count = 0
        if r_idx > -1:
            while right[r_idx] == lv:
                count += 1
                r_idx += 1

        similarity_score += lv * count

    return similarity_score


if __name__ == '__main__':
    left, right = read_input('data/control.txt')
    distance_sum = sum_minimals(left, right)
    sim_score = calc_similarity_score(left, right)
    print(f"{distance_sum=}, {sim_score=}")

    left, right = read_input('data/input.txt')
    distance_sum = sum_minimals(left, right)
    sim_score = calc_similarity_score(left, right)
    print(f"{distance_sum=}, {sim_score=}")
