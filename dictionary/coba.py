# Membuat dictionary dari list key
keys = ["nama", "usia", "kota"]
default_value = "Belum Diisi"

dictionary = dict.fromkeys(keys, default_value)
print(dictionary)