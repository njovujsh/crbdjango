from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import salarayband

class ENF059(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF059, self).__init__(mobject, field, priority, action)
        
        self.status  = None  
        self.salary = salarayband.SalaryBand()
        
    def validate_field(self, field):
        try:
            if(self.salary.search_salary(field)):
                return True
            else:
                return False 
        except:
            raise 

