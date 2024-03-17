from courses import courses
from mentors import mentors

from get_unique_name_mentors import get_unique_name_mentors
from create_courses_list import create_courses_list
from namesake_on_courses import namesake_on_courses
from create_folder_yandex_disc import CreateFolderYandexDisc

if __name__ == '__main__':
    print(get_unique_name_mentors(mentors))
    print()
    print(create_courses_list(courses, mentors))
    print()
    print(namesake_on_courses(courses, mentors))
    print()
    create_folder = CreateFolderYandexDisc()
    create_folder.create_folder()
