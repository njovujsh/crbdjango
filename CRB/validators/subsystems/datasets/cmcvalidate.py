from validators.subsystems import cmccode 
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from branchcode import models as branchmodels

class CMCValidate(ibvalidate.IBValidate):
    def __init__(self, code="CCG"):
        super(CMCValidate, self).__init__(code=code)
        self._model = models.COLLATERAL_MATERIAL_COLLATERAL
        self.all_records  = self.filter_new_old_records(models.COLLATERAL_MATERIAL_COLLATERAL)
        self.headers = branchmodels.RequiredHeader.objects.all()
        self.code = code 
        self.pi_c_code = cmccode.CMCCode(self._model, self.code)
        
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
                                        #print "First validation has passed "
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                        
                                        if(self.validation_second == True):
                                            #print "Second validation has also passed"
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=True 
                                        else:
                                            #print "Second validation has also failed"
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False
                                    else:
                                        #print "First validation has failed."
                                        self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                    self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=True
                                        else:
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False
                                    else:
                                        self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False 
                        else:
                            if(records.PI_Identification_Code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "",10)
                                if(len(self.parseddata) >= 2 ):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code)]["FORMAT"]=False
                #print self.passed 
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
                                        self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=True 
                                        else:
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                    self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=True
                                        else:
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False
                                    else:
                                        self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False 

                        else:
                            if(len(records.Branch_Identification_Code.branch_code) >= 2):
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                print self.passed
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
                                        self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                        
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
                                    self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=True
                                        else:
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False
                                    else:
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False 

                        else:
                            if(records.Borrowers_Client_Number):
                                if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                                    self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrowers_Client_Number.Client_Number)
                                else:
                                    self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                            else:
                                self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                yield self.passed 

            elif(f == "Borrower_Account_Reference"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Borrower_Account_Reference):
                                if(records.Borrower_Account_Reference.Credit_Account_Reference):
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]={"Mandatory":True}
                                else:
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]={"Mandatory":False}
                            else:
                                self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.Borrower_Account_Reference):
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Account_Reference.Credit_Account_Reference, priority=r.get(key))
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["ENF"]=self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)
                                else:
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["ENF"]=self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)

                        else:
                            if(records.Borrower_Account_Reference):
                                if(len(records.Borrower_Account_Reference.Credit_Account_Reference) <= 30):
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrower_Account_Reference)
                                else:
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["FORMAT"]=False
                            else:
                                self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["FORMAT"]=False
                #print "Account Reference", self.passed
                yield self.passed 
                
            elif(f == "Borrower_Classification"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Borrower_Classification):
                                self.passed[records.Borrower_Classification]={"Mandatory":True}
                            else:
                                self.passed[records.Borrower_Classification]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Classification, priority=r.get(key))
                                self.passed[records.Borrower_Classification]["ENF"]=self.statuss.validate_field(records.Borrower_Classification)

                        else:
                            if(len(records.Borrower_Classification) == 1):
                                self.passed[records.Borrower_Classification]["FORMAT"]=checkformat.is_numeric(records.Borrower_Classification)
                            else:
                                self.passed[records.Borrower_Classification]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Collateral_Type_Identification"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Collateral_Type_Identification):
                                self.passed[records.Collateral_Type_Identification]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Type_Identification]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Type_Identification, priority=r.get(key))
                                self.passed[records.Collateral_Type_Identification]["ENF"]=self.statuss.validate_field(records.Collateral_Type_Identification)

                        else:
                            if(len(records.Collateral_Type_Identification) >=1):
                                self.passed[records.Collateral_Type_Identification]["FORMAT"]=checkformat.is_numeric(records.Collateral_Type_Identification)
                            else:
                                self.passed[records.Collateral_Type_Identification]["FORMAT"]=False
                #print self.passed
                yield self.passed 
                
            elif(f == "Collateral_Reference_Number"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Collateral_Reference_Number):
                                self.passed[records.Collateral_Reference_Number]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Reference_Number]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Reference_Number, priority=r.get(key))
                                self.passed[records.Collateral_Reference_Number]["ENF"]=self.statuss.validate_field(records.Collateral_Reference_Number)

                        else:
                            if(len(records.Collateral_Reference_Number) >= 2):
                                self.passed[records.Collateral_Reference_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.Collateral_Reference_Number)
                            else:
                                self.passed[records.Collateral_Reference_Number]["FORMAT"]=False
                self.passed
                yield self.passed 
                
            elif(f == "Collateral_Description"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Collateral_Description):
                                self.passed[records.Collateral_Description]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Description]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Description, priority=r.get(key))
                                self.passed[records.Collateral_Description]["ENF"]=self.statuss.validate_field(records.Collateral_Description)

                        else:
                            if(len(records.Collateral_Description) <= 1000):
                                self.passed[records.Collateral_Description]["FORMAT"]=checkformat.sub_alphanumeric(records.Collateral_Description)
                            else:
                                self.passed[records.Collateral_Description]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Collateral_Currency"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Collateral_Currency):
                                self.passed[records.Collateral_Currency]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Currency]={"Mandatory":False}

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
                                            self.passed[records.Collateral_Currency]["ENF"]=True 
                                        else:
                                            self.passed[records.Collateral_Currency]["ENF"]=False 
                                    else:
                                        self.passed[records.Collateral_Currency]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Collateral_Currency, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Collateral_Currency, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Collateral_Currency)
                                    self.validation_second = self.sec_enf.validate_field(records.Collateral_Currency, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Collateral_Currency]["ENF"]=True
                                        else:
                                            self.passed[records.Collateral_Currency]["ENF"]=False
                                    else:
                                        self.passed[records.Collateral_Currency]["ENF"]=False

                        else:
                            if(len(records.Collateral_Currency)  == 3):
                                self.passed[records.Collateral_Currency]["FORMAT"]=checkformat.sub_alphanumeric(records.Collateral_Currency)
                            else:
                                self.passed[records.Collateral_Currency]["FORMAT"]=False

                yield self.passed 
                
            elif(f == "Collateral_Open_Market_Value"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Collateral_Open_Market_Value):
                                self.passed[records.Collateral_Open_Market_Value]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Open_Market_Value]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Open_Market_Value, priority=r.get(key))
                                self.passed[records.Collateral_Open_Market_Value]["ENF"]=self.statuss.validate_field(records.Collateral_Open_Market_Value)

                        else:
                            if(len(records.Collateral_Open_Market_Value) <= 21):
                                self.passed[records.Collateral_Open_Market_Value]["FORMAT"]=checkformat.is_numeric(records.Collateral_Open_Market_Value)
                            else:
                                self.passed[records.Collateral_Open_Market_Value]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Collateral_Forced_Sale_Value"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Collateral_Forced_Sale_Value):
                                self.passed[records.Collateral_Forced_Sale_Value]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Forced_Sale_Value]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Collateral_Forced_Sale_Value, priority=r.get(key))
                                self.passed[records.Collateral_Forced_Sale_Value]["ENF"]=self.statuss.validate_field(records.Collateral_Forced_Sale_Value)

                        else:
                            if(len(records.Collateral_Forced_Sale_Value) <= 21):
                                self.passed[records.Collateral_Forced_Sale_Value]["FORMAT"]=checkformat.is_numeric(records.Collateral_Forced_Sale_Value)
                            else:
                                self.passed[records.Collateral_Forced_Sale_Value]["FORMAT"]=False
                yield self.passed 

            elif(f == "Collateral_Valuation_Expiry_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Collateral_Valuation_Expiry_Date):
                                self.passed[records.Collateral_Valuation_Expiry_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Collateral_Valuation_Expiry_Date]={"Mandatory":False}

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
                                            self.passed[records.Collateral_Valuation_Expiry_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Collateral_Valuation_Expiry_Date]["ENF"]=False
                                    else:
                                        self.passed[records.PCollateral_Valuation_Expiry_Date]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Collateral_Valuation_Expiry_Date, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Collateral_Valuation_Expiry_Date, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Collateral_Valuation_Expiry_Date)
                                    self.validation_second = self.sec_enf.validate_field(records.Collateral_Valuation_Expiry_Date)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Collateral_Valuation_Expiry_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Collateral_Valuation_Expiry_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Collateral_Valuation_Expiry_Date]["ENF"]=False 

                        else:
                            if(records.Collateral_Valuation_Expiry_Date):
                                self.replace = records.Collateral_Valuation_Expiry_Date.replace("-", "", 50)
                                if(len(self.replace) >= 6):
                                    self.passed[records.Collateral_Valuation_Expiry_Date]["FORMAT"]=checkformat.is_numeric(self.replace)
                                else:
                                    self.passed[records.Collateral_Valuation_Expiry_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Collateral_Valuation_Expiry_Date]["FORMAT"]=False
                #print "DATE ", self.passed 
                yield self.passed 

            elif(f == "Instrument_of_Claim"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Instrument_of_Claim):
                                self.passed[records.Instrument_of_Claim]={"Mandatory":True}
                            else:
                                self.passed[records.Instrument_of_Claim]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Instrument_of_Claim, priority=r.get(key))
                                self.passed[records.Instrument_of_Claim]["ENF"]=self.statuss.validate_field(records.Instrument_of_Claim)

                        else:
                            if(len(records.Instrument_of_Claim) <= 30):
                                self.passed[records.Instrument_of_Claim]["FORMAT"]=checkformat.sub_alphanumeric(records.Instrument_of_Claim)
                            else:
                                self.passed[records.Instrument_of_Claim]["FORMAT"]=False
                yield self.passed 

            elif(f == "Valuation_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Valuation_Date):
                                self.passed[records.Valuation_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Valuation_Date]={"Mandatory":False}

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
                                            self.passed[records.Valuation_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Valuation_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Valuation_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Valuation_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Valuation_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Valuation_Date]["ENF"]=False 
                                    else:
                                        self.passed[records.Valuation_Date]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Valuation_Date)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Valuation_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Valuation_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Valuation_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Valuation_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Valuation_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Valuation_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Valuation_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Valuation_Date]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Valuation_Date]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Valuation_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Valuation_Date)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Valuation_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Valuation_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Valuation_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Valuation_Date]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Valuation_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Valuation_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.Valuation_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Valuation_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Valuation_Date]["ENF"]=False
                                else:
                                    self.passed[records.Valuation_Date]["ENF"]=False

                        else:
                            if(records.Valuation_Date):
                                self.value_date = records.Valuation_Date.replace("-", "", 20)
                                if(len(self.value_date) >= 6):
                                    self.passed[records.Valuation_Date]["FORMAT"]=checkformat.is_numeric(self.value_date)
                                else:
                                    self.passed[records.Valuation_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Valuation_Date]["FORMAT"]=False
                #print "EVA ", self.passed
                yield self.passed
        except Exception as e:
            # Log
            pass  
