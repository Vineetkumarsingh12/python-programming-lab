try:
    try:
        print("hello world")
        raise ValueError
    except ValueError:
        print("Error")    
    print("inner block")    
except:
    print("outer block")    
    
   
