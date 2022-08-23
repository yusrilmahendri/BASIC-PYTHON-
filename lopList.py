# LOOPING FROM LIST 
# MAKE FOR LOOP 

kumpulan_angka = [4,3,2,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

# foor loop with range 
kumpulan_angka = [10,5,1,2,21,2]
panjang = len(kumpulan_angka)

for i in range(panjang):
print(kumpulan_angka[i])

# #with while
kumpulan_angka = [2,4,5,,3,6,1]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka : {kumpulan_angka[i]}")
i += 1

# list comprehension 
data = ["Ucup",1,2,3,"otung"]
[print(f"data : {i}") for i in data]

#enumerate 
data = ["Ucup",1,2,3,"otung"]
for index, data in enumerate(data):
    print(f"index = {index}, data = {data}")