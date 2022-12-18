from copy import deepcopy

MODE_READ_STACKS = 0
MODE_SKIP_LINE = 1
MODE_READ_INSTRUCTIONS = 2


def parse_stacks(stacks_input, stacks_count):
    stacks = [[] for _ in range(stacks_count)]

    for i in range(1, len(stacks_input) + 1):
        nth_slice = stacks_input[-i]

        start = 0
        end = start + 3
        stack_id = 0

        while start < len(nth_slice):
            crate_str = nth_slice[start:end]
            if crate_str.strip():
                stacks[stack_id].append(crate_str[1])

            start = end + 1
            end = start + 3
            stack_id += 1

    return stacks


def parse_instructions(instructions_input):
    instructions = []

    for line in instructions_input:
        left, right = line.split(' from ')
        quantity = int(left.split('move ')[1])

        left, right = right.split(' to ')
        stack_from = int(left)
        stack_to = int(right)

        instructions.append((quantity, stack_from, stack_to))

    return instructions


def read_input(file_path):
    stacks, instructions = [], []
    raw_stacks, raw_instructions = [], []
    stacks_count = 0

    with open(file_path, 'r+') as f:
        mode = MODE_READ_STACKS

        for line in f:
            if mode == MODE_READ_STACKS:
                if line.strip().startswith('1'):
                    mode = MODE_SKIP_LINE
                    stacks_count = int(line.strip()[-1])
                else:
                    raw_stacks.append(line.rstrip())  # need to save whitespaces in places of crates

            elif mode == MODE_SKIP_LINE:
                mode = MODE_READ_INSTRUCTIONS
                continue

            else:
                raw_instructions.append(line.strip())

    stacks = parse_stacks(raw_stacks, stacks_count)
    instructions = parse_instructions(raw_instructions)
    return stacks, instructions


def apply_instructions_9000(stacks, instructions):
    for quantity, from_idx, to_idx in instructions:
        stack_from = stacks[from_idx - 1]
        stack_to = stacks[to_idx - 1]
        q = []

        for i in range(quantity):
            q.append(stack_from.pop())
        stack_to += q

    return stacks


def apply_instructions_9001(stacks, instructions):
    for quantity, from_idx, to_idx in instructions:
        stack_from = stacks[from_idx - 1]
        stack_to = stacks[to_idx - 1]
        q = []

        for i in range(quantity):
            q.append(stack_from.pop())
        while q:
            stack_to.append(q.pop())

    return stacks


def find_top_crates(stacks):
    tops = [stack[-1] for stack in stacks]
    return ''.join(tops)


if __name__ == '__main__':
    stacks, instructions = read_input('input.txt')

    arranged_stacks = apply_instructions_9000(deepcopy(stacks), instructions)

    top_crates = find_top_crates(arranged_stacks)
    print(f'Part 1 - crate ends up on top of each stack: {top_crates}')

    arranged_stacks = apply_instructions_9001(deepcopy(stacks), instructions)
    top_crates = find_top_crates(arranged_stacks)
    print(f'Part 2 - crate ends up on top of each stack: {top_crates}')
