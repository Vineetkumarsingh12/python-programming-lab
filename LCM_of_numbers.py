def LCM(ls):  
    b=1
    for i in ls:
        a=i
        b=lcm(a,b)
    return b    
def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
def lcm(a,b):
    return ((a*b)/gcd(a,b)) 
ls=[2,3,4,5,6,7]
b=LCM(ls)
print(b)

