# DEFAULT ARGUMENT FUNGSI 

def say_hello(nama = "Yusril"):
    print(f"hallo {nama}")

say_hello()

def hitung(input1 = 5, input2 = 3):
    a = input1 + input2 
    print(a)
hitung()

def hi(i = 1, z = 3, y = 5):
    b = i + z + y
    return b

hi()
#if want to rename value prameterdefault
print(hi(z=10))