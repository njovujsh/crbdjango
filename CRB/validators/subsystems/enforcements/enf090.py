from validators.subsystems.enforcements import enf001 

class ENF090(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF090, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.fcs = None 
        
    def validate_field(self, field, records, filename=None):
        try:
            if(filename):
                if(filename == "CBA"):
                    if(records.Credit_Application_Date > "10052011"):
                        if(field):
                            return True 
                        else:
                            return False 
                    else:
                        return True
                else:
                    return True 
            else:
                return True 
        except:
            raise 



