# calculate number of word.
f=open("sample.txt",'r')
data=f.read()
# data.split()
print(len(data.split()))
f.close()
