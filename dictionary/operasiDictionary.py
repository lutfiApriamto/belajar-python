# operator dictionary

data_dict = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}\n\n")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}\n\n")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan \n\n")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict )
data_dict["sep"] = "asep si kasyep"
print(f"{data_dict} \n\n")

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si kweren"}) # kalau gak ada diadd ajah
print(f"{data_dict} \n\n")

# mendelete data pada dictionary
del data_dict["faqih"]
print(f"{data_dict} \n\n")
