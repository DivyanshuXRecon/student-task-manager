def view_timetable(timetable_days, timetable_subjects):

    if len(timetable_days) == 0:
        print("Timetable is empty")
    else:
        for i in range(len(timetable_days)):
            print(timetable_days[i], "-", timetable_subjects[i])