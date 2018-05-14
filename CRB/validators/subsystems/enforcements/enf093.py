from validators.subsystems.enforcements import enf001 

class ENF093(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF093, self).__init__(mobject, field, priority, action)
        self.status = None 
        
    def validate_field(self, field, record):
        try:
            if(record.Applicant_Classification == "0"):
                return True
            else:
                if(record.idi.II_Registration_Certificate_Number or record.idi.II_Tax_Identification_Number or record.idi.II_Value_Added_Tax_Number or record.idi.II_FCS_Number or record.idi.II_KACITA_License_Number):
                    return True
                else:
                    if(field):
                        return True
                    else:
                        return False  
        except:
            raise 
