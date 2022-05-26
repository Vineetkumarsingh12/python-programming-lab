time=input("enter time syntax<hour:mintue:secondmeridan>")
abbservation=time[8:]
if abbservation=='AM':
    if time[:2]=='12':
        print("00",time[3:-2],sep=':')
    else:
        print(time[:-2])
elif abbservation=='PM':
    if time[:2]=='12':
        print(time[:-2])
    else:
            print(int(time[:2])+12,time[3:-2],sep=':')
