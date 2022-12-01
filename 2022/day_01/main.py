import heapq


def find_largest_calories_elf(summaries):
    return heapq.nlargest(1, summaries)[0]


def find_sum_of_top_3(summaries):
    return sum(heapq.nlargest(3, summaries))


def read_input(file_path):
    elves_summary = []
    with open(file_path, 'r+') as f:
        calories = 0
        for line in f:
            if line != '\n':
                calories += int(line)
            else:
                heapq.heappush(elves_summary, calories)
                calories = 0
    return elves_summary


if __name__ == '__main__':
    summaries = read_input('input.txt')

    max_calories = find_largest_calories_elf(summaries)
    print(f'Elf with the most Calories carries {max_calories}.')

    top3_sum = find_sum_of_top_3(summaries)
    print(f'The top three Elves carrying {top3_sum} calories.')
