from validators.subsystems.enforcements import enf001 

class ENF095(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF095, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field_ii, records):
        try:
            if(str(records.Applicant_Classification) == "1"):
                if(records.idi.II_Registration_Certificate_Number):
                    if(records.idi.II_Country_Issuing_Authority == "UG"):
                        if(str(field_ii) >= 4):
                            return True 
                        else:
                            return False 
                    else:
                        return True 
                else:
                    return True  
            else:
                return True 
        except:
            raise 
