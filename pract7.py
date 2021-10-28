"""
author:gauresh
date:27/10/2021
perpose :practical like serch engine
"""
def findword(lis,quer):
    i=0
    word=''
    if any(quer in word for word in lis):
        print(f'\{quer}\ is there inside the list!')
        print(word)
        i+=1
        #print(lis.count(word))
    else:
        print('\'AskPython\' is not there inside the list')
    return lis ,quer

if __name__ == "__main__":
    Sentences = ["Python is cool", "python is good", "python is not python snake"]
    quer = input("Enter query string\n")

    d=findword(Sentences,quer)
    print(d)