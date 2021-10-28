class A:
    classvar1="a is student studing in class A"
    def __init__(self):
        self.var1="i am in class A"
        self.subjects="we have sankrit optional"
        self.team="cricket"

class B(A):
    classvar1 = "b is students studing in class B"
    def __init__(self):
        self.var1 = "i am in class B"
        self.subjects = "we have hindi mandatory"
        super().__init__()


astd=A()
bstd=B()

print(bstd.team,bstd.var1,bstd.subjects)