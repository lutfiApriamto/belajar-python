# # membuat gabungan area rentang dari angka

# # soal nomor 1. ---0++++5----8++++11-----

# inputUser = float(input("masukan angka yang bernilai\nlebih dari 0\nkurang dari 5, \nlebih dari 8, \ndan kurang 11\n:"))

# isLebihDariNol = (inputUser > 0 )
# print("Lebih dari 0 =", isLebihDariNol)

# isKurangDari5 = (inputUser < 5)
# print("Kurang dari 5 =", isKurangDari5)

# isLebihDari8 = (inputUser > 8)
# print("Lebih dari 8 =", isLebihDari8)

# isKurangDari11 = (inputUser < 11)
# print("kurang dari 11 =", isKurangDari11)

# isCorrect = (isLebihDariNol and isKurangDari5) or (isLebihDari8 and isKurangDari11)
# print("angka yang anda masukan: ", isCorrect)


# soal nomor 2 ++++0----5++++8-----11++++
inputUser = float(input("masukan angka yang bernilai\nkurang dari 0\nlebih dari 5, \nkurang dari 8, \ndan lebih 11\n:"))

isKurangDari0 = (inputUser <0)
print("kurang dari 0 =", isKurangDari0)

isLebihDari5 = (inputUser > 5)
print("Lebih dari 5 =", isLebihDari5)

isKurangDari8 = (inputUser < 8)
print("kurang dari 8 =", isKurangDari8)

isLebihDari11 = (inputUser > 11)
print("lebih dari 11 =", isLebihDari11)

isCorrect = isKurangDari0 or ( isLebihDari5 and isKurangDari8) or isLebihDari11
print("angka yang anda masukan: ", isCorrect)