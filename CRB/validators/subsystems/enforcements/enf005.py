from validators.subsystems.enforcements import enf001 

class ENF005(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF005, self).__init__(mobject, field, priority, action)
        self.enfo = "ENF005"
        
    def validate_field(self, closure_field, credit_field):
        try:
            if(closure_field.replace("-", "", len('20')) > credit_field.Credit_Application_Date.replace("/", "", len('20'))):
                return True
            else:
                return False 
        except:
            raise 
            
    def validate_field_cba(self, closure_field, credit_field):
        try:
            if(closure_field.replace("/", "", len('20')) > credit_field.Credit_Account_Type.replace("/", "", len('20'))):
                return True
            else:
                return False 
        except:
            raise 
