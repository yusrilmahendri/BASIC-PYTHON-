# MULTIKEY DICTIONRAY  DAN NESTING DICTIONRAY

import datetime

mahasiswa1 = {
    'nama' : 'Yusril Mahendri',
    'nim' : '1800018397',
    'sks' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2001, 4, 10)
}


mahasiswa2 = {
    'nama' : 'Mahendri',
    'nim' : '1800018290',
    'sks' : 144,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2002, 10, 10)
}

mahasiswa3 = {
    'nama' : 'Mahendri yusril',
    'nim' : '1800018291',
    'sks' : 160,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2000, 8, 3)
}

data_mahasiswa = {
  'MAH001':mahasiswa1,
  'MAH002':mahasiswa2,
}

print(f"{'KEY' : <6} {'nama': <17} {'sks': 3} {'beasiswa': <9} {'lahir': <10} ")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:< 6} {NAMA:< 17} {SKS:< 13} {BEASISWA :<9} {LAHIR:<10} ")