from validators.subsystems.enforcements import enf001 

class ENF006(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF006, self).__init__(mobject, field, priority, action)

        self.enfo = "ENF006"
        
    def validate_field(self, closure_field, records=None):
        try:
            if(closure_field > records.Credit_Account_Date):
                return True
            else:
                return False 
        except:
            raise 
