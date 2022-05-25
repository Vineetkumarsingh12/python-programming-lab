f=open('sample.txt')
lst=f.read().split()
print(max(lst,key=len))
