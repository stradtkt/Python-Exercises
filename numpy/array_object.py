import numpy as np

x = np.arange(2,11).reshape(3,3)
print(x)


#reverse the array
x = np.arange(12,38)
x = x[::-1]
print(x)

#put 0 inside of 1
x = np.ones((5,5))
print(x)
x[1:-1,1:-1] = 0
print(x)

#put 0 on the outside of 1
x = np.ones((3,3))
print(x)
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)

fvalues = [0,12,45.21,34,99.81]
F = np.array(fvalues)
print(5*F/9 - 5*32/9)