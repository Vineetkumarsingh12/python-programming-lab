x=int(input())
ls=[[1]]
for i in range(x-1):
    n=0
    inter_lst=[]
    cp=ls[-1]
    lsc=len(cp)
    for i in range(lsc):
        if cp[i]!=n:
            f=i; count=0
            while f<lsc and cp[i]==cp[f]:
                count=count+1
                f=f+1
            inter_lst.extend([count,cp[i]])
            n=cp[i]
    ls.append(inter_lst)     # extend concate elements in the list and append add the element as a single list. 
for i in ls:
    print(*i)    
