class animal:
    def loyal(self):
        print("animals are loyal")
class dog(animal):
    def bark(self):
        print("Dog is barking")
class puppy(animal):
    def cry(self):
        print("puppy is crying")
obj=puppy()
obj.loyal()
obj.cry()
obj1=dog()
obj1.bark()

