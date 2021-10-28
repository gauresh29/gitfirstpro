class electronicdevice:
    motherboard=3
    cameraunit=1
    batterry=1
class pocketgadget(electronicdevice):
    motherboard = 1

    batterry = 1
    def __init__(self,aname):
        self.name=aname

    def printdetails(self):
        return f"pocket gadeget type{self.name}"

class phone(pocketgadget):
    motherboard = 3
    cameraunit = 1
    batterry = 1

    def __init__(self, aname,type):
        self.name = aname
        self.type=type

    def printdetails(self):
        return f"pocket gadeget type is phone {self.name} type of device {self.type}"

edevice=electronicdevice()
pgadget=pocketgadget(["modem","phone"])
phonee=phone("nokia","cellphone")

print(pgadget.printdetails())
print(phonee.printdetails())
