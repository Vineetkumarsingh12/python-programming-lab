import numpy as np
arr=np.array(list(map(int,input().split())))
arr.reshape(3,3)
print(arr.reshape(3,3))
arr.shape=(3,3)
print(arr)
