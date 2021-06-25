import pickle
def make():
    f=open("password.dat",'wb')
    pickle.dump("*insert password*",f)
    f.close()
def pg(password):
    f=open("password.dat",'wb')
    pickle.dump(password,f)
    f.close()

def ret():
    f=open("password.dat",'rb')
    d=pickle.load(f)
    return d

