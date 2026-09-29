from view_tasks import view_tasks


def complete_task(task_names, task_subjects, task_priorities,
                  task_deadlines, task_status):

    view_tasks(task_names, task_subjects, task_priorities,
               task_deadlines, task_status)

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