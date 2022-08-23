# LOOPING IN DICTINORAY 
teman_teman = {
    "cup" : "ucup srrucup",
    "yus" : "yusril mahendri",
    "hen" : "mahendri"
}

# looping first try || output adalah key 
for teman in teman_teman:
    print(teman)

# operator for get items / iterables 
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)
for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)
for item in teman_teman.items():
    print(item)
for key,value in teman_teman.items():
    print(f"key = {key} value : {value}")