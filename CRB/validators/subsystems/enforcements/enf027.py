from validators.subsystems.enforcements import enf001 

class ENF027(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF027, self).__init__(mobject, field, priority, action)
        
        self.status  = None 
        self.fcs = None 
        
    def validate_field(self, field, records, r_identifier=None):
        try:
            if(r_identifier):
                if(filename == "CAP"):
                    if(records.Credit_Application_Date >= "10052011"):
                        if(field):
                            return True 
                        else:
                            return False 
                    else:
                        return True
                        
                elif(filename == "CBA"):
                    if(records.Borrowers_Client_Number.Credit_Application_Date >= "10052011"):
                        if(field):
                            return True 
                        else:
                            return False 
                    else:
                        return True
                else:
                    return False
            else:
                return True  
        except:
            raise 


