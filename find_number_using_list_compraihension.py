def prime(x:int)->bool:
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    return c==2
lst=[2,3,4,56,7,1]
out=[i for i in lst if prime(i)]
print(out) 
