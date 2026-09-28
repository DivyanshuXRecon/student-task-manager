# STUDENT TASK MANAGER

# ----- LISTS TO STORE TASK DATA -----
task_names = []
task_subjects = []
task_priorities = []
task_deadlines = []
task_status = []

# ----- LISTS TO STORE TIMETABLE DATA -----
timetable_days = []
timetable_subjects = []

# ----- LISTS TO STORE STUDY TIME DATA -----
study_subjects = []
study_hours = []


def add_task():
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


def view_tasks():
    if len(task_names) == 0:
        print("No tasks found")
    else:
        for i in range(len(task_names)):
            print(str(i + 1) + ". " + task_names[i])
            print("   Subject:", task_subjects[i])
            print("   Priority:", task_priorities[i])
            print("   Deadline:", task_deadlines[i])
            print("   Status:", task_status[i])


def complete_task():
    view_tasks()
    num = input("Enter task number to mark completed: ")

    if num.isdigit():
        num = int(num)
        if num >= 1 and num <= len(task_names):
            task_status[num - 1] = "Completed"
            print("Task marked as completed")
        else:
            print("Invalid task number")
    else:
        print("Please enter a valid number")


def delete_task():
    view_tasks()
    num = input("Enter task number to delete: ")

    if num.isdigit():
        num = int(num)
        if num >= 1 and num <= len(task_names):
            task_names.pop(num - 1)
            task_subjects.pop(num - 1)
            task_priorities.pop(num - 1)
            task_deadlines.pop(num - 1)
            task_status.pop(num - 1)
            print("Task deleted")
        else:
            print("Invalid task number")
    else:
        print("Please enter a valid number")


def add_class():
    day = input("Enter day (Monday, Tuesday, etc.): ")
    subject = input("Enter subject: ")
    timetable_days.append(day)
    timetable_subjects.append(subject)
    print("Class added to timetable")


def view_timetable():
    if len(timetable_days) == 0:
        print("Timetable is empty")
    else:
        for i in range(len(timetable_days)):
            print(timetable_days[i], "-", timetable_subjects[i])


def add_study_time():
    subject = input("Enter subject: ")
    hours = input("Enter hours studied (whole number): ")

    if hours.isdigit():
        study_subjects.append(subject)
        study_hours.append(int(hours))
        print("Study time added")
    else:
        print("Please enter a valid number")


def view_study_time():
    if len(study_subjects) == 0:
        print("No study time recorded")
    else:
        total = 0
        for i in range(len(study_subjects)):
            print(study_subjects[i], "-", study_hours[i], "hours")
            total = total + study_hours[i]
        print("Total study time:", total, "hours")


def show_progress():
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


def show_dashboard():
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


# ----- MAIN PROGRAM STARTS HERE -----

student_name = input("Enter your name: ")

while True:
    print()
    print("===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Add Class to Timetable")
    print("6. View Timetable")
    print("7. Add Study Time")
    print("8. View Study Time")
    print("9. Show Progress")
    print("10. Show Dashboard")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        add_class()
    elif choice == "6":
        view_timetable()
    elif choice == "7":
        add_study_time()
    elif choice == "8":
        view_study_time()
    elif choice == "9":
        show_progress()
    elif choice == "10":
        show_dashboard()
    elif choice == "11":
        print("Thank you for using Student Task Manager")
        break
    else:
        print("Invalid choice, please try again")
