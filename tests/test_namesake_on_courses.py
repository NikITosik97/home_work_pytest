from main import namesake_on_courses
from courses import courses
from mentors import mentors
from tests.conftests import len_mentors
import pytest


class TestNamesakeOnCourses:
    def test_return_result(self):
        result = namesake_on_courses(courses, mentors)
        assert type(result) == str

    def test_not_empty_courses_list(self):
        assert len(courses) >= 1

    def test_not_empty_mentors_list(self):
        assert len_mentors() >= 1

    def test_not_empty_mentors_list_in_list(self):
        for count in range(len_mentors()):
            assert len(mentors[count]) >= 1

    def test_type_value_list_on_list_in_mentors(self):
        for count in range(len_mentors()):
            for name_mentor in mentors[count]:
                assert type(name_mentor) == str

