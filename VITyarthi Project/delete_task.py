from view_tasks import view_tasks


def delete_task(task_names, task_subjects, task_priorities,
                task_deadlines, task_status):

    view_tasks(task_names, task_subjects, task_priorities,
               task_deadlines, task_status)

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