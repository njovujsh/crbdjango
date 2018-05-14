from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import salarayband

class ENF026(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF026, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.salary = salarayband.SalaryBand()
        
    def validate_field(self, field, credit_app):
        try:
            if(credit_app.Applicant_Classification == "1"):
                if(field):
                    return True 
                else:
                    return False 
            else:
                return True 
        except:
            raise 

