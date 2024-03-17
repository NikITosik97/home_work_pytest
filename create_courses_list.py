def create_courses_list(list_courses: list, mentors_list: list[list[str]]) -> str:
    durations = [14, 20, 12, 20]

    courses_list = [{'title': title,
                     'duration': duration,
                     'mentors': mentor} for title, duration, mentor in zip(list_courses, durations, mentors_list)]

    duration_min = min(durations)
    duration_max = max(durations)

    index_duration_min = []
    index_duration_max = []

    for ind, val in enumerate(durations):
        if val == duration_min:
            index_duration_min.append(ind)
        elif val == duration_max:
            index_duration_max.append(ind)

    course_name_min = []
    course_name_max = []

    for course_list in courses_list:
        if course_list['duration'] == duration_min:
            course_name_min.append(course_list['title'])
        elif course_list['duration'] == duration_max:
            course_name_max.append(course_list['title'])

    return (f'Самый короткий курс(ы): {"".join(course_name_min)} - {duration_min} месяца(ев)\n'
            f'Самый длинный курс(ы): {"".join(course_name_max[0])}, {"".join(course_name_max[1])} - {duration_max} месяца(ев)')
