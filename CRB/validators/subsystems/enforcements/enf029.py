from validators.subsystems.enforcements import enf001 


class ENF029(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF029, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        self.types = [4,7,9]
        
    def validate_field(self, field, more_validation=None):
        try:
            if(more_validation):
                if(more_validation.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type in self.types):
                    if(field != ""):
                        return True
                    else:
                        return False 
                else:
                    return True 
            else:
                if(field != ""):
                    return True
                else:
                    return False  
        except:
            raise 

    def other_fields(self, field, *varss):
        """
        """
        if(field in varss):
            return True
        else:
            return False 
            
        

