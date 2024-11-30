def penjumlahan(a, b):
    hasil = a + b
    return hasil

# Memanggil function dan menangkap nilai return
hasil_penjumlahan = penjumlahan(3, 5)
print(f'hasil penjulmahan adalah {hasil_penjumlahan} \n\n') 

def operasi(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    return tambah, kurang, kali

# Memanggil function dan menangkap beberapa nilai
hasil_tambah, hasil_kurang, hasil_kali = operasi(5, 3)
print(f"hasil Tambah adalah {hasil_tambah}")  # Output: 8
print(f"hasil Kurang adalah {hasil_kurang}")  # Output: 2
print(f"hasil Kali Adalah {hasil_kali}")    # Output: 15