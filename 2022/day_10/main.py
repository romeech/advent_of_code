from pprint import PrettyPrinter


def read_input(file_name):
    with open(file_name, 'r+') as f:
        return [line.strip() for line in f]


def sum_nth_checkpoints(instructions, n, start, step):
    checkpoints = list(range(start, n * step + 1, step))
    actions = {
        'addx': 2,
        'noop': 1,
    }
    x = 1
    cycle_num = 0
    checkpoint_sum = 0

    for instr in instructions:
        act = instr.split(' ')[0]
        cycle_count = actions[act]
        for _ in range(cycle_count):
            cycle_num += 1
            if cycle_num in checkpoints:
                checkpoint_sum += cycle_num * x
        if act == 'addx':
            arg = instr.split(' ')[1]
            x += int(arg)

    return checkpoint_sum


def draw_screen(instructions, screen_height, screen_with):
    screen = [['.' for _ in range(screen_with)] for _ in range(screen_height)]

    actions = {
        'addx': 2,
        'noop': 1,
    }
    x = 1
    cycle_num = 0

    for instr in instructions:
        act = instr.split(' ')[0]
        cycle_count = actions[act]
        for _ in range(cycle_count):
            cycle_num += 1
            cur_line = (cycle_num - 1) // screen_with
            cur_pos = (cycle_num - 1) % screen_with

            if (x - 2 < cur_pos < x + 2):
                pixel = '#'
            else:
                pixel = '.'

            screen[cur_line][cur_pos] = pixel

        if act == 'addx':
            arg = instr.split(' ')[1]
            x += int(arg)

    return [''.join(line) for line in screen]


if __name__ == '__main__':
    instructions = read_input('control.txt')
    val = sum_nth_checkpoints(instructions, 6, 20, 40)
    control_val = 13140
    assert val == control_val, f"Expected: {control_val}, Got: {val}"

    instructions = read_input('input.txt')
    part1 = sum_nth_checkpoints(instructions, 6, 20, 40)
    print(f'The sum of these six signal strengths: {part1}')

    pp = PrettyPrinter(indent=4)
    pp.pprint(draw_screen(instructions, 6, 40))
