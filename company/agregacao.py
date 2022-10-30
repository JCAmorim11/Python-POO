class Salary:
    def __init__(self, pay,bonus):
        self.pay=pay
        self.bonus = bonus

    def anual_salary(self):
        return (self.pay*12)+ self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age=age
        #Ato de agregação
        self.obj_salary=salary

    def total_salary(self):
        return self.obj_salary.anual_salary()


sal = Salary(15000, 10000)
emp = Employee('maddie', 25, sal)
print(emp.total_salary())
