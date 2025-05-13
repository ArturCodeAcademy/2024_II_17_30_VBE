def convert_to_hex(n):
    hex_nums = "0123456789ABCDEF"
    return hex_nums[n // 16] + hex_nums[n % 16]


with open("U1.txt", "r") as fin, open("U1rez.txt", "w") as fout:
    n, m = map(int, fin.readline().split())
    for i in range(n):
        for j in range(m):
            r, g, b = map(int, fin.readline().split())
            color = convert_to_hex(r) + convert_to_hex(g) + convert_to_hex(b)
            fout.write(color)
            if j == m - 1:
                fout.write("\n")
            else:
                fout.write(";")