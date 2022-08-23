# INDEX  0        1         2
data = ["ucup", "otong", "dudung"]

# HOW TO GET VALUE DATA IN LIST 
data_0 = data[0]
print(data_0)
data_terakhir = data[-1]
print(data_terakhir)

# MANIPULASI DATA 
# data.insert(posisi, item)
data.insert(1, "Asep")
print(f"data sesudah ditambahkan : \n{data}")

#menambahkan di akhir list
data.append("jajang")
print(f"tambahkan lagi data tetapi taruh diakhir : \n{data}" )

#menambahkan list dengan list 
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan : \n{data}")

# MERUBAH DATA 
data[2] = "Michale"
print(f"data rubah : {data}")

# romve data 
data.remove("Usep")
print(f"data uyang sudah di hapuskan :{data} ")