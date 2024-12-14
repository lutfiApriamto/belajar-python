class Hero:
    # class Variable
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, InputPower, inputArmor):
        # intance variable
        self.name = inputName
        self.health = inputHealth
        self.power = InputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        
    # method tanpa argumen
    def sayName(self):
        print(f"hello namaku adalah {self.name}")
        
    # method dengan argument
    def helthUp(self, inputHealtUp):
        self.health += inputHealtUp
        
    # method dengan return
    def getHealth(self):
        return self.health
    
    # method dengan argument dan nilai return
    def powerUp(self, inputPowerUp):
        self.power += inputPowerUp
        return self.power
    
    
hero1 = Hero("Lutfi", 2000, 90, 1000)
hero1.sayName()
hero1.helthUp(200)
print(hero1.getHealth())
print(hero1.powerUp(500))

