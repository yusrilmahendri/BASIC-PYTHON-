data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1]

print(data_2D)

#  GET DATA IN NESTED LIST 
data = data_2D[0]
data1 = data_2D[0][0]
print(data)
print(data1)

#data copy 
data_2D_copy = data_2D.copy()
data_2D[1][0] = 5
# print(data_2D)

# MENGGUNAKAN DEEP COPY 
from copy import deepcopy

data_2D = [data_0, data_1]
data_2D_deepCopy = deepcopy(data_2D)
print(data_2D_deepCopy)