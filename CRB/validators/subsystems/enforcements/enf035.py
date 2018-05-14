from validators.subsystems.enforcements import enf001 

class ENF035(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF035, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
    def validate_field(self, field, credit_field):
        try:
            if(credit_field.Applicant_Classification == "0"):
                if(field):
                    return True 
                else:
                    return False 
            else:
                return True 
        except:
            raise 

