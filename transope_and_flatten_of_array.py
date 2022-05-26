import numpy as np
r,c=map(int,input().split())
ls=[]
for i in range(r):
    l=list(map(int,input().split()))
    ls.append(l)  
m=np.array(ls)
out1=m.transpose()
out2=m.flatten(order='c')
print(out1)
print(out2) 
