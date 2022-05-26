st="vineet"
def reverse(st):
    if len(st)==0:
        return 
    rest=st[0]
    reverse(st[1:])
    print(rest,end="")
reverse(st) 
