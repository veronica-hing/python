from pet import Pet
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_foot = pet_food
        self.pet = Pet(pet)
    
    def walk(self):
        #invokes pet's play method
        self.pet.play()
        return self
    def feed(self):
        #invoke pet's eat method
        self.pet.eat()
        return self
    def bathe(self):
        #invoke pet's noise method
        self.pet.noise()
        return self

##testing things

derp = Ninja("derponica", "herp", ["jerky", "bacon"],["kibble"],"Jet")

derp.walk().feed().bathe()