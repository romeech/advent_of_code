def read_input(file_path):
    codes = []
    with open(file_path, 'r+') as f:
        for line in f:
            codes.append(line.strip())
    return codes


def sum_calibration_values(codes):
    accum = 0
    for code in codes:
        fd, ld = 0, 0
        for i in range(len(code)):
            if code[i].isdigit():
                fd = int(code[i])
                break
        for i in range(len(code) - 1, -1, -1):
            if code[i].isdigit():
                ld = int(code[i])
                break
        accum += fd * 10 + ld
    return accum


DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def sum_calibration_values_2(codes):
    accum = 0
    for code in codes:
        fd, ld = 0, 0
        found = {}

        for d in range(1, 10):
            pos = code.find(str(d))
            if pos > -1:
                found[pos] = d

        for name in DIGITS.keys():
            pos = code.find(name)
            if pos > -1:
                found[pos] = DIGITS[name]

        fd = found[min(found.keys())]

        found = {}
        for d in range(1, 10):
            pos = code.rfind(str(d))
            if pos > -1:
                found[pos] = d

        for name in DIGITS.keys():
            pos = code.rfind(name)
            if pos > -1:
                found[pos] = DIGITS[name]

        ld = found[max(found.keys())]

        accum += fd * 10 + ld
    return accum


if __name__ == '__main__':
    # codes = read_input('control.txt')
    # values_sum = sum_calibration_values(codes)
    # assert values_sum == 142

    codes = read_input('input.txt')
    values_sum = sum_calibration_values(codes)
    print(f"The sum of all of the calibration values: {values_sum}")

    # codes = read_input('control2.txt')
    # values_sum = sum_calibration_values_2(codes)
    # assert values_sum == 281, values_sum

    from time import perf_counter_ns
    start = perf_counter_ns()
    codes = read_input('input.txt')
    values_sum = sum_calibration_values_2(codes)
    end = perf_counter_ns()
    print(
        f"The precise sum of all of the calibration values: {values_sum}."
        f"Time elapsed: {(end - start) / 10**9}"
    )

# The sum of all of the calibration values: 56465
# The precise sum of all of the calibration values: 55902