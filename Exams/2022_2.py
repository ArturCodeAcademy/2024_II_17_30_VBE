class Student:
    def __init__(self, name, subject, average):
        self.name = name
        self.subject = subject
        self.average = average

    def __str__(self):
        return f"{self.name} {self.subject} {self.average:.2f}"


class Subject:
    def __init__(self, name):
        self.name = name
        self.students = []


def sort_subjects(subjects):
    for i in range(len(subjects) - 1):
        for j in range(i + 1, len(subjects)):
            if len(subjects[j].students) > len(subjects[i].students):
                subjects[i], subjects[j] = subjects[j], subjects[i]
            elif len(subjects[j].students) == len(subjects[i].students):
                if subjects[j].name < subjects[i].name:
                    subjects[i], subjects[j] = subjects[j], subjects[i]


with open("U2.txt", "r") as fin:
    n = int(fin.readline())
    students = []
    subjects = []
    for _ in range(n):
        values = fin.readline().split()
        name = values[0]
        subject = values[1]
        count = int(values[2])
        marks = list(map(int, values[3:]))
        average = sum(marks) / count
        student = Student(name, subject, average)

        found = False
        for subject in subjects:
            if subject.name == student.subject:
                found = True
                if student.average >= 9:
                    subject.students.append(student)
                break
        if not found and student.average >= 9:
            new_subject = Subject(student.subject)
            new_subject.students.append(student)
            subjects.append(new_subject)

sort_subjects(subjects)
with open("U2rez.txt", "w") as fout:
    if not subjects:
        print("Neatitinka vidurkis")
    else:
        for subject in subjects:
            fout.write(f"{subject.name} {len(subject.students)}\n")
            for student in subject.students:
                fout.write(student.name)
                fout.write("\n")