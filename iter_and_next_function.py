mylist = iter(["apple", "banana","mango"])
x = next(mylist)
print(x)
x =  list(mylist)   #next(iterable, default)
print(x)
x = next(mylist,0)
print(x)
