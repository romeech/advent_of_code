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


def adjust_coord(head, tail):
    if head > tail:
        return tail + 1
    elif tail > head:
        return tail - 1
    else:
        return tail


def move_step_up(knots):
    head = knots[0]
    knots[0] = Point(head.x, head.y + 1)

    for i in range(len(knots) - 1):
        head = knots[i]
        tail = knots[i + 1]

        new_tail = Point(tail.x, tail.y)
        if abs(head.y - new_tail.y) > 1:
            new_tail.y += 1
            new_tail.x = adjust_coord(head.x, new_tail.x)
        knots[i + 1] = new_tail

    return new_tail


def move_step_down(knots):
    head = knots[0]
    knots[0] = Point(head.x, head.y - 1)

    for i in range(len(knots) - 1):
        head = knots[i]
        tail = knots[i + 1]

        new_tail = Point(tail.x, tail.y)
        if abs(head.y - new_tail.y) > 1:
            new_tail.y -= 1
            new_tail.x = adjust_coord(head.x, new_tail.x)
        knots[i + 1] = new_tail

    return new_tail


def move_step_right(knots):
    head = knots[0]
    knots[0] = Point(head.x + 1, head.y)

    for i in range(len(knots) - 1):
        head = knots[i]
        tail = knots[i + 1]

        new_tail = Point(tail.x, tail.y)
        if abs(head.x - new_tail.x) > 1:
            new_tail.x += 1
            new_tail.y = adjust_coord(head.y, new_tail.y)
        knots[i + 1] = new_tail

    return new_tail


def move_step_left(knots):
    head = knots[0]
    knots[0] = Point(head.x - 1, head.y)

    for i in range(len(knots) - 1):
        head = knots[i]
        tail = knots[i + 1]

        new_tail = Point(tail.x, tail.y)
        if abs(head.x - new_tail.x) > 1:
            new_tail.x -= 1
            new_tail.y = adjust_coord(head.y, new_tail.y)
        knots[i + 1] = new_tail

    return new_tail


def apply_move(knots, move_head_fn, adjust_tail_fn):
    head = knots[0]
    knots[0] = move_head_fn(head)

    for i in range(len(knots) - 1):
        head = knots[i]
        tail = knots[i + 1]
        new_tail = adjust_tail_fn(head, tail)
        knots[i + 1] = new_tail

    return knots[-1]


def move_head_up(head):
    return Point(head.x + 1, head.y)


def adjust_tail_up(head, tail):
    new_tail = Point(tail.x, tail.y)
    if abs(head.x - new_tail.x) > 1:
        new_tail.x -= 1
        new_tail.y = adjust_coord(head.y, new_tail.y)
    return new_tail


def move_head_down(head):
    return Point(head.x, head.y - 1)


def adjust_tail_down(head, tail):
    new_tail = Point(tail.x, tail.y)
    if abs(head.y - new_tail.y) > 1:
        new_tail.y -= 1
        new_tail.x = adjust_coord(head.x, new_tail.x)
    return new_tail


def move_head_right(head):
    return Point(head.x + 1, head.y)


def adjust_tail_right(head, tail):
    new_tail = Point(tail.x, tail.y)
    if abs(head.x - new_tail.x) > 1:
        new_tail.x += 1
        new_tail.y = adjust_coord(head.y, new_tail.y)
    return new_tail


def move_head_left(head):
    return Point(head.x - 1, head.y)


def adjust_tail_left(head, tail):
    new_tail = Point(tail.x, tail.y)
    if abs(head.x - new_tail.x) > 1:
        new_tail.x -= 1
        new_tail.y = adjust_coord(head.y, new_tail.y)
    return new_tail


def calc_tail_positions(motions, knots):
    tail = knots[-1]
    positions = {tail}

    moves = {
        'U': (move_head_up, adjust_tail_up),
        'D': (move_head_down, adjust_tail_down),
        'R': (move_head_right, adjust_tail_right),
        'L': (move_head_left, adjust_tail_left),
    }

    for direction, amount in motions:
        for i in range(1, amount + 1):
            move_head_fn, adjust_tail_fn = moves[direction]
            positions.add(apply_move(knots, move_head_fn, adjust_tail_fn))

    return len(positions)


if __name__ == '__main__':
    motions = read_input('control.txt')
    knots = [Point(), Point()]
    # Need to print traces, to find out why it's 17 now
    tail_positions = calc_tail_positions(motions, knots)
    assert tail_positions == 13, f"Expected: 13, got: {tail_positions}"

    motions = read_input('input.txt')
    knots = [Point(), Point()]
    part1 = calc_tail_positions(motions, knots)
    print(f'Tail positions amount: {part1}')
    assert part1 == 5902

    # TODO: Need to detect dynamically which adjust_tail_* fn should be applied
    # because adjust_coord may change x or y in two directions.
    knots = [Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point(), Point()]
    part2 = calc_tail_positions(motions, knots)
    print(f'Tail positions amount: {part2}')
