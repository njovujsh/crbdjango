from validators.subsystems.enforcements import enf001 

class ENF065(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF065, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field, re_enfor=None):
        try:
            if(field):
                return True
            else:
                return False
        except:
            raise 




