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


def move_step_up(head, tail):
    new_head = Point(head.x, head.y + 1)
    new_tail = Point(tail.x, tail.y)
    if abs(new_head.y - new_tail.y) > 1:
        new_tail.y += 1
        new_tail.x = adjust_coord(new_head.x, new_tail.x)

    return new_head, new_tail


def move_step_down(head, tail):
    new_head = Point(head.x, head.y - 1)
    new_tail = Point(tail.x, tail.y)
    if abs(new_head.y - new_tail.y) > 1:
        new_tail.y -= 1
        new_tail.x = adjust_coord(new_head.x, new_tail.x)

    return new_head, new_tail


def move_step_right(head, tail):
    new_head = Point(head.x + 1, head.y)
    new_tail = Point(tail.x, tail.y)
    if abs(new_head.x - new_tail.x) > 1:
        new_tail.x += 1
        new_tail.y = adjust_coord(new_head.y, new_tail.y)

    return new_head, new_tail


def move_step_left(head, tail):
    new_head = Point(head.x - 1, head.y)
    new_tail = Point(tail.x, tail.y)
    if abs(new_head.x - new_tail.x) > 1:
        new_tail.x -= 1
        new_tail.y = adjust_coord(new_head.y, new_tail.y)

    return new_head, new_tail


def calc_tail_positions(motions):
    head = Point()
    tail = Point()
    positions = {tail}

    moves = {
        'U': move_step_up,
        'D': move_step_down,
        'R': move_step_right,
        'L': move_step_left,
    }

    for direction, amount in motions:
        for i in range(1, amount + 1):
            head, tail = moves[direction](head, tail)
            positions.add(tail)

    return len(positions)


if __name__ == '__main__':
    motions = read_input('control.txt')
    tail_positions = calc_tail_positions(motions)
    assert tail_positions == 13, f"Expected: 13, got: {tail_positions}"

    motions = read_input('input.txt')
    part1 = calc_tail_positions(motions)
    print(f'Tail positions amount: {part1}')
