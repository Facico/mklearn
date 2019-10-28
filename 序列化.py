import pickle
a=dict(name='clf',age=18,attr='ab')
f=open('fan.in','rb')
#pickle.dump(a,f)
b=pickle.load(f)
f.close()
print(b)
