from employee_wages import Employee
from employee_wages import Company


def test_check_attendence():
    """
    testing the check attandence function
    :return:
    """
    e1 = Employee("sunanda", 20, 14, 10, 5)
    assert (e1.check_attendence() == 2 or e1.check_attendence() == 1 or e1.check_attendence() == 0)


def test_attendence():
    """
    testing the attandence function
    :return:
    """
    e2 = Employee("sunanda", 20, 14, 10,10)
    assert isinstance(e2, Employee) == True


def test_calculate_wages():
    """
    testing the calculate wages function
    :return:
    """
    e3 = Employee("Sunanda", 20, 14, 10, 5)
    assert (e3.check_attendence() == 2 or e3.check_attendence() == 1 or e3.check_attendence() == 0)


def test_inserting_employee():
    """
    testing the inserting employee function
    :return:
    """
    c1 = Company("Dmart")
    e3 = Employee("Sunanda", 20, 14, 10, 5)
    c1.add_employee(e3)
    assert len(c1.employee_list) > 0


def test_get_company():
    c1 = Company("Dmart")
    assert isinstance(c1,Company) == True
