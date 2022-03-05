from vehicles import vehicle


class plane(vehicle): 
 
    def __init__(self, age= 0, type= 0, wingLength= 0):
        self.age = age
        self.type = type
        self.wingLength = wingLength
        
    def set_age(self, age):
        self.age = age    

    def set_type(self, type):
        self.type = type

    def set_wingLength(self,wingLength):
        self.wingLength =wingLength

    def get_age(self):
        return self.age

    def get_type(self):
        return self.type
    def get_wingLength(self):
        return self.wingLength

    def print_info(self):
        print ("AGE(years) : " + str(self.age)) 
        print ("TYPE : " + self.type)
        print ("WING LENGTH(meter) : " +str(self.wingLength))  
