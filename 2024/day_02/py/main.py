def read_input(filepath):
    with open(filepath) as f:
        return [[int(lvl) for lvl in line.split()] for line in f.readlines()]


def is_safe_report(elem, next_elem, old_sign):
    diff = abs(next_elem - elem)
    if not diff or diff > 3:
        return False, old_sign

    sign = (next_elem - elem) // diff
    if old_sign and sign != old_sign:
        return False, sign

    return True, sign


def count_safe_reports(reports):
    result = 0

    for rep in reports:
        sign = None
        is_safe = True

        for i in range(len(rep) - 1):
            is_safe, sign = is_safe_report(rep[i], rep[i + 1], sign)
            if not is_safe:
                break

        if is_safe:
            result += 1

    return result


def count_merely_safe_reports(reports):
    result = 0

    for rep in reports:
        is_safe = False
        skip_idx = -1

        while not is_safe and skip_idx < len(rep):
            scan_elems = [e for i, e in enumerate(rep) if i != skip_idx]

            sign = None
            for i in range(len(scan_elems) - 1):
                is_safe, sign = is_safe_report(scan_elems[i], scan_elems[i + 1], sign)
                if not is_safe:
                    break

            skip_idx += 1

        if is_safe:
            result += 1

    return result


if __name__ == '__main__':
    reports = read_input('data/control.txt')
    safe_count = count_safe_reports(reports)
    tolerate_count = count_merely_safe_reports(reports)
    print(f'{safe_count=}, {tolerate_count=}')

    reports = read_input('data/input.txt')
    safe_count = count_safe_reports(reports)
    tolerate_count = count_merely_safe_reports(reports)
    print(f'{safe_count=}, {tolerate_count=}')
