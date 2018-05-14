from validators.subsystems.enforcements import enf001 


class ENF010(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF010, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field):
        try:
            if(field.Last_Payment_Amount != 0):
                if(field.Last_Payment_Date):
                    return True
                else:
                    return False 
            else:
                return True  
        except:
            raise 
