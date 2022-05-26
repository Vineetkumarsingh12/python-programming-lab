f=open("sample.txt",'rb')
data=f.read().decode('utf-8')
print(data)
f.close()
