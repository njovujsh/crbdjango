from validators.subsystems.enforcements import enf001 
from fraudcategory.subsystems import allmodules

class ENF051(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF051, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field):
        try:
            if(self.load_module_by_id(field)):
                return True
            else:
                return False 
        except:
            raise 
    
    def load_module_by_id(self, ID):
        try:
            if(ID):
                try:
                    return allmodules.get_module_by_id(int(ID))
                except:
                    raise 
            else:
                return False 
        except:
            raise 

