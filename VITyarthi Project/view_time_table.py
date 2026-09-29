def view_study_time(study_subjects, study_hours):

    if len(study_subjects) == 0:
        print("No study time recorded")
    else:
        total = 0

        for i in range(len(study_subjects)):
            print(study_subjects[i], "-", study_hours[i], "hours")
            total = total + study_hours[i]

        print("Total study time:", total, "hours")