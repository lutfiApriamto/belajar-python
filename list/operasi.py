## Operasi

# index   0(-3)  1(-2)  2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}\n\n")

data.insert(1,"Asep")
print(f"data sesudah ditambah = \n{data}\n\n")

# menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi =\n{data}\n\n")

# menambah list dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan =\n{data}\n\n")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data rubah = \n{data}\n\n")

# meremove data

data.remove("Ujang")
print(f"data remove = \n{data}\n\n")

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}\n\n")
print(data_akhir)

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"\n\ndata angka = \n{data_angka}\n\n")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3} \n\n")

# ambil posisi data (index)

data = ["Ucup","Otong","Dudung","Ujang"]

print(f"data = {data}\n\n")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang} \n\n")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data} \n\n")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")

data_baru = [1,5,2,6,9,10, "otong", "keisha", 'lutfi', 'joko']
data_baru.sort()
print(data_baru)