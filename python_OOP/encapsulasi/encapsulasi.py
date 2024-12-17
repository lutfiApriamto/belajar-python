class Hero:
    
    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
        
    # getter
    def getName(self):
        return f"Nama Hero : {self.__name}"
    
    def getHealth(self):
        return f"Darah Hero : {self.__health}"
    
    # setter
    def diserang(self, jmlahSerangan):
        self.__health -= jmlahSerangan

alucard = Hero("alucard", 1000, 10)
print("\n\n")
print(alucard.getName())
print(alucard.getHealth())
print(alucard.diserang(10))
print(alucard.getHealth())


