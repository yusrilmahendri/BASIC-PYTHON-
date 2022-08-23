# operator dictionary 

data_dict = {
    "cup" : "ucup sruncup",
    "kd" : "kudung oh kudung"
}

# PANJNG DARI DICTIONARY
LENDICT = len(data_dict)
print(LENDICT)

# MENDETEKSI / CEK KEY EXIST HAS OR NO 
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict : {CHECKKEY}")

# MENGAKSES VALUE / GET AND READ 
print(data_dict.get("cup"))

# update data 
data_dict["cup"] = "Ucup cool"
print(data_dict)

data_dict.update({"cup":"yusril cool"})
print(data_dict)

# delete data pada dictienoray
del data_dict["cup"]
print(data_dict)