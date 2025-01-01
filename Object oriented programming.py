# Object oriented programming 

# class Car :
#    pass       # this just allows as to leave it if we want to use it later 

class Car :
    
    def __init__(self,make,model,year,color) :        # This is a constructor and it is used to construct the object that we will use for us 
        self.make = make              # the left are the atributes of the object car in the program 
        self.model = model
        self.year =year
        self.color = color
    
    
    def drive(self) :           # the left are the methods of the object car , which is the cless of the program 
        print ("This car is driving")
        
    def stop() :
        print ("This car has stopped ")
        
    

