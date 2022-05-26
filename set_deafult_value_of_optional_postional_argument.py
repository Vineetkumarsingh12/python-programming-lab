#set default value of optional positional argument
def optional_sum(*c,d):   # *c store value as a tuple.
    s=0 
    for i in c:
        s+=i
    return s+d
out=optional_sum(4,5,6,7,8,d=10)        
print(out)
