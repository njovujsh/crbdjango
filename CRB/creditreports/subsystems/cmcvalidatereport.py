from validators.subsystems import cmccode 
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 
from branchcode import models as branchmodels

class ReportCMCValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="CMC"):
        super(ReportCMCValidate, self).__init__(code=code)
        self._model = models.COLLATERAL_MATERIAL_COLLATERAL
        self.all_records  = models.COLLATERAL_MATERIAL_COLLATERAL.objects.all()
        self.headers = branchmodels.RequiredHeader.objects.all()
        self.code = code 
        self.pi_c_code = cmccode.CMCCode(self._model, self.code)
        self.all_count = models.COLLATERAL_MATERIAL_COLLATERAL.objects.all().count()
        
        self.set_code(self.pi_c_code)
        
    def check_data_in_field(self, f, rules):        
        self.passed = {}
        self.all_records_passed = {}
        self.final_result={}
        try:
            self.PI_Identification_Code(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Borrowers_Client_Number(f, rules)
            self.Borrower_Account_Reference(f, rules)
            self.Borrower_Classification(f, rules)
            self.Collateral_Type_Identification(f, rules)
            self.Collateral_Reference_Number(f, rules)
            self.Collateral_Description(f, rules)
            self.Collateral_Currency(f, rules)
            self.Collateral_Open_Market_Value(f, rules)
            self.Collateral_Forced_Sale_Value(f, rules)
            self.Collateral_Valuation_Expiry_Date(f, rules)
            self.Instrument_of_Claim(f, rules)
            self.Valuation_Date(f, rules)
        except Exception as e:
            pass 
        else:
            yield self.final_result
        
    def PI_Identification_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "PI_Identification_Code"):
                for r in rules:
                    if r == "M":
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

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
                                    self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                    else:
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata) >= 2):
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
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(len(records.Branch_Identification_Code.branch_code) >= 2):
                            self.passed[records.id]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
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
    
    def Borrowers_Client_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Borrowers_Client_Number"):
                for r in rules:
                    if r == "M":
                        if(records.Borrowers_Client_Number.Client_Number):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

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
                                    self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Borrowers_Client_Number.Client_Number)
                                self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(records.Borrowers_Client_Number):
                            if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrowers_Client_Number.Client_Number)
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
    
    def Borrower_Account_Reference(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Borrower_Account_Reference"):
                for r in rules:
                    if r == "M":
                        if(records.Borrower_Account_Reference.Credit_Account_Reference):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Account_Reference.Credit_Account_Reference, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)

                    else:
                        if(len(records.Borrower_Account_Reference.Credit_Account_Reference) <= 30):
                            self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrower_Account_Reference)
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
            
    def Borrower_Classification(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Borrower_Classification"):
                for r in rules:
                    if r == "M":
                        if(records.Borrower_Classification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Borrower_Classification)

                    else:
                        if(records.Borrower_Classification):
                            if(len(records.Borrower_Classification) == 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Borrower_Classification)
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
            
    def Collateral_Type_Identification(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Type_Identification"):
                for r in rules:
                    if r == "M":
                        if(records.Collateral_Type_Identification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Type_Identification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Collateral_Type_Identification)

                    else:
                        if(len(records.Collateral_Type_Identification) >= 1):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Collateral_Type_Identification)
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
            
    def Collateral_Reference_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Reference_Number"):
                for r in rules:
                    if r == "M":
                        if(records.Collateral_Reference_Number):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Reference_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Collateral_Reference_Number)

                    else:
                        if(len(records.Collateral_Reference_Number) >= 2):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Collateral_Reference_Number)
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
            
    def Collateral_Description(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Description"):
                for r in rules:
                    if r == "M":
                        #print "Date ", records.License_Issuing_Date
                        if(records.Collateral_Description):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Description, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Collateral_Description)

                    else:
                        if(len(records.Collateral_Description) <= 1000):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Collateral_Description)
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
            
    def Collateral_Currency(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Currency"):
                for r in rules:
                    if r == "M":
                        if(records.Collateral_Currency):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Collateral_Currency, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Collateral_Currency)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Collateral_Currency, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Collateral_Currency)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Collateral_Currency, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Collateral_Currency, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Collateral_Currency)
                                self.validation_second = self.sec_enf.validate_field(records.Collateral_Currency, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False

                    else:
                        if(records.Collateral_Currency):
                            if(len(records.Collateral_Currency)  == 3):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Collateral_Currency)
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
            
    def Collateral_Open_Market_Value(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Open_Market_Value"):
                for r in rules:
                    if r == "M":
                        if(records.Collateral_Open_Market_Value):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Open_Market_Value, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Collateral_Open_Market_Value)

                    else:
                        if(len(records.Collateral_Open_Market_Value) <= 21):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Collateral_Open_Market_Value)
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
            
    def Collateral_Forced_Sale_Value(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Forced_Sale_Value"):
                for r in rules:
                    if r == "M":
                        if(records.Collateral_Forced_Sale_Value):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Forced_Sale_Value, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Collateral_Forced_Sale_Value)

                    else:
                        if(len(records.Collateral_Forced_Sale_Value) <= 21):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Collateral_Forced_Sale_Value)
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
    
    def Collateral_Valuation_Expiry_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Collateral_Valuation_Expiry_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Collateral_Valuation_Expiry_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Collateral_Valuation_Expiry_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Collateral_Valuation_Expiry_Date)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Collateral_Valuation_Expiry_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Collateral_Valuation_Expiry_Date)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Collateral_Valuation_Expiry_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Collateral_Valuation_Expiry_Date, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Collateral_Valuation_Expiry_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Collateral_Valuation_Expiry_Date)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(records.Collateral_Valuation_Expiry_Date):
                            self.replace = records.Collateral_Valuation_Expiry_Date.replace("-", "", 50)
                            if(len(self.replace) >= 6):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(self.replace)
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
            
    def Instrument_of_Claim(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Instrument_of_Claim"):
                for r in rules:
                    if r == "M":
                        if(records.Instrument_of_Claim):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Instrument_of_Claim, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Instrument_of_Claim)

                    else:
                        if(len(records.Instrument_of_Claim) <= 30):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Instrument_of_Claim)
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
    
    def Valuation_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Valuation_Date"):            
                for r in rules:
                    if r == "M":
                        if(records.Valuation_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            self.third_priority = self.check_dict_values(r.get(key)[2])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Valuation_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Valuation_Date)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Valuation_Date)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Valuation_Date)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            
                            elif(self.second_priority == 1 or self.second_priority == 2):
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Valuation_Date, priority=r.get(key))
                                self.validation_second = self.sec_enf.validate_field(records.Valuation_Date)

                                if(self.validation_second == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Valuation_Date)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Valuation_Date)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.third_priority == 1 or self.third_priority == 2):
                                self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Valuation_Date, priority=r.get(key))
                                self.validation_third = self.third_ef.validate_field(records.Valuation_Date)
                                
                                if(self.validation_third == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Valuation_Date)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Valuation_Date)
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.passed[records.id]["ENF"]=False

                    else:
                        if(records.Valuation_Date):
                            self.value_date = records.Valuation_Date.replace("-", "", 20)
                            if(len(self.value_date) >= 6):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(self.value_date)
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
