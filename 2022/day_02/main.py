DRAW_MAP = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}
WIN_MAP = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
}
VALUES_MAP = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

LOSE_ACTS_MAP = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}
WIN_ACTS_MAP = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}
DRAW_ACTS_MAP = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
ACTIONS_MAP = {
    'X': (LOSE_ACTS_MAP, 0),
    'Y': (DRAW_ACTS_MAP, 3),
    'Z': (WIN_ACTS_MAP, 6),
}


def read_input(file_path):
    strategy_guide = []
    with open(file_path, 'r+') as f:
        for line in f:
            opps, yours = line.strip().split(' ')
            strategy_guide.append((opps, yours))
    return strategy_guide


def apply_guide(guide):
    result = 0
    for opps, yours in guide:
        round_val = VALUES_MAP[yours]
        if WIN_MAP[yours] == opps:
            round_val += 6
        elif DRAW_MAP[yours] == opps:
            round_val += 3

        result += round_val

    return result


def apply_guide_by_elf_rules(guide):
    result = 0
    for opps, yours in guide:
        figures_map, mod = ACTIONS_MAP[yours]
        result += VALUES_MAP[figures_map[opps]] + mod

    return result


if __name__ == '__main__':
    guide = read_input('input.txt')

    part1 = apply_guide(guide)
    print(f"Part 1: total score by your strategy: {part1}")

    part2 = apply_guide_by_elf_rules(guide)
    print(f"Part 2: total score by the elf strategy: {part2}")
