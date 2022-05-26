h=int(input())
l=int(input())
for i in range(h):
    for j in range(h-i-1):
        print(" ",end="")
    print("*",end="")    
    for j in range(2*i-1):
        print(" ",end="") if i!=l-1 else print("*",end="")
    if i!=0:    
        print("*",end="")  
    print() 
