from validators.subsystems.enforcements import enf001 
from validators.subsystems import startswithnum 

class ENF068(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF068, self).__init__(mobject, field, priority, action)
        
        self.status = False 
        
    def validate_field(self, value):
        try:
            if(str(value)):
                if(startswithnum.startswith_alpha(value) and startswithnum.endswith_number(value)):
                    #print "Starts and ends with required char"
                    return True 
                else:
                    return False 
            else:
                return None 
        except:
            raise 
