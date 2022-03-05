class person :


    def __init__(self, NIK= 0, name=0, gender=0):
        self.NIK = NIK
        self.name = name
        self.gender = gender
        
    def set_NIK(self, NIK):
        self.NIK = NIK    

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def get_NIK(self):
        return self.NIK
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.gender

    def isSleeping(self, name):
        print("{name} is sleeping".format(name=name)) 
    def print_info(self):
        print (self.NIK) 
        print (self.name)
        print (self.gender)          

