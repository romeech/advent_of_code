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
        '(': 'i1',
        'i1': 'i2',
        'i2': 'i3',
        'i3': ',',
        ',': 'i4',
        'i4': 'i5',
        'i5': 'i6',
        'i6': ')',
        ')': 'flush',
    }
    SWITCH_MAP = {
        'd': 'o',
        'o': 'n',
        'n': "'",
        "'": 't',
        't': '(',
        '(': ')',
        ')': 'flush',
    }
    INIT_STATE = 'm'

    def __init__(self):
        self.reset()
        self.is_on = True
        self.pairs = []

    def reset(self):
        self.x = ''
        self.y = ''
        self.map = self.FSM_MAP
        self.state = self.INIT_STATE
        self.flush = self.add_pair

    def transit(self):
        self.state = self.map[self.state]

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
        return self.state.startswith('i')

    @property
    def is_switch_scan(self):
        return self.map == self.SWITCH_MAP

    @property
    def is_flush(self):
        return self.state == 'flush'

    def is_switch_start(self, char):
        return char == 'd'

    def parse_switch(self):
        self.map = self.SWITCH_MAP
        self.state = 'd'
        self.transit()

    def finish_switch(self):
        if self.state == 'n':
            self.flush = self.do_done
            self.state = '('
            self.transit()

        elif self.state == '(':
            self.flush = self.dont_done
            self.transit()

        else:
            self.reset()

    # Flushers

    def add_pair(self):
        if self.is_on:
            self.pairs.append((int(self.x), int(self.y)))
        self.reset()

    def do_done(self):
        self.is_on = True
        self.reset()

    def dont_done(self):
        self.is_on = False
        self.reset()


def parse_muls(hay):
    fsm = Fsm()
    i = 0

    while i < len(hay):
        if fsm.is_flush:
            fsm.flush()
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

        elif fsm.is_switch_start(char):
            fsm.parse_switch()

        elif fsm.is_switch_scan and char == '(':
            fsm.finish_switch()

        elif char == fsm.state:
            fsm.transit()

        else:
            fsm.reset()

        i += 1

    return fsm.pairs


def sum_pairs(pairs):
    return reduce(lambda acc, pair: acc + pair[0] * pair[1], pairs, 0)


if __name__ == '__main__':
    hay = read_input('data/control.txt')
    pairs = parse_muls(hay)
    mulsum = sum_pairs(pairs)
    print(mulsum)

    hay = read_input('data/control2.txt')
    pairs = parse_muls(hay)
    mulsum = sum_pairs(pairs)
    print(mulsum)

    # Part 1 answer: 178794710
    hay = read_input('data/input.txt')
    pairs = parse_muls(hay)
    mulsum = sum_pairs(pairs)
    print(mulsum)

