def add_study_time(study_subjects, study_hours):

    subject = input("Enter subject: ")
    hours = input("Enter hours studied (whole number): ")

    if hours.isdigit():
        study_subjects.append(subject)
        study_hours.append(int(hours))

        print("Study time added")
    else:
        print("Please enter a valid number")