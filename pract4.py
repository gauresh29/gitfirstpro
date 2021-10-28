"""Python Problem 4 | Python Tutorials For Absolute Beginners In Hindi #109
The task you have to perform is “The Next Palindrome.” This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be the number of test cases and then take all the cases as input from the user.



Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222

"""
def nextpallendrom(num):

    print(num)
    while not ispallendrom(num) :
        num += 1
    return num


def ispallendrom(num):
    return str(num) == str(num)[::-1]
    #print("already ")
if __name__ == "__main__":
    num=int(input("How many numbers you want to enter"))
    mylist=[]
    for i in range(num):
         pnum=int(input("enetr number\n"))
         mylist.append(pnum)

    for i in range(num):
        print(f"you enter {mylist[i]} and next pallendrom {nextpallendrom(mylist[i])}")

