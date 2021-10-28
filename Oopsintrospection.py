class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
       # self.email=f"{self.fname}.{self.lname}@gn.com"

    def explain(self):
        return f"this employee {self.fname} {self.lname}"

    @property
    def email(self):

        if self.fname != None or self.lname != None:
            print("email is not set please set with setter")

        return f" {self.fname}{self.lname}@gn.com"

    @email.setter
    def email(self, string):
        print("this is executting")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

newemail=Employee("gauresh","shirodkar")
newemail1=Employee("gauresh","shirodkar")
print(id(newemail))
print(dir(newemail1))
skillf="this is string"
import inspect
print(inspect.getmembers(newemail))
print(inspect.getclasstree(newemail))