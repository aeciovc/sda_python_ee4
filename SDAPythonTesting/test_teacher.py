import pytest

from teacher import Teacher


@pytest.fixture()
def valid_person_name():
    yield 'James'
    print("Cleaning the environment")


@pytest.fixture()
def invalid_person_name():
    return ''


class TestCreateDirector:

    @pytest.mark.skip(reason="still not implemented")
    def test_create_director_with_wrong_position(self):
        pass


class TestCreateTeacher:

    def test_create_teacher_with_optinal_args(self, valid_person_name):

        # input
        years_of_experience = 4
        master_degree = True
        topics = ['Python Tech', 'Data structure']

        # process
        teacher = Teacher(valid_person_name, years_of_experience, master_degree=master_degree, topics=topics)

        # assert
        assert isinstance(teacher, Teacher)
        assert teacher.name == 'James'
        assert teacher.years_of_experience == 4
        assert teacher.has_master_degree is True
        assert teacher.topics == ['Python Tech', 'Data structure']
        assert teacher.amount_topics == 2

    def test_create_teacher_with_defaults(self, valid_person_name):

        # input
        years_of_experience = 2

        # process
        teacher = Teacher(valid_person_name, years_of_experience)

        # assert
        assert isinstance(teacher, Teacher)
        assert teacher.name == valid_person_name
        assert teacher.years_of_experience == 2
        assert teacher.has_master_degree is False
        assert teacher.topics == []

    def test_create_teacher_with_invalid_name(self, invalid_person_name):
        pass
