#modle matematika dengan import 
# crate file matematika then file name matematika.py
# crate file matematika then file name mainAlias.py
from  matematika import tambah, kali

# ambil semua module
from matematika import *

import matematika

# penggunaan alias 
from matematika import tambah as x

# implementasi cara manggil from 
hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

#implementasi alias
hasil_t = x(1,2,3,4,5)
print(f"hasil tambah = {hasil_t}")

#implementasi dari panggil import 
hasil_kali = matematika.kali(1,2,4,5,6)
print(f"hasil kali = {hasil_kali}")

# pangkat_3 = matematika.pangkat(3)
# print(f"hasil pangkat = {pangkat_3}")

# import module make from 
