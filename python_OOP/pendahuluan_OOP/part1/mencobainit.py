class Hero:
    def __init__(self, InputName, InputKelas, InputNPM):
        self.name = InputName
        self.kelas = InputKelas
        self.npm = InputNPM


hero1 = Hero("Lutfi", "4IA21", 51421011)
hero2 = Hero("keisha ", "4IA22", 51421012)
hero3 = Hero("Fatih", "4IA23", 51421013)

print(f"DATA hero1  {hero1.__dict__} \n")
print(f"DATA hero2  {hero2.__dict__} \n")
print(f"DATA hero3  {hero3.__dict__} \n")