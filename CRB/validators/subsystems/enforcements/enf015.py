from validators.subsystems.enforcements import enf001 


class ENF015(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF015, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field, records=None):
        try:
            if(records):
                if(str(records.Flag_for_Restructured_Credit) == '0'):
                    if(len(str(field))):
                        return True
                    else:
                        return False 
                else:
                    return True
            else:
                return False 
        except:
            raise 
