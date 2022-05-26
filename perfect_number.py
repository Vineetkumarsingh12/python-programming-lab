Num = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Num):
    if(Num % i == 0):
        Sum = Sum + i
if (Sum == Num):
    print(" %d is a Perfect Number" %Num)
else:
    print(" %d is not a Perfect Number" %Num)
