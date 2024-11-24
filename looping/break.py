# Break
angka = 0

while angka < 5:
	angka += 1
	print(f"angka sekarang = {angka}")

	if angka == 3:
		print("nice!")
		break

	print("wassup!")

print("cukuuup finish!")

# data_int = int(input("hitung sampai = "))

# angka = 0

# while True:
# 	angka += 1
# 	print(f"count = {angka}")

# 	if angka == data_int:
# 		print("nice!")
# 		break

# 	print("wassup!")

# print("cukuuup finish!")

a = 1

for i in range(5):
    if a%2:
        print(f"aku ganteng{a}")
        a += 1
    else:
        a += 1
        continue