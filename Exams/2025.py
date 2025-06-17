class Student:
    def __init__(self, name, pil, soc, kul, spo, eko, dar, kit):
        self.name = name
        self.pil = pil
        self.soc = soc
        self.kul = kul
        self.spo = spo
        self.eko = eko
        self.dar = dar
        self.kit = kit
        self.total_hours = pil + soc + kul + spo + eko + dar + kit


class SocialActivity:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.hour_percentage = 0


def sort_activities_by_percentage_desc(activities):
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            if activities[i].hour_percentage < activities[j].hour_percentage:
                activities[i], activities[j] = activities[j], activities[i]


def sort_students_by_names(students):
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[i].name > students[j].name:
                students[i], students[j] = students[j], students[i]


with open("Duomenys.txt", "r") as file:
    n = int(file.readline())
    students = []
    social_activities = []
    total_hours = 0
    for _ in range(n):
        student_name, amount = file.readline().split()
        amount = int(amount)
        pil, soc, kul, spo, eko, dar, kit = 0, 0, 0, 0, 0, 0, 0
        for __ in range(amount):
            values = file.readline().split()
            subject = values[0]
            hours = sum(map(int, values[2:]))
            if subject == "Pil.":
                pil += hours
            elif subject == "Soc.":
                soc += hours
            elif subject == "Kul.":
                kul += hours
            elif subject == "Spo.":
                spo += hours
            elif subject == "Eko.":
                eko += hours
            elif subject == "Dar.":
                dar += hours
            elif subject == "Kit.":
                kit += hours

            total_hours += hours

            for activity in social_activities:
                if activity.name == subject:
                    activity.hours += hours
                    break
            else:
                social_activity = SocialActivity(subject, hours)
                social_activities.append(social_activity)

        student = Student(student_name, pil, soc, kul, spo, eko, dar, kit)
        students.append(student)

for activity in social_activities:
    activity.hour_percentage = (activity.hours / total_hours) * 100

sort_activities_by_percentage_desc(social_activities)
sort_students_by_names(students)

with open("Rezultatai.txt", "w") as file:
    file.write("Statistika\n")
    for activity in social_activities:
        file.write(f"{activity.name} {activity.hour_percentage:.2f} %\n")

    file.write("Mokiniai\n")
    for student in students:
        if student.total_hours >= 20:
            file.write(f"{student.name} {student.total_hours}\n")