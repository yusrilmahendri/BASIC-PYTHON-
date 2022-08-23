# LIST == ARRAY 
# LIST ADALAH KUMPULAN DATA

data = [1, 2, 3]
print(data)

# how to create a alternatif list 
data_range = range(0, 5, 10) # range start, stop, step
data_list = list(data_range)
print(data_range)
print(data_list)

# create list with foor loop 
data_list_with_for = [i**2 for i in range(0, 10)]
print(data_list_with_for) 

# create list with for and if 
list_for_if = [i for i in range(0, 10) if i != 5]
print(list_for_if)
