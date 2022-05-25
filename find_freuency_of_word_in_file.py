f=open("sample.txt")
lst=f.read().split()
fstr=''.join(lst)
print(fstr.count(input("enter the word")))
