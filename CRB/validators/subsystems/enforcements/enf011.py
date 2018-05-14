from validators.subsystems.enforcements import enf001 

class ENF011(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF011, self).__init__(mobject, field, priority, action)
        
        self.status = status 
        
    def validate_field(self):
        try:
            if(self.get_field().Credit_Account_Date > self.get_field().Date_of_First_Payment):
                self.validation_result["Credit_Account_Date"]=False 
            else:
                self.validation_result["Credit_Account_Date"]=True
        except:
            raise 
