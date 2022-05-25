ls1=[1,2,3,4,5,67]
ls2=[2,3,456]
x=len(ls1) if len(ls1)<len(ls2) else len(ls2)
ls=[]
for i in range(x):
    ls.append((ls1[i],ls2[i]))
print(ls)
