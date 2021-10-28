def namesercher():
    import time
    names="hello,mola,bhaiyya,patalo,kanase,gautam"

    time.sleep(3)
    while True:
        text = (yield )
        if text in names:
            print("your name in names")
        else:
            print("you are adopted bro hahaha")
namee=namesercher()
print("now executing")
next(namee)
namee.send("gauresh")
