data_0 = [1, 2]
data_1 = [3, 4]

# LIST BIASA 
data_list_biasa = [1,2,3,4,5,6]
print(data_list_biasa)

# LIST 2 D 
list_2D = [data_0, data_1, data_list_biasa]
print(list_2D)

#contoh penggunaan 
peserta_0 = ["yusril", 25, "laki-laki"]
peserta_1 = ["mahendri", 25, "perempuan"]

list_peserta = [peserta_0, peserta_1]
print(list_peserta)

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"gender\t : {peserta[2]}\n")

#  WITH REFERENCE 
list_copy = list_peserta.copy()
print(list_copy)
peserta_0[0] = "Yusril iza mahendri"
print(f"nama : {list_copy}")
print(f"nama : {list_peserta}")