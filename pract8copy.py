import random
def rohanmultiplication(number):
    wrong = random.randint(1,9)
     # print(wrong)
    tabel = [i * number for i in range(1,11)]
     # print(tabel[wrong])
    tabel[wrong] = tabel[wrong]+random.randint(1,8)
    #print(tabel)
    return tabel
def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1]!= i * number:
            print(table[i-1])
            return i

if __name__ == "__main__":
    number= int(input("Enter any no"))
    mytable = rohanmultiplication(number)
    print(mytable)
    print(iscorrect(mytable,number))