from validators.subsystems.enforcements import enf001 


class ENF008(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF008, self).__init__(mobject, field, priority, action)
        self.status = None 
        
    def validate_field(self, field):
        try:
            if(field.Credit_Account_Date > field.Date_of_First_Payment):
                if(field.Last_Payment_Amount):
                    return True
                else:
                    return False 
            else:
                return True 
        except:
            raise 
            
    def validate_otherfields(self, mobject):
        for values in mobject:
            if(values.Last_Payment_Amount):
                return True
            else:
                return False 

