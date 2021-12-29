from employee_wages import Employee
from employee_wages import Company


def test_check_attendence():
    """
    testing the check attandence function
    :return:
    """
    employee = Employee("sunanda", 20, 14, 10, 5)
    assert (employee.check_attendence() == 2 or employee.check_attendence() == 1 or employee.check_attendence() == 0)


def test_attendence():
    """
    testing the attandence function
    """
    employee = Employee("sunanda", 20, 14, 10,10)
    assert isinstance(employee, Employee) == True


def test_calculate_wages():
    """
    testing the calculate wages function
    """
    employee = Employee("Sunanda", 20, 14, 10, 5)
    assert (employee.check_attendence() == 2 or employee.check_attendence() == 1 or employee.check_attendence() == 0)


def test_inserting_employee():
    """
    testing the inserting employee function
    """
    company = Company("Dmart")
    employee = Employee("Sunanda", 20, 14, 10, 5)
    company.add_employee(employee)
    assert len(company.employee_list) > 0


def test_get_company():
    company = Company("Dmart")
    assert isinstance(company,Company) == True
