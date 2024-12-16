class Hero:
    
    def __init__(self, inputName, inputHealth, inputAttackPower, inputArmorNumber):
        self.name = inputName
        self.health = inputHealth
        self.attackPower = inputAttackPower
        self.armorNumber = inputArmorNumber
        
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower)
        
    def diserang(self, lawan, attackPowerLawan):
        print(f"{self.name} diserang oleh {lawan.name}")
        attackDiterima = attackPowerLawan/self.armorNumber
        self.health -= attackDiterima
        print(f"darah {self.name} tersisa {self.health}")
        lawan.tambahDarah(lawan.attackPower)
        
        
    def tambahDarah(self, serangan):
        lifestill = serangan/10
        self.health += lifestill
        print(f"{self.name} mendapatkan life still ketika menyerang, total darah : {self.health}")
        
luoyi = Hero("Luoyi", 100, 10, 5)
xavier = Hero("xavier", 100, 20, 10)

luoyi.serang(xavier)
print("\n")
xavier.serang(luoyi)
print("\n")
xavier.serang(luoyi)
print("\n")
xavier.serang(luoyi)
print("\n")
xavier.serang(luoyi)
print("\n")
xavier.serang(luoyi)
