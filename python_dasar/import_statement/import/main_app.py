# import

# fungsinya adalah untuk mengambil 
# program dari file external .py

# 1. untuk menyambung program dari external
import program_print


# 2. import dengan data
import variable
# data ada di namespace variable
print(variable.data)

# 3. import dengan fungsi
# import matematika

# hasil = matematika.tambah(4,5)
# print(hasil)

print("\n\n")

# from matematika import tambah, kali, pangkat
# import matematika 
# from matematika import *
from matematika import tambah as plus
from matematika import kali as minus
from matematika import pangkat as puangkat


hasil_tambah = plus(4,5)
print(f"hasil Tambah = {hasil_tambah}")

hasil_kali = minus(1,2,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = puangkat(2)
print(f"hasil pangkat = {hasil_pangkat(4)}")