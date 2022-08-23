# KEY WORD *ARGS

def fungsi(**kwargs):
    print(kwargs)
fungsi(nama = "ucup", tinggi = 180, berat =  90)

# STUDI KASUS 
def math(*args, **kwargs):
    if kwargs["option"] == "tambah":
       for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("tidak ada operais") 
    return output

    hasil = math(1, 2,3, option = "tambah")
    print(f"hasil math adalah : {hasil}")