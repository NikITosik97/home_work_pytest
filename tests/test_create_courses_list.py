from main import create_courses_list
from courses import courses
from mentors import mentors
import pytest


class TestCreateCoursesList:
    def test_not_empty_list(self):
        assert len(courses) >= 1

    def test_return_result(self):
        result = create_courses_list(courses, mentors)
        assert type(result) == str

    def test_type_value_in_courses_list(self):
        for course in courses:
            assert type(course) == str


