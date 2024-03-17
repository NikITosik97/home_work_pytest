def get_unique_name_mentors(list_mentors: list[list[str]]) -> str:
    all_: set = set()
    for lst_mentors in list_mentors:
        for name_mentor in lst_mentors:
            all_.add(name_mentor.split()[0])

    try:
        assert type(all_) == set
    except AssertionError:
        return 'Error: Имена повторяются!'
    return f'Уникальные имена преподавателей: {", ".join(sorted(all_))}'
