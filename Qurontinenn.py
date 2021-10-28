def sercher():
    import time
    book="this is way ypu go long"
    time.sleep(5)
    while True:
        text= (yield)
        if text in book:
            print("text in book")
        else:
            print("text is not in book")
opp=sercher()
print("search started")
next(opp)
print("next method started")
opp.send("adsa")
opp.send("is")
opp.close()

