import pickle

#cars = ["tata","garittty bmw","nimoo ferrai"]
#file = "mycar.pkl"
#fileobj = open(file,'wb')
#pickle.dump(cars,fileobj)
#fileobj.close()


file = "mycar.pkl"
fileobj = open(file,'rb')
dp=pickle.load(fileobj)
print(dp)
