# 1. Create class or find another way to store data
# 2. Read data into class array or use another way to store data
# 3. Validate data (Check if time is not 0)
# 4. Find the minimum time
# 5. Find days with minimum time
# 6. Write results to file

class Running:
    def __init__(self, day, time):
        self.day = day
        self.time = time


def calculate_time(sh, sm, eh, em):
    return (eh * 60 + em) - (sh * 60 + sm)


with open("U1.txt", "r") as f:
    n = int(f.readline())
    runs = []

    for _ in range(n):
        day, msh, msm, meh, mem, esh, esm, eeh, eem = map(int, f.readline().split())
        t1 = calculate_time(msh, msm, meh, mem)
        t2 = calculate_time(esh, esm, eeh, eem)

        if t1 != 0 and t2 != 0:
            run = Running(day, t1 + t2)
            runs.append(run)

min_time = runs[0].time
for run in runs:
    if run.time < min_time:
        min_time = run.time

with open("U1rez.txt", "w") as f:
    f.write(f"Minimalus laikas\n")
    f.write(f"{min_time}\n")
    f.write(f"Dienos\n")
    found = False
    for run in runs:
        if run.time == min_time:
            if found:
                f.write(" ")
            f.write(f"{run.day}")
            found = True
