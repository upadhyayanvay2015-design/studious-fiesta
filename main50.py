class Family:
    def __init__(self, eye, height):
        self.eye = eye
        self.height = height
    def show(self):
        print(f"Eye color: {self.eye}, Height: {self.height}")
class kid(Family):
    def __init__(self, name, age, eye, height):
        super().__init__(eye, height)
        self.name = name
        self.age = age
        super().__init__(eye, height)
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        super().show()
    def fav_hobby(self,hobby):
        print(self.name," loves",hobby)

child=kid("Anvay", 11,"Brown","4.10 ft") 
child.show()
child.fav_hobby("Playing guitar and singing")

print(" Is subclass child of Family?", issubclass(kid, Family))
child1=kid("Yalinee", 11,"Green","4.9 ft") 
child1.show()
child1.fav_hobby("Walking")