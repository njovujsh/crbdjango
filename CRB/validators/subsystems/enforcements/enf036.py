from validators.subsystems.enforcements import enf001 

class ENF036(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF036, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
        self.country_code = "UG"
        
    def validate_field(self, field, records=None):
        try:
            if(records):
                if(records == self.country_code):
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



