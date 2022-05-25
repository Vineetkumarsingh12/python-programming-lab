def vineet():
    x=20
    def vikas():
        global x #  function create  variable on the top where function start.
        x=88
    print("before calling vikas",x)
    vikas()
    print("after calling vikas",x)
vineet()    
print(x) 
