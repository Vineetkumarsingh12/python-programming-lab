s=input()
l=list(s)
ls=[l]
for i in range(len(l)):
    for j in range(len(ls[-1])-1):
        if ls[-1][j]==ls[-1][j+1]:
            ls.append(ls[-1][:j]+ls[-1][j+2:])
            break
print("".join(ls[-1])) if len(ls[-1])!=0 else print("Empty String")    #important
