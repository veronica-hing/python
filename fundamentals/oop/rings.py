## class which is ring

class Ring:
    #making a class attribute that stores all the rings ever created
    everyRing = []
    def __init__(self, material, peoples, stone): #define the constructor to require parameters material, peoples, stone
        #assign the attributes with the given parameters
        self.material = material
        self.peoples = peoples
        self.stone = stone
        #adding the ring we just made to the list, everyRing which is a class attribute
        Ring.everyRing.append(self) #pass self to get entire ring so it is list of rings

    def changeMat(self, new_material): #example of method that alters a attribute to given parameter
        self.material = new_material # reassignment of attribute material
        return self # enables chaining
    def printStats(self): #example of method that just prints the stats of rings
        #able to access attributes since we have access to self
        # print using an f-string
        print(f"the ring is {self.material} of {self.peoples} peoples")
        return self
    #decorator to announce we are making a class method
    @classmethod
    def allRings(cls): #pass in cls so method knows to refer to the class that we're making (Ring in this case)
        for ring in cls.everyRing:
            #calls the printStats method each ring instance has
            ring.printStats()
    
    @classmethod # put the decorator before declaration of each new class method
    def makeDark(cls):
        for ring in cls.everyRing:
            ring.changeMat("dark-matter")



##testing out our class
elves = Ring("mithrill", "Elven", "diamond")
dwarves = Ring("silver", "Dwarven","Ruby")
human = Ring("copper", "humans", "garnet")

dwarves.changeMat("steel")
#elves.printStats()

#prints all the rings
Ring.allRings()
#testing other class method
Ring.makeDark()
#see if class method made changes to all the rings
Ring.allRings()
