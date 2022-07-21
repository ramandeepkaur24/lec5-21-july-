class animal:
    def loyal(self):
        print("animals are loyal")
class dog:
    def bark(self):
        print("Dog is barking")
class puppy(dog,animal):
    def cry(self):
        print("puppy is crying")
obj=puppy()
obj.loyal()
obj.bark()
obj.cry()
