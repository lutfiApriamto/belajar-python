class Hero:
    # class variable
    jumlah = 0
    
    def __init__(self, InputName, InputKelas, InputNPM):
        # instance variable
        self.name = InputName
        self.kelas = InputKelas
        self.npm = InputNPM
        Hero.jumlah += 1
        print(f"membuah hero dengan nama {InputName}")

hero1 = Hero("Lutfi", "4IA21", 51421011)
print(Hero.jumlah)
hero2 = Hero("keisha ", "4IA22", 51421012)
print(Hero.jumlah)
hero3 = Hero("Fatih", "4IA23", 51421013)
print(Hero.jumlah)
print(f"\n\nData Class Hero {Hero.__dict__}")