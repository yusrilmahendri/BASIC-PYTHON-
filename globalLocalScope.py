# GLOBAL DAN LOCAL SCOPE

nama = "yusril" # variabel global

def fungsi():
    print(f"ini fungsi menampilkan {nama}")
fungsi()

#akses variabe; global make loop 
for i in range(0, 5):
    print(f"loop {i} - {nama}")

#PERCABANGAN 
if True:
    print(f"if menampilkan {nama}")

# VARIABEL LOKAL SCOPE 
def fungsi2():
    nama_loc = "ucup" # variabel lokal scope
fungsi2()
print(nama_loc)

# EXAMPLE 
angka = 0
def ubah_angka(value_new):
  global  angka  # ini akan bilang fungsi ini akan mendaapatkan akses untuk merubah 
  angka = value_new
print(f"sebelum {angka}")
ubah_angka(10)
print(f"sesudah {angka}") 


