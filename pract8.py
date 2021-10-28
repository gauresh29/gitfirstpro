"""Problem Statement:-
 Rohan das is a fraud by nature. Rohan Das wrote a python function to print a

 multiplication table of a given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test.
You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s actions by writing a
 python program that validates Rohan’s multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and
expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number)
and return the index where rohan’s function is wrong and
print it to the screen! If the table is correct, your function returns None"""

import random

# rohan fraud function
def rohanMultiplication(number):
    mylist=[]
    for item in range(1,11):
        if item == 5:
            num4 = random.randint(1, item)
            # print(num4)
            # print(item*number)
            mylist.append(num4)
        else:
            #print(item*number)
            mylist.append(item*number)

    return mylist
# Cid function that detect rohan is froud or not
def isCorrect(table,number):
        i = 0
        for item in table:
            i +=1
            if i*number != item:
                print(f"rohan cheating at position {i} as {item}")


if __name__ == "__main__":
    outputrohan= rohanMultiplication(6)
    print(outputrohan)
    #outputrohanmul=[mul for mul in outputrohan]
    findchor=isCorrect(outputrohan,6)
    #print(findchor)