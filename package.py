# HOW TO CREATE PACKAGE 
# PACKAGE ADALAH SEBUAH PROGRAM / TEMPAT DALAM MENARUH MODULE 
# implementasi dengan cara buat folder baru, penamaan adalah sains  
import sains.matematika
from sains import matematika as x         

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari : {hasil_tambah}")

hasil_kali = x.tambah(1,2,3,4,5,6)
print(f"hasil perkalian {hasil_kali}")

