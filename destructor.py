class A:
    def __init__(self):
        print("constructor")
    def function(self):
        print("function")
    def __del__(self):
        print("destructor")
obj=A()
del obj
#obj.function()  <---- used to see our destructor work or not if yes
                      #then obj is not defined error will show
