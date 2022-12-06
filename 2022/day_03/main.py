def read_input(file_path):
    with open(file_path, 'r+') as f:
        return [rucksack.strip() for rucksack in f]


def split_compartments(rucksack):
    return rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]


def decode_priority(char):
    if char.islower():
        priority = ord(char) - 96
    else:
        priority = ord(char) - 38
    return priority


def sum_priorities(packs):
    result = 0
    for rucksack in packs:
        first, second = split_compartments(rucksack)
        violation = set(first).intersection(set(second))

        assert len(violation) == 1

        result += decode_priority(violation.pop())
    return result


def sum_badges(packs):
    assert len(packs) % 3 == 0

    result = 0
    offset = 0
    for i in range(len(packs) // 3):
        r1 = packs[i + offset]
        r2 = packs[i + 1 + offset]
        r3 = packs[i + 2 + offset]

        badge = set(r1).intersection(set(r2)).intersection(set(r3)).pop()
        result += decode_priority(badge)

        offset += 2

    return result


if __name__ == '__main__':
    packs = read_input('input.txt')
    part1 = sum_priorities(packs)
    print(f"The sum of the priorities of those item types: {part1}")
    part2 = sum_badges(packs)
    print(f"The sum of the priorities of those item types: {part2}")
