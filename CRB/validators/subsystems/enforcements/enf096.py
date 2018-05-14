from validators.subsystems.enforcements import enf001 

class ENF096(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF096, self).__init__(mobject, field, priority, action)
        self.status = None 
        
    def validate_field(self, field_ii, records):
        try:
            if(records.idi.II_Tax_Identification_Number):
                if(records.idi.II_Country_Of_Issue == "UG"):
                    if(len(field_ii) >= 8):
                        return True 
                else:
                    return True  
            else:
                return True 
        except:
            raise 

