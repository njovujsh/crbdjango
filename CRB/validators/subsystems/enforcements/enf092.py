from validators.subsystems.enforcements import enf001 

class ENF092(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF092, self).__init__(mobject, field, priority, action)
        self.status = None 
        
    def validate_field(self, field, records):
        try:
            if(records.Applicant_Classification == "0"):
                return True
            else:
                if(records.idi.II_Voters_PERNO or records.idi.II_Tax_Identification_Number or records.idi.II_Value_Added_Tax_Number or records.idi.II_FCS_Number or records.idi.II_Passport_Number or records.idi.II_Drivers_Licence_ID_Number or records.idi.II_Drivers_License_Permit_Number or records.idi.II_NSSF_Number or records.idi.II_Police_ID_Number or records.idi.II_UPDF_Number or records.idi.II_Public_Service_Pension_Number):
                    return True
                else:
                    if(field):
                        return True 
                    else:
                        return False  
        except:
            raise 

