print("\n====== PROGRAM KONVERSI SUHU ======\n")

kelvin = float(input("Masukan Suhu Dalam kelvin : "))
print("Suhu adalah  ", kelvin, " kelvin")

celcius = kelvin - 273
print("Suhu kelvin dalam celcius adalah  ", celcius, " celcius")

reamur = (4/5) * (kelvin - 273)
print("Suhu kelvin dalam reamur adalah  ", reamur, " reamur")

farenheit = kelvin * (9/5) - 459.67
print("Suhu kelvin dalam farenheit adalah  ", farenheit, " farenheit")