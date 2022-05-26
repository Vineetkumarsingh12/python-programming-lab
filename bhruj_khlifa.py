n=int(input())
b=len(bin(n)[2:])
if n>=0 and n<=500:
    for i in range(n):
        print(bin(i)[2:].rjust(b)) 
