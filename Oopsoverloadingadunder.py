class Employee:
    no_of_leaves=3
    def  __init__(self,ename,esalary,erole):
        self.name=ename
        self.salary=esalary
        self.role=erole

    def printdetails(self):

        return f"the name is{self.name}.salary is {self.salary}.role is{self.role}"

    @classmethod
    def __repr__(self):
        return f"hello"

    def __str__(self):
        return f"bollo"

    def __add__(self, other):
        return self.salary+other.salary
    def __truediv__(self, other):
        return self.salary/other.salary

a= Employee("gauresh",222,"student")
b=Employee("gauresh",222,"student")
print(repr(a))
