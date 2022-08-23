# COPY DICTIONRAY 
teman_teman = {
    "cup" : "ucup kuncup",
    "yusr" : "yusril mahendri",
    "hen" : "mahendri",
}

friends = teman_teman.copy()
print(friends)

# POP DICTIONRAY 
dataCup = friends.pop("cup")
print(f"data asep : {dataCup}")
print(f"data  : {friends}")

# pop dictionray  (get data a last)
dataTerakhir = friends.popitem()
print(f"data terakhir {dataTerakhir}")
print(f"data terakhir {friends}")