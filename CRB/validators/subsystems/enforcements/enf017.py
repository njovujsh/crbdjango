from validators.subsystems.enforcements import enf001 


class ENF017(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF017, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field , records=None):
        try:
            if(records.Credit_Account_Arrears_Date or records.Balance_Overdue):
                if(len(field)):
                    return True
                else:
                    return False
            else:
                return True 
        except:
            raise 
