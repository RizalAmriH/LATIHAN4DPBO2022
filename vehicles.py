class vehicle :
 
    def __init__(self, fuelType= 0, maxPassenger= 0):
        self.fuelType = fuelType
        self.maxPassenger = maxPassenger
        
    def set_fuelType(self, fuelType):
        self.fuelType = fuelType    

    def set_maxPassenger(self, maxPassenger):
        self.maxPassenger = maxPassenger

    def get_fuelType(self):
        return self.fuelType

    def get_maxPassenger(self):
        return self.maxPassenger
    def isMove(self):
        print("vechile is moving")   
   
        