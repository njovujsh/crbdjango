from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import maritalstatus

class ENF055(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF055, self).__init__(mobject, field, priority, action)
        
        self.status  = maritalstatus.Marital() 
        
    def validate_field(self, field):
        try:
            if(self.status.search_status(field)):
                return True
            else:
                return False 
        except:
            raise 

