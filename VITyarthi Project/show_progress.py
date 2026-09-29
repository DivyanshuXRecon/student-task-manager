def show_progress(task_names, task_status):

    total = len(task_names)

    if total == 0:
        print("No tasks added yet")
    else:
        completed = 0

        for i in range(len(task_status)):
            if task_status[i] == "Completed":
                completed = completed + 1

        pending = total - completed
        progress = (completed / total) * 100

        print("Total Tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)
        print("Progress:", progress, "%")