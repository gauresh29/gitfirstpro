"""
Practice Problem 2 (Easy) | Python Tutorials For Absolute Beginners In Hindi #105
The task you have to perform is “Divide the Apples.” This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
Harry Potter has got the “n” number of apples.
 Harry has some students among whom he wants to distribute the apples.
 These “n” number of apples is provided to harry by his friends, and
 he can request for few more or a few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.




Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisors of “n” or not.
If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20

Have you solved this task? If yes, then it is time to check your solution. The solution is discussed in tutorial#106.


"""
#print(6%4)
try:
    n=int(input("enter apple no"))
    mn=int(input("enetr mn"))
    mx=int(input("eneter mx"))
    for i in range(mn, mx+1):
         if n%i == 0:
            print(f"{i}is divisble")
         else:
             print(f"{i}is not divisible")
except Exception as e:
    print("enter integer only")
