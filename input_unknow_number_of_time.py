lst=[]
while 1:
 try:
    lst.append(eval(input()))
 except Exception as e:
     print(e) 
     break
print(lst) 
