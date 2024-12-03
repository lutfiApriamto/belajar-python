# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Cek Nilai Kelulusan!")

# Variabel dan Fungsi
nilai_uas = tk.IntVar()
nilai_uts = tk.IntVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    TOTAL_NILAI = (nilai_uts.get() + nilai_uas.get()) /2
    predikat = ''
    pesan = ''
    
    if (TOTAL_NILAI <= 100) and (TOTAL_NILAI >= 90) :
        predikat = 'A'
        pesan = f'selamat anda lulus matakuliah anda mendapatkan predikan {predikat}'
    elif (TOTAL_NILAI <= 89) and (TOTAL_NILAI >= 80) :
        predikat = 'B'
        pesan = f'selamat anda lulus matakuliah anda mendapatkan predikan {predikat}'
    elif (TOTAL_NILAI <= 79) and (TOTAL_NILAI >= 70) :
        predikat = 'C'
        pesan = f'selamat anda lulus matakuliah anda mendapatkan predikan {predikat}'
    elif (TOTAL_NILAI <= 69) and (TOTAL_NILAI >= 60) :
        predikat = 'D'
        pesan = f'anda tidak lulus matakuliah, karena anda mendapatkan predikan {predikat}'
    else:
        predikat = 'E'
        pesan = f'anda tidak lulus matakuliah, karena anda mendapatkan predikan {predikat}'
        
    print(TOTAL_NILAI)
    
    showinfo(title="NILAI AKHIR!",message=pesan)


# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nilai_uas_label = ttk.Label(input_frame,text="Masuka Nilain UAS anda:")
nilai_uas_label.pack(padx=10,fill="x",expand=True,)
# 2. entry nama depan
nilai_uas_entry = ttk.Entry(input_frame,textvariable=nilai_uas)
nilai_uas_entry.pack(padx=10,fill="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Masukan Nilai UTS anda")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=nilai_uts)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="Check Nilai!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop()