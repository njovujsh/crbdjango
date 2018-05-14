from validators.subsystems.enforcements import enf001 


class ENF004(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF004, self).__init__(mobject, field, priority, action)
        
        self.status = False 
        
    def validate_field(self, records):
        try:
            if(records.Balance_Overdue):
                if(records.Credit_Account_Status == "4" or records.Credit_Account_Status == "5" or records.Credit_Account_Status=="6"):
                    return False
                else:
                    return True 
            else:
                return True 
        except:
            raise 
            
    def validate_otherfields(self, mobject):
        for values in mobject:
            if(values.Credit_Account_Status == 4 or values.Credit_Account_Status== 5 or values.Credit_Account_Status==6):
                return False
            else:
                return True
