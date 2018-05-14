from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import propertyowner

class ENF084(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF084, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        self.propert_y = propertyowner.PropertyOwner()
        
    def validate_field(self, field):
        try:
            if(self.propert_y.get_p_dict(field.strip().lstrip().rstrip())):
                return True
            else:
                return False 
        except:
            raise 




