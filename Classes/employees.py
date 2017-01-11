class Employee(object):
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date
        self.employees = set()

    def get_name(self):
        """Returns the name of the company"""

        return self.name

    # Add the remaining methods to fill the requirements above

    def __repr__(self):
        employee_list = ''
        for employee in self.employees:
            employee_list += employee.name + ', '
        return ('%s, the %s, founded on %s employs %s' % (repr(self.name), repr(self.title), repr(self.start_date), repr(employee_list)))

ThisCo = Company('ThisCo', 'Company of zees', 'apr 1 2017')

me = Employee('Billing', 'Billing', 'apr 1 2017')
you = Employee('Shipping', 'Shipping', 'apr 1 2017')
we = Employee('Accounting', 'Accounting', 'apr 1 2017')

ThisCo.employees.add(me)
ThisCo.employees.add(you)
ThisCo.employees.add(we)

print(ThisCo)