from add_task import add_task
from view_tasks import view_tasks
from complete_task import complete_task
from delete_task import delete_task
from add_class import add_class
from view_timetable import view_timetable
from add_study_time import add_study_time
from view_time_table import view_study_time
from show_progress import show_progress
from show_dashboard import show_dashboard


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

        add_task(
            task_names,
            task_subjects,
            task_priorities,
            task_deadlines,
            task_status
        )


    elif choice == "2":

        view_tasks(
            task_names,
            task_subjects,
            task_priorities,
            task_deadlines,
            task_status
        )


    elif choice == "3":

        complete_task(
            task_names,
            task_subjects,
            task_priorities,
            task_deadlines,
            task_status
        )


    elif choice == "4":

        delete_task(
            task_names,
            task_subjects,
            task_priorities,
            task_deadlines,
            task_status
        )


    elif choice == "5":

        add_class(
            timetable_days,
            timetable_subjects
        )


    elif choice == "6":

        view_timetable(
            timetable_days,
            timetable_subjects
        )


    elif choice == "7":

        add_study_time(
            study_subjects,
            study_hours
        )


    elif choice == "8":

        view_study_time(
            study_subjects,
            study_hours
        )


    elif choice == "9":

        show_progress(
            task_names,
            task_status
        )


    elif choice == "10":

        show_dashboard(
            student_name,
            task_names,
            task_priorities,
            task_status
        )


    elif choice == "11":

        print("Thank you for using Student Task Manager")
        break


    else:

        print("Invalid choice, please try again")