from validators.subsystems.enforcements import enf001 


class ENF030(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF030, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field, records=None):
        try:
            if(records):
                if(records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type == "6" or records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type == "10" or records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type == "11"):
                    if(field):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False 
        except:
            raise 

    def other_fields(self, field, var1, var2, var3):
        """
        """
        if(field == var1 or field == var2 or field == var3):
            return True
        else:
            return False 
            
        
