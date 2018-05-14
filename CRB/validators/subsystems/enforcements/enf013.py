from validators.subsystems.enforcements import enf001 

class ENF013(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF013, self).__init__(mobject, field, priority, action)
        
        self.subdate = None
        
    def validate_field(self, field, records):
        try:
            if(field != records):
                return True
            else:
                return False 
        except:
            raise 
