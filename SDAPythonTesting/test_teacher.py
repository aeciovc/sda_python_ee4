from teacher import Teacher


def test_create_teacher_with_optinal_args():

    # input
    name = 'James'
    years_of_experience = 4
    master_degree = True
    topics = ['Python Tech', 'Data structure']

    # process
    teacher = Teacher(name, years_of_experience, master_degree=master_degree, topics=topics)

    # assert
    assert isinstance(teacher, Teacher)
    assert teacher.name == 'James'
    assert teacher.years_of_experience == 4
    assert teacher.has_master_degree is True
    assert teacher.topics == ['Python Tech', 'Data structure']
    assert teacher.amount_topics == 2

def test_create_teacher_with_defaults():

    # input
    name = 'Julia'
    years_of_experience = 2

    # process
    teacher = Teacher(name, years_of_experience)

    # assert
    assert isinstance(teacher, Teacher)
    assert teacher.name == 'Julia'
    assert teacher.years_of_experience == 2
    assert teacher.has_master_degree is False
    assert teacher.topics == []
