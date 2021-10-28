"""
Python Problem 6 | Python Tutorials For Absolute Beginners In Hindi #113
The task you have to perform is “Guess The number”. This task consists of a total of 10 points to evaluate your performance.

 Problem Statement:-
Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.



Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

Wrong guess a smaller number again

6

Correct, you took 3 trials to guess the number

Player 2:

Correct, you took 7 trials to guess the number

Player 1 wins!
author = gauresh
date 26/10/2021
perpose=practical no 6 of harry
"""
import random
def guessgame():
    i = 6
    j =0
    if j%2 == 0:
        while True:
            userinp = int(input("guess the number"))
            i -= 1

            print(f"you left chance {i}")
            if userinp == randomnum:
                print("you win")
                i=6
                j +=1
                print(j)
            elif userinp <= randomnum:
                print("enter greater")
            elif userinp >= randomnum:
                print("Enter less")
            if i == 0:
                print("you loss")
                i=6
                j += 1

if __name__ == "__main__":
    try:
        pnum1 = int(input("enter number player \n"))
        pnum2 = int(input("enter number player \n"))
        randomnum = random.randint(pnum1,pnum2)
        guessgame()
    except Exception as e :
        print("enter interger value")