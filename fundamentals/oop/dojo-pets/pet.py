class Pet:
    def __init__(self, name, type = "doggo", tricks = ["sit"]):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 50
    def sleep(self):
        #increase pet energy by 25
        self.energy += 25
        return self
    def eat(self):
        #increase pet energy by 5 and health by 10
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        #increases pet's health by 5
        self.health += 5
        return self
    def noise(self):
        print("BORK BORK")
        return self

class FancyPet(Pet):
    def __init__(self, name, type, tricks, breed):
        super().__init__(name,type,tricks)
        self.breed = breed
    def noise(self):
        print("Fancy Bork")
        return self
##testing things 

if __name__ == "__main__":
    jet = Pet("Jet")
    jet.noise()
    ##if the methods bonked, we wouldn't get a second noise
    jet.play().eat().sleep().noise()
    keno = FancyPet("Keno","work-doggo",["get harness","sit", "haw", "gee", "hike", "whoa","easy"],"Husky")
    keno.noise()
