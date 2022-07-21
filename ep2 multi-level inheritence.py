class animal:
    def loyal(self):
        print("animals are loyal")
class dog(animal):
    def bark(self):
        print("Dog is barking")
class puppy(dog):
    def cry(self):
        print("puppy is crying")
obj=puppy()
obj.loyal()
obj.bark()
obj.cry()
