import pickle
f=open("binary.dat","rb")
rec=[]
while True:
    try:
        rec=pickle.load(f)
        print(rec)
    except:
        break
