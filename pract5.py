#author gauresh
# date 26-10-2021//practical 5
#perpose=practical code with harry 5th pract
#function for printing next pallendron
def nextpallendrom(num):
    #print(mylist)
    if num >10:
         while not ispallendrom(num) :
            num += 1
         return num
    else:
        return num
#This function define number is palllendrom or not
def ispallendrom(num):
    return str(num) == str(num)[::-1]
    #print("already ")
if __name__ == "__main__":
    num=int(input("How many numbers you want to enter"))
    mylist=[]
    newlist=[]
    for i in range(num):
         pnum=int(input("enetr number\n"))
         mylist.append(pnum)

    for i in range(num):

        #print(f" {mylist[i]} {nextpallendrom(mylist[i])}")
        p=nextpallendrom(mylist[i])
        newlist.append(p)
    print(mylist)
    print(newlist)