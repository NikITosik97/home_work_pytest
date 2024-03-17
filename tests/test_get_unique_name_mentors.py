from tests.conftests import len_mentors
from main import get_unique_name_mentors
from mentors import mentors
import pytest


class TestGetUniqueNameMentors:
    def test_return_result(self):
        result = get_unique_name_mentors(mentors)
        assert type(result) == str

    def test_not_empty_mentors_list(self):
        assert len_mentors() >= 1

    def test_not_empty_mentors_list_in_list(self):
        for i in range(len_mentors()):
            assert len(mentors[i]) >= 1

    def test_type_value_list_on_list_in_mentors(self):
        for count in range(len_mentors()):
            for name_mentor in mentors[count]:
                assert type(name_mentor) == str

    def test_type_arguments(self):
        assert type(mentors) == list

    def test_type_arguments2(self):
        for mentor_list in mentors:
            assert type(mentor_list) == list


@pytest.mark.parametrize('exception, expected_error', [(TypeError, int),
                                                       (TypeError, tuple),
                                                       (TypeError, dict),
                                                       (TypeError, float),
                                                       (TypeError, set),
                                                       (TypeError, str)])
def test_unique_name_arguments(exception, expected_error):
    with pytest.raises(exception):
        get_unique_name_mentors(expected_error)
