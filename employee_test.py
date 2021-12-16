from employee_wages import Employee


def test_check_attendence():
    """
    testing the check attandence function
    :return:
    """
    e1 = Employee("sunanda", 20, 14, 10)
    assert e1.check_attendence() == 2


def test_attendence():
    """
    testing the attandence function
    :return:
    """
    e2 = Employee("sunanda", 20, 14, 10)
    assert e2.attendence() == 0


def test_calculate_wages():
    """
    testing the calculate wages function
    :return:
    """
    e3 = Employee("sunanda", 20, 14, 10)
    assert e3.calculate_daily_wage() == 0
