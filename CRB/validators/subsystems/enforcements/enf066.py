from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import eitypes

class ENF066(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF066, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        
        self.EI = eitypes.EmployementInformation()
        
    def validate_field(self, field, credit):
        try:
            if(field.ei.EI_Employment_Type== "0" or field .ei.EI_Employment_Type == "1" or field.ei.EI_Employment_Type == "2"):
                if(credit.Applicant_Classification == "0"):
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

