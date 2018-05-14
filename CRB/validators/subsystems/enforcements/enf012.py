from validators.subsystems.enforcements import enf001 


class ENF012(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF012, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.fcs = None 
        
    def validate_field(self, field):
        try:
            if(field.idi.II_FCS_Number):
                return True
            else:
                return False 
        except:
            raise 
