# LAMBDA FUNCTION 

def fungsi_kuadrat(angka):
    return angka**2
print(f"hasil fungsi kuadrat : {fungsi_kuadrat(4)}")

# with lambda 
kuadrat = lambda angka:angka**2
print(f"hasil from lambda kuadrat : {kuadrat(3)}")
pangkat = lambda num, pow: num**pow 
print(f"hasil lambda pangkat : {pangkat(4,2)}")

# KEGUNAAN LAMBDA 

# sort for list biasa 
data_list = ["Otong","ucup","dudu"]
data_list.sort()
print(f"sorted list : {data_list}")

# sorting make panjang 
def panjang_nama(nama):
    return len(nama)
    data_list.sort(key = panjang_nama)
print(f"sorted list  by len : {data_list}")

# ini fungsi contoh dari lambda 
data_list = ["otong","yusril","rio"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda : {data_list}")

# filter 
data_angka = [1,2,3,4,5,6,7,8,9,10]
# kurang dari  5
def ganjil(angka):
    return angka < 5 
    
angka_baru = list(filter(lambda x:x<7,data_angka))
print(angka_baru)

#kasus genap
data_genap = list(filter(lambda x:(x%2==0), data_angka))
print(data_genap)
#kasus ganjil 
data_ganjil = list(filter(lambda x:(x%2 != 0), data_angka))
print(data_ganjil)

#kelipatan 3
data_3 = list(filter(lambda x:(x%3==0), data_angka))
print(data_3)

#with currying then 
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

#kelipatan 3 