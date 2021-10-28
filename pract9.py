"""
author gauresh
date 29/10/2021
perpose: practical 9 funny names printing
actually itis swapping names but its look like funny

Problem Statement:-
It's result day at school and not everyone is happy.
You decided to make your friends laugh by jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated
 by space as input. Output should be funny names in the same order.

Input:
Enter number of friends:

3

Enter the name of your 3 friends:

Rohan Das

Shubham Agarwal

Ritesh Arora

Output:
Ritesh Das

Shubham Arora

Rohan Agarwal
"""
import random

def altername(students):
    mylist=[]
    for i in range(0,students):
        #print(i)
        names=input("enter name")
        mylist.append(names)
    return mylist
def funny names():
    wrong = random.randint(1, 9)
    # print(wrong)
    tabel = [i * number for i in range(1, 11)]
    # print(tabel[wrong])
    tabel[wrong] = tabel[wrong] + random.randint(1, 8)
    #


if __name__ == "__main__":
    students= int(input("Enter number of student name you want to add\n"))
    altere=altername(students)
    print(altere)

