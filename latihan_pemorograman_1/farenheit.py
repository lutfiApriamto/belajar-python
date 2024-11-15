print("\n====== PROGRAM KONVERSI SUHU ======\n")

farenheit = float(input("Masukan Suhu Dalam farenheit : "))
print("Suhu adalah  ", farenheit, " farenheit")

celcius = (5 / 9) * (farenheit - 32) 
print("Suhu farenheit dalam celcius  ", celcius, " celcius")

reamur = (4/9) * (farenheit- 32)
print("Suhu farenheit dalam reamur  ", reamur, " reamur")

kelvin = (farenheit + 459.67 ) * (5/9)
print("Suhu farenheit dalam kelvin  ", kelvin, " kelvin")