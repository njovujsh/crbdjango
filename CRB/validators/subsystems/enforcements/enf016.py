from validators.subsystems.enforcements import enf001 


class ENF016(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(EN016, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self):
        try:
            if(self.get_field().EI_Employment_Type == 0):
                self.validation_result["EI_Employment_Type"]=False
            else:
                self.validation_result["EI_Employment_Type"]=True
        except:
            raise 
