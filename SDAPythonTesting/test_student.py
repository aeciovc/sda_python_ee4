from student import Student


def test_when_student_is_not_approved():
    # input
    name = 'Paul'
    age = 23
    grade = 6

    # process
    student = Student(name, age, grade=grade)

    # assert
    student.is_approved() is False


def test_when_grade_is_not_in_range():
    # input
    name = 'Paul'
    age = 43
    grade = 12

    # processing
    student = Student(name, age, grade=grade)

    # assert
    assert isinstance(student, Student)
    assert student.name == name
    assert student.age == age
    assert student.grade is None


def test_instantiating_student_sucess():
    # input
    name = 'Jaan'
    age = 33

    # process
    student = Student(name, age, grade=8)

    # assert
    assert isinstance(student, Student)
    assert student.name == 'Jaan'
    assert student.age == 33
    assert student.grade == 8
