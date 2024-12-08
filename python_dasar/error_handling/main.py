# contoh pertama :

# try:
#     print(x)
# except:
#     print("\n\nBlok except dijalankan\n\n")

#  contoh kedua
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")

# contoh ketiga 
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")
    
# contoh ke 4
# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")

x =10
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")