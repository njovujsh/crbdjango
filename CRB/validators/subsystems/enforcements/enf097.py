from validators.subsystems.enforcements import enf001 

class ENF097(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF097, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field, records):
        try:
            if(str(records.Applicant_Classification) == "0"):
                if(records.idi.II_Value_Added_Tax_Number):
                    if(records.idi.II_Country_Issuing_Authority == "UG"):
                        if(str(field) >= 7):
                            return True 
                        else:
                            return False 
                    else:
                        return True 
                else:
                    return False  
            else:
                return True 
        except:
            raise 
