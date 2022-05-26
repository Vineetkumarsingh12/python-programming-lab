def fun(dd, pre=''):

    print(dd,pre)
    print(type(dd))
    if type(dd)==dict :
        print( {pre + '.' + k if pre else k: v for kk, vv in dd.items() for k, v in fun(vv,kk).items()},2)
        return {pre + '.' + k if pre else k: v for kk, vv in dd.items() for k, v in fun(vv,kk).items()}
    else:
        print({pre: dd},1)
        return {pre: dd}

ini_dict = {"key":3,"foo":{"b":5,"bar":{'baz':8}}}
print("main dict", str(ini_dict))
print("output dict", str(fun(ini_dict)))
