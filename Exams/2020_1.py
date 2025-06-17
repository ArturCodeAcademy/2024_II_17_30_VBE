def index_from_date(month, day):
    if month == 6:
        return day - 1
    if month == 7:
        return 30 + day - 1
    return 30 + 31 + day - 1


def date_from_index(index):
    if index < 30:
        return 6, index + 1
    if index < 30 + 31:
        return 7, index - 30 + 1
    return 8, index - 30 - 31 + 1


def find_first_day_index_with_max_flowers(flowers_count, max_count):
    for i, el in enumerate(flowers_count):
        if el == max_count:
            return i


def find_last_day_index_with_max_flowers(flowers_count, first_day_index):
    for i in range(first_day_index, len(flowers_count)):
        if flowers_count[i] != flowers_count[first_day_index]:
            return i - 1
    return 91


flowers_count = [0] * 92

with open("U1.txt", "r") as fin:
    n = int(fin.readline())
    for _ in range(n):
        _, from_month, from_day, to_month, to_day = map(int, fin.readline().split())
        from_index = index_from_date(from_month, from_day)
        to_index = index_from_date(to_month, to_day)
        for i in range(from_index, to_index + 1):
            flowers_count[i] += 1

max_count = max(flowers_count)
first_day_index = find_first_day_index_with_max_flowers(flowers_count, max_count)
last_day_index = find_last_day_index_with_max_flowers(flowers_count, first_day_index)
from_month, from_day = date_from_index(first_day_index)
to_month, to_day = date_from_index(last_day_index)

with open("U1rez.txt", "w") as fout:
    fout.write(f"{max_count}\n")
    fout.write(f"{from_month} {from_day}\n")
    fout.write(f"{to_month} {to_day}")