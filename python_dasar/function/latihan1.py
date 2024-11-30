'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# # Membuat header program
# os.system("clear")
# # os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukan nilai lebar: "))
# PANJANG = int(input("Masukan nilai panjang: "))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")
os.system("clear")

def header():
    '''fungsi Header'''
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # Mengambil input user
    pilihan = input("Masukan pilihan anda (keliling/luas): ").lower()
    lebar, panjang = 0, 0
    hasil_pilihan = True
    
    if pilihan not in ["keliling", "luas"]:
        hasil_pilihan = False
    else:
        lebar = int(input("Masukan nilai lebar: "))
        panjang = int(input("Masukan nilai panjang: "))

    return pilihan, hasil_pilihan, lebar, panjang


def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")

def main():
    header()
    PILIHAN,HASIL_PILIHAN,LEBAR,PANJANG = input_user()
    
    if HASIL_PILIHAN == False :
        print("pilihan yang anda masukan salah, silahkan ulangi lagi \n\n\n")
        main()
    else:
        if PILIHAN == "keliling" :
            KELILING = hitung_keliling(LEBAR,PANJANG)
            display("keliling", KELILING)
        else:
            LUAS = hitung_luas(LEBAR,PANJANG)
            display("luas", LUAS)


# Program utamanya
while True:
    main()

    isContinue = input("apakah lanjut (y/n)?")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")