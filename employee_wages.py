"""
Author :- Sunanda Shil
Date :- 16-12-21
"""

import random
import logging

logging.basicConfig(filename="employe_wages.log", filemode="w")


class Employee:
    """
    created this class for employee
    """
    is_full_day = 1
    is_part_day = 2
    working_hr = 0

    def __init__(self, name, wages_per_hour, company_working_hr, employee_working_hr, working_for_month):
        """
        Initializing the attribute
        :param name:
        :param wages_per_hour:
        :param company_working_hr:
        :param employee_working_hr:
        """
        self.name = name
        self.wages_per_hour = wages_per_hour
        self.company_working_hr = company_working_hr
        self.employee_working_hr = employee_working_hr
        self.working_for_month = working_for_month

    def check_attendence(self):
        """
        finding the employee attandence randomly
        :return:
        """
        absent = 0
        is_full_time = 1
        is_part_time = 2
        dictionary = {
            0: absent,
            1: is_full_time,
            2: is_part_time
        }
        empcheck = random.randint(0, 2)
        attendence_employee = dictionary.get(empcheck)
        return attendence_employee

    def attendence(self):
        """
        checkoing the attandence and finding the working hours of employee
        :return:
        """
        attendence_emp = self.check_attendence()
        try:
            if attendence_emp == self.is_full_day:
                self.working_hr = 8
            elif attendence_emp == self.is_part_day:
                self.working_hr = 4
            else:
                self.working_hr = 0
            return self.working_hr
        except Exception:
            logging.exception("Given range is not proper")

    def calculate_daily_wage(self):
        """
        In this Method calculation process is running
        :return:
        """
        total_wages = 0
        day_working_hr = self.attendence()
        while self.employee_working_hr < self.company_working_hr:
            value = self.wages_per_hour * day_working_hr * self.working_for_month
            total_wages = total_wages + value
            return total_wages


class Company:
    """
    Created this class for company
    """
    totalwages_by_company = 0

    def __init__(self, name):
        """
        Initialize the attribute
        :param name:
        """
        self.employee_list = list()
        self.name = name

    def add_employee(self, employee):
        """
        adding the employee in employee list
        :param employee:
        :return:
        """
        try:
            self.employee_list.append(employee)
        except Exception:
            logging.exception("Enter integer value")

    def display(self):
        """
        Created this method for display the wages and details
        :return:
        """
        print("Company name is :- ", company.name)
        for employee in self.employee_list:
            print("Employee name is :- ", employee.name)
            print("Wages per hour is :- ", employee.wages_per_hour)
            print("Company Working hour:- ", employee.company_working_hr)
            print("Employee working hour:- ", employee.employee_working_hr)
            print("Working days:- ", employee.working_for_month)

    def Total_Wages(self):
        """
        calling calculate wages in company class
        :return:
        """
        for employee in self.employee_list:
            self.totalwages_by_company = self.totalwages_by_company + employee.calculate_daily_wage()

        print(self.totalwages_by_company)


def get_company(company_list, company_name):
    """
    checking the company exist or not
    :param company_list:
    :param company_name:
    :return:
    """
    for company in company_list:
        if company.name == company_name:
            return company_list, company
    c1 = Company(company_name)
    company_list.append(c1)
    return company_list, c1


if __name__ == "__main__":
    """
    Executing the program with user choice"""
    company_list = []

    try:
        while True:

            print("""Your choices:- 
                        1.Add employee
                        2.Display
                        3.Total wages"""
                  )
            choice = int(input("Enter your choice:-"))

            if choice == 1:
                c3 = input("Enter company name:- ")
                list_of_company, company = get_company(company_list, c3)

                name = input("Enter employee name:- ")
                wages_per_hour = int(input("Enter the wages per hour given by company:- "))
                company_working_hr = int(input("Enter the company working hour:- "))
                employee_working_hr = int(input("Enter the employee working  hour in company"))
                working_for_month = int(input("Enter working days:- "))
                employee = Employee(name, wages_per_hour, company_working_hr, employee_working_hr, working_for_month)

                company.add_employee(employee)

            elif choice == 2:
                c3 = input("Enter company name:- ")
                list_of_company, company = get_company(company_list, c3)
                print(company.display())
            elif choice == 3:
                c3 = input("Enter company name:- ")
                list_of_company, company = get_company(company_list, c3)
                print(company.Total_Wages())
            else:
                print("Enter proper choice!!!")
                break
    except Exception:
        logging.exception("Type integer value")
