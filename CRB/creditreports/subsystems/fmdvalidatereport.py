from validators.subsystems import fmdcode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 

class ReportFMDValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="FRA"):
        super(ReportFMDValidate, self).__init__()
        self._model = models.FINANCIAL_MALPRACTICE_DATA
        self.all_records = models.FINANCIAL_MALPRACTICE_DATA.objects.all()
        self.code = code
        self.pi_c_code = fmdcode.FMDCode(self._model, self.code)
        self.all_count = models.FINANCIAL_MALPRACTICE_DATA.objects.all().count()
        self.record_fields = 11
        self.set_code(self.pi_c_code)

    def begin_validation(self):
        try:
            self.all_field = self.pi_c_code.extract()
            self.examine_field(self.all_field)
        except:
            pass

    def check_data_in_field(self, f, rules):
        self.passed = { }
        self.all_records_passed = {}
        self.final_result={}
        
        try:
            self.validate_PI(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Client_Number(f, rules)
            self.Consumer_Classification(f, rules)
            self.Category_Code(f, rules)
            self.Sub_Category_Code(f, rules)
            self.Incident_Date(f, rules)
            self.Loss_Amount(f, rules)
            self.Currency_Type(f, rules)
            self.Incident_Details(f, rules)
            self.Forensic_Information_Available(f, rules)
        except Exception as e:
            pass 
        else:
            yield self.final_result 

    def check_dict_values(self, s):
        for value in s.values():
            return value.get("P")
            
    def get_keys(self, key_list):
        for k in key_list.keys():
            return k
            
    #VALIDATION FUNCTION BY FIELD
    def validate_PI(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "PI_Identification_Code"):
                self.pass_pi = []
                self.final_result = {}
                for r in rules:
                    if r == "M":
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                    else:
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata) == 6 or len(self.parseddata) == 8):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(self.parseddata)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_list = []
                self.passed_list.append(self.passed.get(keys).values().count(True))
                self.passed_by_id[keys]=self.passed_list
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Branch_Identification_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Branch_Identification_Code"):
                for r in rules:
                    if r == "M":
                        if(records.Branch_Identification_Code.branch_code):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)

                    else:
                        if(len(records.Branch_Identification_Code.branch_code) >= 3):
                            self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Branch_Identification_Code)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  

    #VALIDATION FUNCTION BY FIELD
    def Client_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Client_Number"):
                for r in rules:
                    if r == "C":
                        if(records.Borrowers_Client_Number.Client_Number):
                            self.passed[records.Borrowers_Client_Number.Client_Number]={"Conditional":True}
                        else:
                            self.passed[records.Borrowers_Client_Number.Client_Number]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=self.statuss.validate_field(records.Borrowers_Client_Number.Client_Number)

                    else:
                        if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                            self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Number.Client_Number)
                        else:
                            self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Consumer_Classification(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Consumer_Classification"):
                for r in rules:
                    if r == "C":
                        if(records.Consumer_Classification):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Consumer_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Consumer_Classification)

                    else:
                        if(len(records.Consumer_Classification) == 1):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Consumer_Classification)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  

    #VALIDATION FUNCTION BY FIELD
    def Category_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Category_Code"):
                for r in rules:
                    if r == "C":
                        if(records.Category_Code):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Category_Code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Category_Code)

                    else:
                        if(records.Category_Code):
                            if(len(records.Category_Code) == 2 or len(records.Category_Code) == 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Category_Code)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  

    #VALIDATION FUNCTION BY FIELD
    def Sub_Category_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Sub_Category_Code"):
                for r in rules:
                    if r == "C":
                        if(records.Sub_Category_Code):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Sub_Category_Code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Sub_Category_Code)

                    else:
                        if(records.Sub_Category_Code):
                            if(len(records.Sub_Category_Code) >= 2 or len(records.Sub_Category_Code) >= 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Sub_Category_Code)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  

    #VALIDATION FUNCTION BY FIELD
    def Incident_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Incident_Date"):
                for r in rules:
                    if r == "C":
                        if(records.Incident_Date):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                #print r.get(key)[1]
                                #print key
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Incident_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Incident_Date, records.Borrowers_Client_Number.Credit_Application_Date)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Incident_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Incident_Date)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Incident_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Incident_Date, priority=r.get(key))
                                
                                
                                self.validation_first = self.vstatus.validate_field(records.Incident_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Incident_Date)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                    else:
                        if(len(records.Incident_Date) >= 8):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Incident_Date)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  

    #VALIDATION FUNCTION BY FIELD
    def Loss_Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Loss_Amount"):
                for r in rules:
                    if r == "C":
                        if(records.Loss_Amount):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            #self.statuss = checkenforcements.check_enforcements(key, self._model, records.Sub_Category_Code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Loss_Amount)

                    else:
                        if(len(records.Loss_Amount) <= 21):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Loss_Amount)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Currency_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Currency_Type"):
                for r in rules:
                    if r == "C":
                        if(records.Currency_Type):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Currency_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Currency_Type)

                    else:
                        if(len(records.Currency_Type) == 3):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Currency_Type)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Incident_Details(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Incident_Details"):
                for r in rules:
                    if r == "C":
                        if(records.Incident_Details):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            #pass 
                            #self.statuss = checkenforcements.check_enforcements(key, self._model, records.Incident_Details, priority=r.get(key))
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Incident_Details, re_enfor=self.sec_enf)

                    else:
                        if(len(records.Incident_Details) <= 1000):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Incident_Details)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Forensic_Information_Available(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Forensic_Information_Available"):
                for r in rules:
                    if r == "C":
                        if(records.id):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Forensic_Information_Available, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Forensic_Information_Available)

                    else:
                        if(len(records.Forensic_Information_Available) == 1):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Forensic_Information_Available)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed         
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  

