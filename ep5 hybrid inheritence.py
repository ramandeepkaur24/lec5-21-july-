class animal:
    def loyal(self):
        print("animals are loyal")
class dog(animal):
    def bark(self):
        print("Dog is barking")
class bitch(animal):
    def eating(self):
        print("bitch is eating")
class puppy(dog,bitch):
    def cry(self):
        print("puppy is crying")
obj=puppy()
obj.cry()
obj.eating()
obj.bark()
obj.loyal()
