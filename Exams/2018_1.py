def calculate_flags(g, z, r):
    return min(g, z, r) // 2


with open("U1.txt", "r") as f:
    n = int(f.readline())
    g = 0
    z = 0
    r = 0

    for _ in range(n):
        color, count = f.readline().split()
        count = int(count)
        if color == "G":
            g += count
        elif color == "Z":
            z += count
        elif color == "R":
            r += count

    count = calculate_flags(g, z, r)
    g -= count * 2
    z -= count * 2
    r -= count * 2

with open("U1rez.txt", "w") as f:
    f.write(f"{count}\n")
    f.write(f"G = {g}\n")
    f.write(f"Z = {z}\n")
    f.write(f"R = {r}\n")

