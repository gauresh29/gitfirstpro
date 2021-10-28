import inspect
class Employee:
    def __init__(self,fname):
        self.fname=fname

    def objectinsector(self):

        for item in inspect.classify_class_attrs(Employee):
            print(item[0])


theobject=Employee("gauresh")
theobject.objectinsector()
