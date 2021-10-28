import pickle
import requests
irisdata = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
text_1=irisdata.text
#print(text_1)

x = iter(text_1.split("\n"))

p=list(x)
#print(p)
#print(type(p))

#create piokel
""""file = "iris.pkl"
fileobj = open(file,'wb')
pickle.dump(p,fileobj)
fileobj.close()"""

file = "iris.pkl"
fileobj = open(file,'rb')
irris=pickle.load(fileobj)
print(irris)


