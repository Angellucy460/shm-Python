#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd
class Human():

    def __init__(self):
        print("The initializer wass called")

    def another_one(self):
        print("This is another method")
    
adam=Human() #object from a class
# adam.__init__()
#adam.__init__()
# adam.another_one()