# import sangat penting, import for mengambil program dari luar 
# FUngsi import adalah mengambil file dari external .py
# create file new for import dengan file program_print.py

#menyambung program dari exterbnal
import program_print 

#import data / variabel 
print(program_print.data)

#import with fungsi 
hasil = program_print.tambah(4, 5)
print(hasil)
