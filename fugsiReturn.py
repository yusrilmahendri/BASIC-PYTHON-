# FUNGSI WITH RETURN 
def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat
y = kuadrat(5)
print(y)

def tambah(angka1, angka2):
    return angka1 + angka2

a = tambah(10,5)
print(a)

# FUNGSI DENGAN RETURN BANYAK
def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi 
k,l,m,n = operasi_matematika(5,3)
print(f"tambah : {k}")
print(f"kurang : {l}")
print(f"kali : {l}")
print(f"bagi : {n}")
