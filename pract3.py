try:
    while True:
        list1 = list(input())
        list1.reverse()
        print(f"{list1}list1")

        list1.reverse()
        list2 = list1[::-1]
        print(f"{list2}list2")

        reverse3=list2
        #print(reverse3)

        for i in range(len(reverse3)):
            reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1],reverse3[i]
            #reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
            print(f"the reversed list at i={i} is {reverse3[len(reverse3) -i -1]}")
            #print(reverse3[i])
        print(reverse3)


except Exception as e:
    print("Please enter list")