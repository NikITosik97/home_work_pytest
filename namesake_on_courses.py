def namesake_on_courses(course_list: list[str], mentors_list: list[list[str]]) -> str:
    durations = [14, 20, 12, 20]
    result_list = []

    courses_list = []
    for course, mentor, duration in zip(course_list, mentors_list, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    for cours in courses_list:
        all_name_list = [i.split(' ')[0] for i in cours['mentors']]
        unique_names = set(all_name_list)
        same_name_list = []
        for set_name in unique_names:
            if all_name_list.count(set_name) > 1:
                for fio in cours['mentors']:
                    if set_name in fio:
                        same_name_list.append(fio)
        if same_name_list:
            result_list.append(f'На курсе {cours["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')

    return f'{result_list[0]},\n{result_list[1]},\n{result_list[2]},\n{result_list[3]}\n'
