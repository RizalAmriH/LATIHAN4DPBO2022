from person import person


class job(person): 

    def __init__(self, NIP= 0, companyName= 0, position= 0,):
        self.NIP = NIP
        self.companyName = companyName
        self.position = position
        
    def set_NIP(self, NIP):
        self.NIP = NIP    

    def set_companyName(self, companyName):
        self.companyName = companyName

    def set_position(self, position):
        self.position = position

    def get_NIP(self):
        return self.NIP

    def get_companyName(self):
        return self.companyName
    def get_position(self):
        return self.position    
    def print_info(self):
        print ("NIP : "+ str(self.NIP)) 
        print ("COMPANY : " + self.companyName)
        print ("POSITION : " + self.position)  

