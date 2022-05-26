#magic number
num=input()
total=sum(list(map(int,num)))

product=total*int(str(total)[::-1])
print("magic number") if product==int(num) else print("not magic number")
