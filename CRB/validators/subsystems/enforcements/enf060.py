from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import businesscode

class ENF060(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF060, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
        self.BS = businesscode.BussinessCode()
        
    def validate_field(self, field):
        try:
            if(self.BS.search_code(field)):
                return True
            else:
                return False
        except:
            raise 

