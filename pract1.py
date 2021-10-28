"""Practice Problem 1 (Easy) | Python Tutorials For Absolute Beginners In Hindi #103
The task you have to perform is “Your Age In 2090”. This task consists of a total
 of 10 points to evaluate your performance.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable.
 Your program should detect whether the entered input is age or year of birth and tell the
  user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of module like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in
that particular year. (3points)
Your code should handle all sorts of errors like :            (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!
"""
try:
    while True:
        ageyear=int(input("Enter age or year of age"))
        currentyear=2021

        if ageyear < 100:
            print("you Enter age")
            finalyear=100-ageyear
            final1=2021+finalyear
            print(f"you will be 100 year in {final1}")
        elif ageyear > 1960 and ageyear <= 2021:
            print("you Enter year")

            ageyear = 2021 - ageyear
           # print(finalyear)
            finalyear1 = 100 - ageyear
           # print(finalyear1)
            final1 = 2021 + finalyear1
            print(f"you will be 100 year in {final1}")
        else:
            print("invalid input")
        perticularyear=int(input("Enter year that we can display age in that year"))
        if perticularyear > 2021 and perticularyear <= 2121:

            futureage= perticularyear - 2021
            futu=futureage+ageyear
            print(futu)

except Exception as e:
    print("Exception handel")