from validators.subsystems.enforcements import enf001 

class ENF018(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF018, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field,  records):
        try:
            if(records.Credit_Account_Arrears_Date or records.Number_of_Days_in_Arrears):
                if field:
                    return True
                else:
                    return False 
            else:
                return True 
        except:
            raise 
