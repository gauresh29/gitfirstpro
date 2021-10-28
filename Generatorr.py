def seqq(n):
    for i in range(n):
        yield i

seq= seqq(2)
print(seq.__next__())
print(seq.__next__())
#print(seq.__next__())#stop iteration

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

hello=123456
hello1=iter(hello)
print(hello1.__next__())