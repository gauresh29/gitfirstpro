a, b= map(int, input("Enter two number").split())
op = input("enter operator")
match op:
    case "+":
        print(a+b)
    case "-":
        print(a - b)
    case _:print("operator not found")
