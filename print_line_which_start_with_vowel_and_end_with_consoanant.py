with open("sample.txt",'r') as f:
 x=f.readlines()
 alpha=['a','A','e','E','i','I','o','O','u','U']
 for i in x:
   if i.split()[0][0] in alpha and i.split()[-1][-1] not in alpha :
     print(i,end='')
