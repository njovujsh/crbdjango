from validators.subsystems import ibcode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 
from branchcode import models as branchmodels

class ReportIBValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="IB"):
        super(ReportIBValidate, self).__init__()
        self._model = models.INSTITUTION_BRANCH
        self.all_records = models.INSTITUTION_BRANCH.objects.all()
        self.all_count = models.INSTITUTION_BRANCH.objects.all().count()
        self.code = code
        self.pi_c_code = ibcode.IBCode(self._model, self.code)
        self.record_fields = 5

        #Set the code of model/datasets to be used
        self.set_code(self.pi_c_code)
        self.dict_list = []
        self.passed_by_id = {}
        self.real_passed = {}
        
        self.headers = branchmodels.RequiredHeader.objects.all()
        
    def begin_validation(self):
        try:
            self.all_field = self.pi_c_code.extract()
            self.examine_field(self.all_field)
        except:
            pass

    def check_data_in_field(self, f, rules):
        self.passed = {}
        self.all_records_passed = {}
        self.final_result={}
        try:
            self.validate_PI(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Branch_Name(f, rules)
            self.Branch_Type(f, rules)
            self.Date_Opened(f, rules)
        except Exception as e:
            # Log 
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
                        if(len(records.Branch_Identification_Code.branch_code) <= 15):
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
    def Branch_Name(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Branch_Name"):
                for r in rules:
                    if r == "M":
                        if(records.Branch_Name):
                            self.passed[records.Branch_Name]={"Mandatory":True}
                        else:
                            self.passed[records.Branch_Name]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Name, priority=r.get(key))
                            self.passed[records.Branch_Name]["ENF"]=self.statuss.validate_field(records.Branch_Name)
                    else:
                        if(len(records.Branch_Name) <= 100):
                            self.passed[records.Branch_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.Branch_Name)
                        else:
                            self.passed[records.Branch_Name]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                if(self.passed_by_id.get(keys)):
                    self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                else:
                    pass 
                    #elf.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Branch_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Branch_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Branch_Type):
                            self.passed[records.Branch_Type]={"Mandatory":True}
                        else:
                            self.passed[records.Branch_Type]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Type, priority=r.get(key))
                            self.passed[records.Branch_Type]["ENF"]=self.statuss.validate_field(records.Branch_Type)

                    else:
                        if(len(records.Branch_Type) == 1):
                            self.passed[records.Branch_Type]["FORMAT"]=checkformat.sub_alphanumeric(records.Branch_Type)
                        else:
                            self.passed[records.Branch_Type]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                if(self.passed_by_id.get(keys)):
                    self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                else:
                    pass 
        else:
            pass  
            
    #VALIDATION FUNCTION BY FIELD
    def Date_Opened(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Date_Opened"):
                for r in rules:
                    if r == "M":
                        if(records.Date_Opened):
                            self.passed[records.Date_Opened]={"Mandatory":True}
                        else:
                            self.passed[records.Date_Opened]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_Opened, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Date_Opened)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_Opened, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Date_Opened)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.Date_Opened]["ENF"]=True 
                                    else:
                                        self.passed[records.Date_Opened]["ENF"]=False
                                else:
                                    self.passed[records.Date_Opened]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_Opened, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_Opened, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Date_Opened)
                                self.validation_second = self.sec_enf.validate_field(records.Date_Opened, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.Date_Opened]["ENF"]=True
                                    else:
                                        self.passed[records.Date_Opened]["ENF"]=False
                                else:
                                    self.passed[records.Date_Opened]["ENF"]=False

                    else:
                        if(len(records.Date_Opened.replace("-", "", 12)) == 8):
                            self.passed[records.Date_Opened]["FORMAT"]=checkformat.is_numeric(records.Date_Opened.replace("-", "",12))
                        else:
                            self.passed[records.Date_Opened]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                if(self.passed_by_id.get(keys)): 
                    self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                else:
                    self.passed_by_id.get(keys)
        else:
            pass  
