s=["dog","deer","deal"]
f=input("enter character to find word ")
l=len(f)
if(l>0):
    for i in s:
      k=0
      for j in range(l):
        if(i[j]==f[j]):
           k+=1
      if(k==l):
        print(i) 
