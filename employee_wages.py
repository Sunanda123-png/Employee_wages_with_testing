import random
import logging

logging.basicConfig(filename="employe_wages.log", filemode="w")


class Employee:
    is_full_day = 1
    is_part_day = 2
    working_hr = 0

    def __init__(self, name, wages_per_hour, company_working_hr, employee_working_hr):
        self.name = name
        self.wages_per_hour = wages_per_hour
        self.company_working_hr = company_working_hr
        self.employee_working_hr = employee_working_hr

    def check_attendence(self):
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
        total_wages = 0
        day_working_hr = self.attendence()
        while self.employee_working_hr < self.company_working_hr:
            value = self.wages_per_hour * day_working_hr
            total_wages = total_wages + value
            return total_wages


if __name__ == "__main__":
    st = Employee("Sunanda", 20, 14, 10)
    print(st.name)
    print(st.calculate_daily_wage())


