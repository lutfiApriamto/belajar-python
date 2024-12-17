class Hero:
    # class variable
    jumlah = 0
    
    def __init__(self, name, health):
        # instance variable
        self.name = name
        self.healt = health
        
        # private variable
        self.__private = "private"
        
        # protected variable
        self._protected = "protected"
        
print("\n\n")

lina = Hero("Lina", 1000)
print(lina.__dict__)
print(f"\nsebelum : {lina._protected}\n")
lina._protected = "testing"
print(lina.__dict__)
print(f"\nsesudah : {lina._protected}\n")
























# lina.__private = "testing"
# print(lina.__dict__)
# print(lina.__private)