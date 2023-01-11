def read_control(file_path):
    data = []
    with open(file_path, 'r+') as f:
        for line in f:
            expected_pack, expected_msg, datastream = line.split(' ')
            data.append((expected_pack, expected_msg, datastream))

    return data


def read_input(file_path):
    with open(file_path, 'r+') as f:
        return f.read().strip()


def _find_unique_pos(chunk_size):
    for i in range(len(datastream) - chunk_size + 1):
        chunk = datastream[i:i + chunk_size]
        if len(set(chunk)) == chunk_size:
            return i + chunk_size

    return None


def find_packet(datastream):
    return _find_unique_pos(4)


def find_message(datastream):
    return _find_unique_pos(14)


if __name__ == '__main__':
    parsed = read_control('control.txt')
    for expected_pack, expected_msg, datastream in parsed:
        end_pack = find_packet(datastream)
        assert end_pack == int(expected_pack)

        end_msg = find_message(datastream)
        assert end_msg == int(expected_msg), expected_msg

    datastream = read_input('input.txt')
    part1 = find_packet(datastream)
    print(f'Characters before the start-of-packet marker: {part1}')

    part2 = find_message(datastream)
    print(f'Characters before the start-of-message marker: {part2}')
