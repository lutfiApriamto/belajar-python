class Hero:
    
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name : {} \nhealth : {}".format(self.name, self.__health)
        
    @property
    def info(self):
        return  "name : {} \nhealth : {}".format(self.name, self.__health)
    
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
        self.__armor += input
        
    @armor.deleter
    def armor(self):
        print('armor di delet')
        self.__armor = None

keisha = Hero("Keisha", 999, 99)
print('merubah info')
print(keisha.info)
keisha.name = "lutfi"
print(keisha.info)

print('menggunakan getter dan setter python asli')
print(f"armor Keisha : {keisha.armor}")
keisha.armor = 10
print(f"armor Keisha : {keisha.armor}")