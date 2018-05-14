from validators.subsystems.enforcements import enf001 

class ENF104(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF104, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
    def validate_field(self, field, records):
        try:
            if(records.Applicant_Classification == "0"):
                if(records.idi.II_Registration_Certificate_Number or records.idi.II_Value_Added_Tax_Number == "UG"):
                    if(field):
                        return True 
                    else:
                        return False 
                else:
                    return True 
            else:
                return True 
        except:
            raise 
