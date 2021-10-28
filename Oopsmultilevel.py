class dad:
    basketball=1

class son(dad) :
    dance=1
    def isdance(self):
        return f"hello i can dance {self.dance}"
class grandson(son):
    dance = 6

    def isdance(self):
        return f"hello i can dance awesomely {self.dance}"
darry=dad()
sonry=son()
gauresh=grandson()
print(gauresh.isdance())