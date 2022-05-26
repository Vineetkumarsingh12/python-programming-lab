#handle optional argument
def optional_sum(a:int,b:int,*c):
    print(c)
    return a+b
out=optional_sum(3,4,5,6,7)  
print(out) 
