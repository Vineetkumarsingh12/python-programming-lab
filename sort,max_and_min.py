ls1=["aman","Ansu","a","anshika"]# assending order to ascii value of first character
ls1.sort(key=min)
ls1.sort(key=max)
ma=max(ls1,key=len)
mi=min(ls1,key=len)
print("ascending sort--->",ls1)
print("longest word--->",ma)
print("shortest word--->",mi)
