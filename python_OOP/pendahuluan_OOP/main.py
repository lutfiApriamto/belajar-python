class Mhs:
    mhs = []
    
    def __init__(self, name, kelas, npm):
        self.name = name
        self.kelas = kelas
        self.npm = npm
        new_mhs = [self.name, self.kelas, self.npm]
        Mhs.mhs.append(new_mhs)
        
        
mhs1 = Mhs("Lutfi", "4IA21", 51421011)
print(mhs1.name)
print(mhs1.kelas)
print(mhs1.npm)
print(mhs1.__dict__)

print(Mhs.mhs)
mhs2 = Mhs("keisha", "4IA25", 51421012)
print(Mhs.mhs)
# print(Mhs)