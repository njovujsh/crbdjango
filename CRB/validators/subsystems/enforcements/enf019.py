from validators.subsystems.enforcements import enf001 

class ENF019(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF019, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        self.must_not_be_empty = False 
        
    def validate_field(self, field):
        try:
            if(field.Number_of_Days_in_Arrears and field.Credit_Account_Arrears_Date and field.Balance_Overdue):
                if(field.Balance_Overdue_Indicator):
                    return True
                else:
                    return False 
            else:
                return True
        except:
            raise 
    
    def get_empty_status(self):
        return self.must_not_be_empty
