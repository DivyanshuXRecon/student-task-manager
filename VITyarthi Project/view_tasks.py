def view_tasks(task_names, task_subjects, task_priorities,
               task_deadlines, task_status):

    if len(task_names) == 0:
        print("No tasks found")
    else:
        for i in range(len(task_names)):
            print(str(i + 1) + ". " + task_names[i])
            print("   Subject:", task_subjects[i])
            print("   Priority:", task_priorities[i])
            print("   Deadline:", task_deadlines[i])
            print("   Status:", task_status[i])