def add_task(task_names, task_subjects, task_priorities,
             task_deadlines, task_status):

    name = input("Enter task name: ")
    subject = input("Enter subject: ")

    print("Select priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Enter choice: ")

    if choice == "1":
        priority = "High"
    elif choice == "2":
        priority = "Medium"
    elif choice == "3":
        priority = "Low"
    else:
        priority = "Medium"

    deadline = input("Enter deadline: ")

    task_names.append(name)
    task_subjects.append(subject)
    task_priorities.append(priority)
    task_deadlines.append(deadline)
    task_status.append("Pending")

    print("Task added successfully")