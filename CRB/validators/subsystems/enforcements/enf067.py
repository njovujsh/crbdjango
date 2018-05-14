from validators.subsystems.enforcements import enf001 

class ENF067(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF067, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
    def validate_field(self, field, records):
        try:
            if(records.Applicant_Classification == "0"):
                if(field):
                    return True
                else:
                    return False  
            else:
                return True 
        except:
            raise 

