from validators.subsystems.enforcements import enf001 

class ENF098(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF098, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.fcs = None 
        
    def validate_field(self, field, records):
        try:
            if(records.Applicant_Classification == "0"):
                if(records.idi.II_Passport_Number):
                    if(len(field) >= 4):
                        return True
                    else:
                        return False 
                else:
                    return True 
            else:
                return True 
        except:
            raise 



