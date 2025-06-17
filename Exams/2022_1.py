class Participant:
    def __init__(self, name, solution_times):
        self.name = name
        self.solution_times = solution_times
        self.points = 0
        self.total_time = 0
        self.solved_tasks = 0


def calculate_participant_data(participant, task_time_limits, task_max_points):
    participant.total_time = sum(participant.solution_times)

    for i, time in enumerate(participant.solution_times):
        if time == 0:
            continue

        participant.solved_tasks += 1
        if time <= task_time_limits[i]:
            participant.points += task_max_points[i]
        else:
            participant.points += task_max_points[i] // 2


def sort_by_solved_desc_then_by_time_acsc(participants):
    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            if participants[i].solved_tasks < participants[j].solved_tasks:
                participants[i], participants[j] = participants[j], participants[i]


with open("U1.txt", "r") as fin:
    task_count = int(fin.readline())
    task_time_limits = list(map(int, fin.readline().split()))
    task_max_points = list(map(int, fin.readline().split()))
    max_points = 0

    participants = []
    for line in fin:
        name = line[:10]
        solution_times = list(map(int, line[10:].split()))
        participant = Participant(name, solution_times)
        calculate_participant_data(participant, task_time_limits, task_max_points)
        participants.append(participant)
        max_points = max(max_points, participant.points)

sort_by_solved_desc_then_by_time_acsc(participants)

with open("U1rez.txt", "w") as fout:
    fout.write(f"{max_points}\n")
    for participant in participants:
        if participant.points == max_points:
            fout.write(f"{participant.name} {participant.solved_tasks} {participant.total_time}\n")
