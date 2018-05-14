from validators.subsystems.enforcements import enf001 
from fraudcategory.subcategory import salarayband
from fraudcategory.subcategory import industrycode

class ENF048(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF048, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.salary = salarayband.SalaryBand()
        
    def validate_field(self, field):
        try:
            if(field):
                return True
            else:
                return False 
        except:
            raise 

