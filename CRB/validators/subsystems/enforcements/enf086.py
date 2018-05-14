from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import gender
from fraudcategory.subcategory import maritalstatus

class ENF086(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF086, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.M = maritalstatus.Marital()
        
    def validate_field(self, field):
        try:
            if(self.M.search_status(field)):
                return True
            else:
                return False 
        except:
            raise 

