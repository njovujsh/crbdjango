from validators.subsystems import bscode 
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from branchcode import models as branchcodemodels

class BSValidate(ibvalidate.IBValidate):
    def __init__(self, code="BS"):
        super(BSValidate, self).__init__(code=code)
        self._model = models.BORROWERSTAKEHOLDER
        self.all_records  = self.filter_new_old_records(models.BORROWERSTAKEHOLDER)
        self.headers = branchcodemodels.RequiredHeader.objects.all()
        self.code = code 
        self.pi_c_code = bscode.BSCode(self._model, self.code)
        
        self.set_code(self.pi_c_code)
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }

        try:
            if(f == "PI_Identification_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.PI_Identification_Code.pi_identification_code):
                                self.passed[records.PI_Identification_Code.pi_identification_code]={"Mandatory":True}
                            else:
                                self.passed[records.PI_Identification_Code.pi_identification_code]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=True 
                                        else:
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False
                                    else:
                                        self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                    self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=True
                                        else:
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False
                                    else:
                                        self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False 
                        else:
                            if(records.PI_Identification_Code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                                if(len(self.parseddata) <= 8):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code.pi_identification_code)]["FORMAT"]=False
                yield self.passed 

            elif(f == "Branch_Identification_Code"):
                self.pass_it = { }
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Branch_Identification_Code.branch_code):
                                self.passed[records.Branch_Identification_Code.branch_code]={"Mandatory":True}
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=True 
                                        else:
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                    self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=True
                                        else:
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False
                                    else:
                                        self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False 

                        else:
                            if(len(records.Branch_Identification_Code.branch_code) <= 15):
                                if(str(records.Branch_Identification_Code.branch_code).strip().lstrip().rstrip()):
                                    self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=checkformat.is_numeric(records.Branch_Identification_Code.branch_code)
                                else:
                                    self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                yield self.passed 

            elif(f == "Borrowers_Client_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Borrowers_Client_Number.Client_Number):
                                self.passed[records.Borrowers_Client_Number.Client_Number]={"Mandatory":True}
                            else:
                                self.passed[records.Borrowers_Client_Number.Client_Number]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Borrowers_Client_Number.Client_Number)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False 
                                    else:
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Borrowers_Client_Number.Client_Number)
                                    self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=True
                                        else:
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False
                                    else:
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False 

                        else:
                            if(records):
                                if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                                    self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Number)
                                else:
                                    self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                            else:
                                self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                yield self.passed 

            elif(f == "Stakeholder_Type"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Stakeholder_Type):
                                self.passed[records.Stakeholder_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Stakeholder_Type]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Stakeholder_Type, priority=r.get(key))
                                self.passed[records.Stakeholder_Type]["ENF"]=self.statuss.validate_field(records.Stakeholder_Type)

                        else:
                            if(records):
                                if(len(records.Stakeholder_Type) == 1):
                                    self.passed[records.Stakeholder_Type]["FORMAT"]=checkformat.is_numeric(records.Stakeholder_Type)
                                else:
                                    self.passed[records.Stakeholder_Type]["FORMAT"]=False
                            else:
                                self.passed[records.Stakeholder_Type]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Stakeholder_Category"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Stakeholder_Category):
                                self.passed[records.Stakeholder_Category]={"Mandatory":True}
                            else:
                                self.passed[records.Stakeholder_Category]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Stakeholder_Category, priority=r.get(key))
                                self.passed[records.Stakeholder_Category]["ENF"]=self.statuss.validate_field(records.Stakeholder_Category)

                        else:
                            if(records):
                                if(len(records.Stakeholder_Category) == 1):
                                    self.passed[records.Stakeholder_Category]["FORMAT"]=checkformat.is_numeric(records.Stakeholder_Category)
                                else:
                                    self.passed[records.Stakeholder_Category]["FORMAT"]=False
                            else:
                                self.passed[records.Stakeholder_Category]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Shareholder_Percentage"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Shareholder_Percentage):
                                self.passed[records.Shareholder_Percentage]={"Mandatory":True}
                            else:
                                self.passed[records.Shareholder_Percentage]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Shareholder_Percentage, priority=r.get(key))
                                self.passed[records.Shareholder_Percentage]["ENF"]=self.statuss.validate_field(records.Shareholder_Percentage)

                        else:
                            if(records):
                                if(len(records.Shareholder_Percentage) >= 1):
                                    self.passed[records.Shareholder_Percentage]["FORMAT"]=checkformat.is_float(records.Shareholder_Percentage)
                                else:
                                    self.passed[records.Shareholder_Percentage]["FORMAT"]=False
                            else:
                                self.passed[records.Shareholder_Percentage]["FORMAT"]=False
                yield self.passed
        except Exception as e:
            # Log
            pass 
