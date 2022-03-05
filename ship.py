from vehicles import vehicle


class ship(vehicle): 
 
    def __init__(self, age= 0, type= 0, country= 0):
        self.age = age
        self.type = type
        self.country = country
        
    def set_age(self, age):
        self.age = age    

    def set_type(self, type):
        self.type = type

    def set_country(self, country):
        self.country = country

    def get_age(self):
        return self.age

    def get_type(self):
        return self.type
    def get_country(self):
        return self.country    
    def print_info(self):
        print ("AGE(years) : " + str(self.age)) 
        print ("TYPE : " + self.type)
        print ("COUNTRY OF MANUFACTURES : " +str(self.country))       