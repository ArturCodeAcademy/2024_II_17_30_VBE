def calculate(eaten_count, fruits):
    for i in range(10):
        fruits[i] -= eaten_count[i]

    for i in range(19):
        for j in range(19, 0, -1):
            fruits[j] = fruits[j - 1]
        fruits[0] = 0

        for j in range(20):
            if fruits[j] > 0:
                fruits[j] -= 1
                eaten_count[j] += 1


with open("U1.txt", "r") as fin:
    eaten_count = list(map(int, fin.readline().split()))
    eaten_count += [0] * 10
fruits = [10] * 10 + [0] * 10

calculate(eaten_count, fruits)

with open("U1rez.txt", "w") as fout:
    fout.write(" ".join(map(str, eaten_count)))


