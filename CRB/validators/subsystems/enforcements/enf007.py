from validators.subsystems.enforcements import enf001 
from validators.subsystems.enforcements import enf014

class ENF007(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF007, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field, records=None):
        try:
            self.date = str(field).replace("-", "", len(field))
            if(len(self.date.replace(" ", "", len(self.date))) <= 8):
                return True
            else:
                return False  
        except:
            raise 

