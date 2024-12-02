'''MODULE ARITMATIKA'''

def tambah(a:float, b:float) ->float :
    return a + b

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    
    return hasil

def pangkat(n):
    return lambda angka : angka**n