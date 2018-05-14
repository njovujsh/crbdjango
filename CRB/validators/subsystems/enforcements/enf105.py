from validators.subsystems.enforcements import enf001 

class ENF105(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF105, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
    def validate_field(self, field):
        try:
            if(field.Applicant_Classification == "0"):
                if(field.idi.II_Nationality):
                    return True 
                else:
                    return False 
            else:
                return True 
        except:
            raise 
