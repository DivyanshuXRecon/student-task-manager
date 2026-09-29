def add_class(timetable_days, timetable_subjects):

    day = input("Enter day (Monday, Tuesday, etc.): ")
    subject = input("Enter subject: ")

    timetable_days.append(day)
    timetable_subjects.append(subject)

    print("Class added to timetable")