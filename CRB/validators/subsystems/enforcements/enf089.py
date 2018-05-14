from validators.subsystems.enforcements import enf001 

class ENF089(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF089, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.fcs = None 
        
    def validate_field(self, field, records, filename=None):
        try:
            if(filename):
                if(filename == "CAP"):
                    if(records.idi.II_FCS_Number):
                       return True 
                    else:
                        return False 
                else:
                    return True
            else:
                return True
        except:
            raise 



