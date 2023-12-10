def read_input(path):
    cards = []
    with open(path) as f:
        for line in f:
            w, h = line.split(':')[1].split('|')
            win = set(w.split())
            have = set(h.split())
            cards.append((win, have))

    return cards


def calculate_cards_worth(cards):
    total_worth = 0
    matches_map = {}

    for i, (win, have) in enumerate(cards):
        match_count = len(set(have).intersection(set(win)))
        if match_count:
            total_worth += 1 * 2**(match_count - 1)

        matches_map[i + 1] = match_count

    return total_worth, matches_map


def count_scratchcards(matches_map):
    scards_count = 0
    win_stack = [card_id for card_id, match_count in matches_map.items()]

    while len(win_stack):
        card_id = win_stack.pop()
        scards_count += 1
        match_count = matches_map[card_id]
        if match_count:
            copies_ids = [card_id + i for i in range(1, match_count + 1)]
            win_stack.extend(copies_ids)

    return scards_count


def count_scratchcards_win0err(matches_map):
    cards_count = [1] * len(matches_map)

    for idx, (_, match_count) in enumerate(matches_map.items()):
        for i in range(match_count):
            cards_count[idx + 1 + i] += cards_count[idx]

    return sum(cards_count)


if __name__ == '__main__':
    cards = read_input('data/control.txt')
    total_worth, matches_map = calculate_cards_worth(cards)
    scards_count = count_scratchcards(matches_map)
    assert total_worth == 13, total_worth
    assert scards_count == 30, scards_count

    cards = read_input('data/input.txt')
    total_worth, matches_map = calculate_cards_worth(cards)
    print(f"Total worth of the cards: {total_worth} pts.")
    scards_count = count_scratchcards(matches_map)
    print(f"Total number of the cards: {scards_count}.")
