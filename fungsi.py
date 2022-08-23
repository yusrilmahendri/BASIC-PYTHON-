# FUNGIS HAS 3 : FUNCTION, METHOD, SUBRUTIN /RUTIN

# FUNCTION 
def hello_world():
    print("Hello world!")

hello_world()

# FUNGSI  WITH ARGUMENT 
# def nama_fungsi(argument/ prameter)
# badan fungsi 

def hello(nama):
    print(f'hallo, {nama} selamat belajar python')

hello('yusril')

def say_hi(list_peserta):
    data_perserta = list_peserta.copy()
    for peserta in data_perserta:
        print(f"hallo {peserta}")
    
anggota_boyband = ["yusril","mahendri","ihza"]

say_hi(anggota_boyband)