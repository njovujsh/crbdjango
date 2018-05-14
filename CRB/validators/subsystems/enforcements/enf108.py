from validators.subsystems.enforcements import enf001 

class ENF108(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF108, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
    def validate_field(self, field,records):
        try:
            if(records.Applicant_Classification == "0"):
                if(records.idi.II_KACITA_License_Number):
                    if(records.idi.II_Country_Of_Issue == "UG"):
                        if(len(field) >= 4):
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
