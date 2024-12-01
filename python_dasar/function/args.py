'''*args'''

# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"hex data_list = {hex(id(data_list))}")
    print(f"hex data fungsi = {hex(id(data))}")
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

data = ["otong",100,120]
print(f"hex data kirim = {hex(id(data))}")
fungsi(data)

print("\n\n\n\n")

# kenalan dengan *args

def fungsi(*args):
    print(type(args))
    print(args)
    print(f"hex args = {hex(id(args))}")
    
    nama = args[0][0]
    tinggi = args[0][1]
    berat = args[0][2]
    
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

data = ["dudung",120,120]
print(f"hex data = {hex(id(data))}")
fungsi(data)
print("\n\n\n\n")


# studi kasus

def tambah(*data):
    # cara menggunakan method sum dan  memanfaatkan list chomprehension
    output = sum([angka for angka in data])
    return output


    # cara manual
    
    # output = 0
    # for angka in data:
    #     output += angka
    
    # return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")