class A:
    var1="this is from A"
class B(A):
    var1="this is from B"
class C(A):
    var1="this is from C"
class D(C,B):
    var1="this is from own class"
a=A()
b=B()
c=C()
d=D()

print(d.var1)