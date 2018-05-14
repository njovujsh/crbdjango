from validators.subsystems.enforcements import enf001 

class ENF111(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF111, self).__init__(mobject, field, priority, action)
        
        self.status  = status 
        
    def validate_field(self, field, credit_field):
        try:
            if(credit_field.Applicant_Classification == "0"):
                if(field.II_Teacher_Registration_Number):
                    if(field.II_Country_Of_Issue == "UG"):
                        if(len(field.II_Teacher_Registration_Number) >= 4):
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
