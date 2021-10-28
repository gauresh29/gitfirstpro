#ap = open("ooo.txt")
try:
    op=open("ooo.txt")
except Exception as e:
    print("this is ", e)
else:
    print("exception occure yahoooo")

finally:
    print("this is running")
    op.close()
