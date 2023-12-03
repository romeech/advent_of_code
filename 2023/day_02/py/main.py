from functools import reduce


def read_input(file_path):
    codes = []
    with open(file_path, 'r+') as f:
        for line in f:
            codes.append(line.strip())
    return codes


LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def sum_possible(games):
    accum = 0
    for game in games:
        header, body = game.split(':')
        game_id = header.split(' ')[1]
        if is_game_possible(body):
            accum += int(game_id, base=10)

    return accum


def is_game_possible(game: str) -> bool:
    rounds = [r.strip() for r in game.split(';')]

    for r in rounds:
        stones = r.split(', ')

        for s in stones:
            num, name = s.split(' ')

            if int(num, base=10) > LIMITS[name]:
                return False

    return True


def sum_powers_of_mins(games):
    accum = 0
    for game in games:
        _, body = game.split(':')
        power = find_game_power(body)
        accum += power

    return accum


def find_game_power(game):
    stones_limits = {'red': 1, 'blue': 1, 'green': 1}
    rounds = [r.strip() for r in game.split(';')]

    for r in rounds:
        stones = r.split(', ')

        for s in stones:
            num, color = s.split(' ')
            stone_amount = int(num)
            if stone_amount > stones_limits[color]:
                stones_limits[color] = stone_amount

    return reduce(lambda x, acc: x * acc, stones_limits.values(), 1)


if __name__ == '__main__':
    games = read_input('../data/control.txt')
    res = sum_possible(games)
    assert res == 8, res

    total_power = sum_powers_of_mins(games)
    assert total_power == 2286, total_power

    games = read_input('../data/input.txt')
    res = sum_possible(games)
    print(f"The sum of IDs of the valid games: {res}")

    total_power = sum_powers_of_mins(games)
    print(f"The sum of the power of minimal sets: {total_power}")
