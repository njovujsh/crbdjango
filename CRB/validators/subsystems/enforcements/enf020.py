from validators.subsystems.enforcements import enf001 

class ENF020(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF020, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, status):
        try:
            if(status.Credit_Account_Status =='4' or  status.Credit_Account_Status == '5'):
                if(status.Credit_Account_Closure_Date):
                    return True
                else:
                    return False 
            else:
                return True 
        except:
            raise 


