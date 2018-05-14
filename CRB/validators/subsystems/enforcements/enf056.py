from validators.subsystems.enforcements import enf001 

class ENF056(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF056, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field):
        try:
            if(field):
                return True
            else:
                return False
        except:
            raise 





