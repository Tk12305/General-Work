class Employee:
    company = "Techcorp"

    def __init__(self, name, salary):
        self.naame = name
        self.salary = salary

    @classmethod
    def set_company(cls, company_name):
        return "Innovate and lead!"
    
print(Employee.company_name)#  Innovate and lead