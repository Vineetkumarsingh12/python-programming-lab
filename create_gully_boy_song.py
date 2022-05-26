s=input()
pos=int(input())
t=int(input())
if (pos>0 and pos<len(s)-s.count(" ") ) and (t>0 and t<10):
 s=s.replace(" ",'')
 a=s[pos-1:].replace(' ','')
 b=s[:pos-1].replace(' ','')
 f=a+b
 for i in range(t):
    for i in f:
        print(i,end=" ")
    

