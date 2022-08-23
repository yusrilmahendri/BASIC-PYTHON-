# how to in data a argument 

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("ucup", 170, 40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi(["yusril mahendri", 100, 200])

# WITH *args  adalah teknik mengambil dari banyak input 
# def fungsi(*args):
#      nama = args[0]
#      tinggi = args[1]
#      berat = args[2]
#          print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
# fungsi("dudung", 120, 120)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka 
    return output 
hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil} ")

hasil = tambah(1,2,10)
print(f"hasil = {hasil} ")

