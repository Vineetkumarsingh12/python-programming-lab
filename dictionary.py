dct={'vineet':1,'jay':"big zero",'jay':{'big star':'in c programing'}}
print(dct['jay']['big star'])
dct={'vineet':1,'jay':"big zero",'jay':['big star','in c programing']}
print(dct['jay'][0])
dct={1:100,[2,4]:'jay'} #key is always immutable
print(dct[1])
dct={1:100,(1,2):1}
print(dct[(1,2)])
dct={'name':'vineet',1:'vikas',1.0:"shivam"}  #value 1 and 1.0 is same
print(dct[1])
