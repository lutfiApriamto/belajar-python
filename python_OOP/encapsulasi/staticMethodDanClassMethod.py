class Hero :
    
    # private class Variable
    __jumlahHero = 0
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlahHero += 1
        
    # method ini hanya berlaku untuk object dan 
    def getJumlah(self):
        return f"jumlah Hero : {Hero.__jumlahHero}"
    
    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah1():
        return f"jumlah Hero : {Hero.__jumlahHero}"
    
    # menggunakan static method
    # method decoration (decorator) menempel pada object danclass
    @staticmethod
    def getJumlah2():
        return Hero.__jumlahHero
    
    # menempel dengan class dan object namun dapat diberikan argument berguna untuk inheritence
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlahHero
    
alucard = Hero('Alucard')
# menggunakan mehthod getJumlah()

# print(alucard.getJumlah()) # cara ini bisa
# print(Hero.getJumlah()) # cara ini gak bisa

# menggunakan method getJumlah1()
# print(alucard.getJumlah1()) # cara ini gak bisa
# print(Hero.getJumlah1()) # cara ini bisa

# menggunakan mehtod decoration (decorator) @staticmethod
# print(f"Menggunakan Class {Hero.getJumlah2()}") # cara ini bisa
# print(f"Menggunakan Object {alucard.getJumlah2()}") # cara ini bisa

# menggunakan mehtod decoration (decorator) @classmethod
# print(f"Menggunakan Class {Hero.getJumlah2()}") # cara ini bisa
# print(f"Menggunakan Object {alucard.getJumlah2()}") # cara ini bisa