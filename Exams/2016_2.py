class exercise:
    def __init__(self, name, repeats):
        self.name = name
        self.repeats = repeats


def sort_exercises(exercises):
    for i in range(len(exercises)):
        for j in range(i + 1, len(exercises)):
            if (exercises[i].repeats < exercises[j].repeats or
                    (exercises[i].repeats == exercises[j].repeats and
                     exercises[i].name > exercises[j].name)):
                exercises[i], exercises[j] = exercises[j], exercises[i]


with open('U2.txt', 'r') as f:
    exercise_count = int(f.readline())
    exercises = []
    for _ in range(exercise_count):
        line = f.readline().strip()
        #name = line[:20]
        #repeats = int(line[20:])
        name, repeats = line.split()
        repeats = int(repeats)

        already_exists = False
        for i in range(len(exercises)):
            if exercises[i].name == name:
                already_exists = True
                exercises[i].repeats += repeats
                break

        if not already_exists:
            new_exercise = exercise(name, repeats)
            exercises.append(new_exercise)

sort_exercises(exercises)
with open('U2rez.txt', 'w') as f:
    for ex in exercises:
        f.write(f"{ex.name:<20} {ex.repeats}\n")