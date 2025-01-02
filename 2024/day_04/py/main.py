from itertools import chain


def read_input(path):
    matrix = []
    with open(path) as f:
        for line in f.readlines():
            matrix.append(line.strip())

    return matrix


def make_rotations(initial):
    rotations = [initial]  # 0 degrees
    current = initial
    for i in range(3):  # 3 rotations - 90, 180 and 270 degrees
        current = [line[::-1] for line in zip(*current)]
        rotations.append(current)
    return rotations


def count_word(screen, word):
    counter = 0

    # lines and colums scan
    columns = [''.join(line) for line in zip(*screen)]
    for line in chain(screen, columns):
        counter += line.count(word)
        counter += line[::-1].count(word)

    # diagonals
    for rotation in make_rotations(screen):
        for i in range(len(rotation) - len(word) + 1):
            for j in range(len(rotation[0]) - len(word) + 1):
                diagonal = ''

                for k in range(len(word)):
                    diagonal += rotation[i + k][j + k]

                if diagonal == word:
                    counter += 1

    return counter


def count_crosses(screen):
    cross = [
        ('M', '.', 'M'),
        ('.', 'A', '.'),
        ('S', '.', 'S'),
    ]
    options = make_rotations(cross)

    counter = 0
    for i in range(len(screen) - 2):
        for j in range(len(screen[0]) - 2):
            window = [
                (screen[i][j], '.', screen[i][j + 2]),
                ('.', screen[i + 1][j + 1], '.'),
                (screen[i + 2][j], '.', screen[i + 2][j + 2]),
            ]
            if window in options:
                counter += 1

    return counter


if __name__ == '__main__':

    screen = read_input('data/control.txt')
    res = count_word(screen, 'XMAS')
    print(f'Words, control.txt: {res}')
    res = count_crosses(screen)
    print(f'Crosses, control.txt: {res}')

    screen = read_input('data/input.txt')
    res = count_word(screen, 'XMAS')
    print(f'Words, input.txt: {res}')
    res = count_crosses(screen)
    print(f'Crosses, input.txt: {res}')
