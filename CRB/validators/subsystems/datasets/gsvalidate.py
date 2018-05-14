from validators.subsystems import gscode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import validationstatus
from validators.subsystems.datasets import ibvalidate

#fields' attribute or the 'exclude' attribute is deprecated - form SecurityRulesForms needs updating
class GSValidate(ibvalidate.IBValidate):
    def __init__(self, code="GSCAFB"):
        super(GSValidate, self).__init__()
        self._model = models.GSCAFB_INFORMATION
        self.all_records = models.GSCAFB_INFORMATION.objects.all()
        self.code = code 
        self.pi_c_code = gscode.GSCAFBCode(self._model, self.code)
        
        self.all_records = models.CREDIT_APPLICATION.objects.all()
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }
        try:
            if(f == "GSCAFB_Business_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Business_Name):
                                self.passed[records.gscafb.GSCAFB_Business_Name]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Business_Name]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.gscafb.GSCAFB_Business_Name, priority=r.get(key))
                                self.passed[records.gscafb.GSCAFB_Business_Name]["ENF"]=self.statuss.validate_field(records.gscafb.GSCAFB_Business_Name, credit_app=records)
                        else:
                            if(len(records.gscafb.GSCAFB_Business_Name) <= 100):
                                self.passed[records.gscafb.GSCAFB_Business_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Business_Name)
                            else:
                                self.passed[records.gscafb.GSCAFB_Business_Name]["FORMAT"]=False
                yield self.passed  
                
            elif(f == "GSCAFB_Trading_Name"):
                self.pass_it = { }
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Trading_Name):
                                self.passed[records.gscafb.GSCAFB_Trading_Name]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Trading_Name]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.gscafb.GSCAFB_Trading_Name, priority=r.get(key))
                                self.passed[records.gscafb.GSCAFB_Trading_Name]["ENF"]=self.statuss.validate_field(records.gscafb.GSCAFB_Trading_Name, credit_app=records)

                        else:
                            if(len(records.gscafb.GSCAFB_Trading_Name) <= 100):
                                self.passed[records.gscafb.GSCAFB_Trading_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Trading_Name)
                            else:
                                self.passed[records.gscafb.GSCAFB_Trading_Name]["FORMAT"]=False
                yield self.passed 

            elif(f == "GSCAFB_Activity_Description"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Activity_Description):
                                self.passed[records.gscafb.GSCAFB_Activity_Description]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Activity_Description]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.gscafb.GSCAFB_Activity_Description, priority=r.get(key))
                                self.passed[records.gscafb.GSCAFB_Activity_Description]["ENF"]=self.statuss.validate_field(records.gscafb.GSCAFB_Activity_Description,credit_app=records)

                        else:
                            if(len(records.gscafb.GSCAFB_Activity_Description) <= 100):
                                self.passed[records.gscafb.GSCAFB_Activity_Description]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Activity_Description)
                            else:
                                self.passed[records.gscafb.GSCAFB_Activity_Description]["FORMAT"]=False
                yield self.passed 

            elif(f == "GSCAFB_Industry_Sector_Code"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Industry_Sector_Code):
                                self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Industry_Sector_Code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Industry_Sector_Code,credit_app=records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Industry_Sector_Code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Industry_Sector_Code)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Industry_Sector_Code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Industry_Sector_Code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Industry_Sector_Code)
                                    self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Industry_Sector_Code)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["ENF"]=False
                                   
                        else:
                            if(len(str(records.gscafb.GSCAFB_Industry_Sector_Code)) <= 5):
                                self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["FORMAT"]=checkformat.is_numeric(records.gscafb.GSCAFB_Industry_Sector_Code)
                            else:
                                self.passed[records.gscafb.GSCAFB_Industry_Sector_Code]["FORMAT"]=False
                print self.passed 
                yield self.passed 
                
            elif(f == "GSCAFB_Date_Registered"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Date_Registered):
                                self.passed[records.gscafb.GSCAFB_Date_Registered]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Date_Registered]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                
                                if(self.first_priority == 1 or self.first_priority == 2): 
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Date_Registered,records)
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Date_Registered, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.gscafb.GSCAFB_Date_Registered,records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False 
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Date_Registered,records)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Date_Registered,records)

                                        if(self.validation_first == True):
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.gscafb.GSCAFB_Date_Registered,records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.gscafb.GSCAFB_Date_Registered,records)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Date_Registered,records)

                                        if(self.validation_first == True):
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Date_Registered, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Date_Registered,records)
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False
                                else:
                                    self.passed[records.gscafb.GSCAFB_Date_Registered]["ENF"]=False

                        else:
                            if(records.gscafb.GSCAFB_Date_Registered):
                                self.gscafb_date = records.gscafb.GSCAFB_Date_Registered.replace("-", "", len(records.gscafb.GSCAFB_Date_Registered))
                                if(len(self.gscafb_date) >= 8):
                                    self.passed[records.gscafb.GSCAFB_Date_Registered]["FORMAT"]=checkformat.is_numeric(self.gscafb_date)
                                else:
                                    self.passed[records.gscafb.GSCAFB_Date_Registered]["FORMAT"]=False
                            else:
                                self.passed[records.gscafb.GSCAFB_Date_Registered]["FORMAT"]=False
                print self.passed 
                yield self.passed 
                
            elif(f == "GSCAFB_Business_Type_Code"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Business_Type_Code):
                                self.passed[records.gscafb.GSCAFB_Business_Type_Code]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Business_Type_Code]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Business_Type_Code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Business_Type_Code, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Business_Type_Code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Business_Type_Code)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Business_Type_Code]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Business_Type_Code]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Business_Type_Code]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Business_Type_Code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Business_Type_Code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Business_Type_Code)
                                    self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Business_Type_Code)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Business_Type_Code]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Business_Type_Code]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Business_Type_Code]["ENF"]=False
                                   
                        else:
                            if(records.gscafb.GSCAFB_Business_Type_Code):
                                if(len(str(records.gscafb.GSCAFB_Business_Type_Code)) <= 2):
                                    self.passed[records.gscafb.GSCAFB_Business_Type_Code]["FORMAT"]=checkformat.is_numeric(records.gscafb.GSCAFB_Business_Type_Code)
                                else:
                                    self.passed[records.gscafb.GSCAFB_Business_Type_Code]["FORMAT"]=False
                            else:
                                self.passed[str(records.gscafb.GSCAFB_Business_Type_Code)]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "GSCAFB_Surname"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Surname):
                                self.passed[records.gscafb.GSCAFB_Surname]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Surname]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.gscafb.GSCAFB_Surname, priority=r.get(key))
                                self.passed[records.gscafb.GSCAFB_Surname]["ENF"]=self.statuss.validate_field(records.gscafb.GSCAFB_Surname, records)

                        else:
                            if(len(records.gscafb.GSCAFB_Surname) <= 30):
                                self.passed[records.gscafb.GSCAFB_Surname]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Surname)
                            else:
                                self.passed[records.gscafb.GSCAFB_Surname]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "GSCAFB_Forename1"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Forename1):
                                self.passed[records.gscafb.GSCAFB_Forename1]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Forename1]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.gscafb.GSCAFB_Forename1, priority=r.get(key))
                                self.passed[records.gscafb.GSCAFB_Forename1]["ENF"]=self.statuss.validate_field(records.gscafb.GSCAFB_Forename1, records)

                        else:
                            if(len(records.gscafb.GSCAFB_Forename1) <= 30):
                                self.passed[records.gscafb.GSCAFB_Forename1]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Forename1)
                            else:
                                self.passed[records.gscafb.GSCAFB_Forename1]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "GSCAFB_Forename2"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.gscafb.GSCAFB_Forename2):
                                self.passed[records.gscafb.GSCAFB_Forename2]={"Optional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Forename2]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                                #self.statuss = checkenforcements.check_enforcements(key, self._model, records.GSCAFB_Forename1, priority=r.get(key))
                            self.passed[records.gscafb.GSCAFB_Forename2]["ENF"]= True #self.statuss.validate_field(records.GSCAFB_Forename1)

                        else:
                            if(len(records.gscafb.GSCAFB_Forename2) <= 30):
                                self.passed[records.gscafb.GSCAFB_Forename2]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Forename2)
                            else:
                                self.passed[records.gscafb.GSCAFB_Forename2]["FORMAT"]=TRue
                yield self.passed 
                
            elif(f == "GSCAFB_Forename3"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.gscafb.GSCAFB_Forename3):
                                self.passed[records.gscafb.GSCAFB_Forename3]={"Optional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Forename3]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                                #self.statuss = checkenforcements.check_enforcements(key, self._model, records.GSCAFB_Forename1, priority=r.get(key))
                            self.passed[records.gscafb.GSCAFB_Forename3]["ENF"]= True #self.statuss.validate_field(records.GSCAFB_Forename1)

                        else:
                            if(len(records.gscafb.GSCAFB_Forename3) <= 30):
                                self.passed[records.gscafb.GSCAFB_Forename3]["FORMAT"]=checkformat.sub_alphanumeric(records.gscafb.GSCAFB_Forename3)
                            else:
                                self.passed[records.gscafb.GSCAFB_Forename3]["FORMAT"]=True
                yield self.passed 
                
            elif(f == "GSCAFB_Gender"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Gender):
                                self.passed[records.gscafb.GSCAFB_Gender]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Gender]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Gender, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Gender, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Gender, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Gender)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Gender]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Gender]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Gender]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Gender, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Gender, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Gender)
                                    self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Gender, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Gender]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Gender]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Gender]["ENF"]=False
                                   
                        else:
                            if(records.gscafb.GSCAFB_Gender):
                                if(len(str(records.gscafb.GSCAFB_Gender)) == 1):
                                    self.passed[records.gscafb.GSCAFB_Gender]["FORMAT"]=checkformat.is_numeric(records.gscafb.GSCAFB_Gender)
                                else:
                                    self.passed[records.gscafb.GSCAFB_Gender]["FORMAT"]=False
                            else:
                                self.passed[str(records.gscafb.GSCAFB_Gender)]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "GSCAFB_Marital_Status"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Marital_Status):
                                self.passed[records.gscafb.GSCAFB_Marital_Status]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Marital_Status]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Marital_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Marital_Status, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Marital_Status, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Marital_Status)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Marital_Status]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Marital_Status]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Marital_Status]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Marital_Status, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Marital_Status, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Marital_Status)
                                    self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Marital_Status, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Marital_Status]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Marital_Status]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Marital_Status]["ENF"]=False
                                   
                        else:
                            if(records.gscafb.GSCAFB_Marital_Status):
                                if(len(str(records.gscafb.GSCAFB_Marital_Status)) >= 1):
                                    self.passed[records.gscafb.GSCAFB_Marital_Status]["FORMAT"]=checkformat.is_numeric(records.gscafb.GSCAFB_Marital_Status)
                                else:
                                    self.passed[records.gscafb.GSCAFB_Marital_Status]["FORMAT"]=False
                            else:
                                self.passed[str(records.gscafb.GSCAFB_Marital_Status)]["FORMAT"]=False
                print self.passed 
                yield self.passed 
                
            elif(f == "GSCAFB_Date_of_Birth"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.gscafb.GSCAFB_Date_of_Birth):
                                self.passed[records.gscafb.GSCAFB_Date_of_Birth]={"Conditional":True}
                            else:
                                self.passed[records.gscafb.GSCAFB_Date_of_Birth]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                
                                if(self.first_priority == 1 or self.first_priority == 2): 
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Date_of_Birth, records)
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Date_of_Birth, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.gscafb.GSCAFB_Date_of_Birth)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False 
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Date_Registered)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Date_of_Birth)

                                        if(self.validation_first == True):
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.gscafb.GSCAFB_Date_of_Birth)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.GSCAFB_Date_of_Birth)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.gscafb.GSCAFB_Date_of_Birth)

                                        if(self.validation_first == True):
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=True 
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.gscafb.GSCAFB_Date_of_Birth, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.gscafb.GSCAFB_Date_of_Birth)
                                        if(self.validation_second == True):
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=True
                                        else:
                                            self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                    else:
                                        self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                                else:
                                    self.passed[records.gscafb.GSCAFB_Date_of_Birth]["ENF"]=False
                        else:
                            if(records.gscafb.GSCAFB_Date_of_Birth):
                                if(len(str(records.gscafb.GSCAFB_Date_of_Birth)) >= 6):
                                    self.gscafb_date = str(records.gscafb.GSCAFB_Date_of_Birth).replace("-", "", 40)
                                    self.passed[records.gscafb.GSCAFB_Date_of_Birth]["FORMAT"]=checkformat.is_numeric(int(self.gscafb_date))
                                else:
                                    self.passed[records.gscafb.GSCAFB_Date_of_Birth]["FORMAT"]=False
                            else:
                                self.passed[records.gscafb.GSCAFB_Date_of_Birth]["FORMAT"]=False
                yield self.passed
        except Exception as e:
            print e
            pass  
