from functools import reduce


def read_input(path):
    with open(path) as f:
        result = f.read()

    return result


class Fsm:
    FSM_MAP = {
        'm': 'u',
        'u': 'l',
        'l': '(',
        '(': 'd1',
        'd1': 'd2',
        'd2': 'd3',
        'd3': ',',
        ',': 'd4',
        'd4': 'd5',
        'd5': 'd6',
        'd6': ')',
        ')': 'flush',
    }
    INIT_STATE = 'm'

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = ''
        self.y = ''
        self.state = self.INIT_STATE

    def transit(self):
        self.state = self.FSM_MAP[self.state]

    def add_digit(self, digit):
        place = int(self.state[1])
        if place < 4:
            self.x += digit
        else:
            self.y += digit

    def x_done(self):
        if self.x:
            self.state = self.FSM_MAP[',']
        else:
            self.reset()

    def y_done(self):
        if self.y:
            self.state = self.FSM_MAP[')']
        else:
            self.reset()

    @property
    def is_digit_scan(self):
        return self.state.startswith('d')

    @property
    def is_flush(self):
        return self.state == 'flush'

    def make_pair(self):
        return int(self.x), int(self.y)


def parse_muls(hay):
    pairs = []
    fsm = Fsm()
    i = 0

    while i < len(hay):
        if fsm.is_flush:
            pairs.append(fsm.make_pair())
            fsm.reset()
            continue

        char = hay[i]

        if fsm.is_digit_scan:
            if char.isdigit():
                fsm.add_digit(char)
                fsm.transit()

            elif char == ',':  # x is less than 3-digit num
                fsm.x_done()

            elif char == ')':  # y is less than 3-digit num
                fsm.y_done()

            else:
                fsm.reset()

        elif char == fsm.state:
            fsm.transit()

        else:
            fsm.reset()

        i += 1

    return pairs


def sum_pairs(pairs):
    return reduce(lambda acc, pair: acc + pair[0] * pair[1], pairs, 0)


if __name__ == '__main__':
    hay = read_input('data/control.txt')
    pairs = parse_muls(hay)
    mulsum = sum_pairs(pairs)
    print(mulsum)

    hay = read_input('data/input.txt')
    pairs = parse_muls(hay)
    mulsum = sum_pairs(pairs)
    print(mulsum)

