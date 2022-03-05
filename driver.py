from job import job


class driver(job) :


    def __init__(self, lisenceID= 0, activeUntil= 0, vehicleType= 0):
        self.lisenceID = lisenceID
        self.activeUntil = activeUntil
        self.vehicleType = vehicleType
        
    def set_lisenceID(self, lisenceID):
        self.lisenceID = lisenceID    

    def set_activeUntil(self, activeUntil):
        self.activeUntil = activeUntil

    def set_vehicleType(self, vehicleType):
        self.vehicleType = vehicleType

    def get_lisenceID(self):
        return self.lisenceID

    def get_activeUntil(self):
        return self.activeUntil
    def get_vehicleType(self):
        return self.vehicleType    
    def print_info(self):
        print ("LISENCE ID : " + str(self.lisenceID)) 
        print ("ACTIVE UNTIL : " + str(self.activeUntil))
        print ("VEHICLE TYPE : " + self.vehicleType)  