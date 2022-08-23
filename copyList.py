# teknik menduplikat list 

a = ["ucup", "otong", "dudung"]
print(a)

b = a                  
print(b)

# rename member from a 
# ini akan merubah dari kedua list 
a[1] = "yusil"
print(a)
print(b)

# menduplikat list with copy 
c = a.copy()
c[1] = "adang"
print(a)
print(b)
print(c)
