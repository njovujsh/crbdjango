from validators.subsystems.enforcements import enf001 



class ENF009(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF009, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field):
        try:
            if(field.Credit_Account_Status == "5"):
                if(field.Credit_Account_Arrears_Date):
                    return True
                else:
                    return False 
            else:
                return True  
        except:
            raise 
            
