class Ninja:
    def __init__(self, first_name , last_name ,pet, treats , pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self


    
class Pet:
    def __init__(self,type,tricks,health,energy):
        self.type = type 
        self.tricks = tricks 
        self.health = health 
        self.energy = energy 
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("hababababbahahahabhabhab")
        return None
    

ghost = Pet("Wolf","defend",100,110)

ali = Ninja("Ali","Bourara",ghost,"cracker","chicken")



ali.feed().walk().bathe()
print(f"health is : {ghost.health} energy is { ghost.energy}")



# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
