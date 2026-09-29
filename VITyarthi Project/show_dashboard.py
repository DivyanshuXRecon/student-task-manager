def show_dashboard(student_name, task_names,
                   task_priorities, task_status):

    print("Student:", student_name)
    print()

    total = len(task_names)

    completed = 0

    for i in range(len(task_status)):
        if task_status[i] == "Completed":
            completed = completed + 1

    pending = total - completed

    if total == 0:
        progress = 0
    else:
        progress = (completed / total) * 100

    high_count = 0

    for i in range(len(task_priorities)):
        if task_priorities[i] == "High" and task_status[i] == "Pending":
            high_count = high_count + 1

    print("Total Tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)
    print("Progress:", progress, "%")
    print("High Priority Tasks:", high_count)