from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import eitypes

class ENF085(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF085, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
        self.EI = eitypes.EmployementInformation()
        
    def validate_field(self, field):
        try:
            if(self.EI.search_value(field)):
                return True 
            else:
                return False 
        except:
            raise 

