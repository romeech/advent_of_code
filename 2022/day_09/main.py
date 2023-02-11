from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'({self.x}, {self.y})'


def read_input(file_name):
    with open(file_name, 'r+') as f:
        motions = []
        for line in f:
            direction, amount = line.strip().split(' ')
            motions.append((direction, int(amount)))
        return motions


def apply_move(knots, move_head_fn):
    head = knots[0]
    knots[0] = move_head_fn(head)

    for i in range(len(knots) - 1):
        head = knots[i]
        tail = knots[i + 1]
        new_tail = adjust_tail(head, tail)
        knots[i + 1] = new_tail

    return knots[-1]


def adjust_tail(head, tail):
    new_tail = tail

    if head.x - tail.x == 2:  # right
        new_tail = Point(tail.x + 1, tail.y)
        new_tail.y = adjust_coord(head.y, tail.y)

    elif tail.x - head.x == 2:  # left
        new_tail = Point(tail.x - 1, tail.y)
        new_tail.y = adjust_coord(head.y, tail.y)

    elif head.y - tail.y == 2:  # up
        new_tail = Point(tail.x, tail.y + 1)
        new_tail.x = adjust_coord(head.x, tail.x)

    elif tail.y - head.y == 2:  # down
        new_tail = Point(tail.x, tail.y - 1)
        new_tail.x = adjust_coord(head.x, tail.x)

    return new_tail


def adjust_coord(head, tail):
    if head > tail:
        return tail + 1
    elif tail > head:
        return tail - 1
    else:
        return tail


def move_head_up(head):
    return Point(head.x, head.y + 1)


def move_head_down(head):
    return Point(head.x, head.y - 1)


def move_head_right(head):
    return Point(head.x + 1, head.y)


def move_head_left(head):
    return Point(head.x - 1, head.y)


def calc_tail_positions(motions, knots):
    tail = knots[-1]
    positions = {tail}

    moves = {
        'U': move_head_up,
        'D': move_head_down,
        'R': move_head_right,
        'L': move_head_left,
    }

    for direction, amount in motions:
        for i in range(1, amount + 1):
            positions.add(apply_move(knots, moves[direction]))

    return len(positions)


if __name__ == '__main__':
    motions = read_input('control.txt')
    knots = [Point(), Point()]
    tail_positions = calc_tail_positions(motions, knots)
    assert tail_positions == 13, f"Expected: 13, got: {tail_positions}"

    motions = read_input('input.txt')
    knots = [Point(), Point()]
    part1 = calc_tail_positions(motions, knots)
    print(f'Tail positions amount: {part1}')
    assert part1 == 5902

    motions = read_input('control2.txt')
    knots = [
        Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(),
    ]
    tail_positions = calc_tail_positions(motions, knots)
    assert tail_positions == 36, f"Expected: 36, got: {tail_positions}"

    motions = read_input('input.txt')
    knots = [
        Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(),
    ]
    part2 = calc_tail_positions(motions, knots)
    print(f'Tail positions amount: {part2}')
