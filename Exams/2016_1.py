def find_max():
    max_weight = 0
    with open("U1.txt", "r") as f:
        n = int(f.readline())
        for _ in range(n):
            weigth = int(f.readline())
            if weigth > max_weight:
                max_weight = weigth
    return max_weight


def count_bags(max_weight):
    count = 0
    with open("U1.txt", "r") as f:
        n = int(f.readline())
        for _ in range(n):
            weigth = int(f.readline())
            if weigth * 2 <= max_weight:
                count += 1
    return count


max_weight = find_max()
count = count_bags(max_weight)

with open("U1rez.txt", "w") as f:
    f.write(f"{max_weight} {count}")