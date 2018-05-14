from validators.subsystems import cbacode  
from datasetrecords import models 
from validators.subsystems import checkstatus 
from validators.subsystems import checkformat 
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate 
from validators.subsystems.enforcements import enf007
from validators.subsystems.datasets import validationstatus
from validators.subsystems.datasets import ibvalidate

class CBAValidate(ibvalidate.IBValidate):
    def __init__(self, code="CBA"):
        super(CBAValidate, self).__init__()
        self.cba_model = models.CREDITBORROWERACCOUNT
        self.all_records = self.filter_new_old_records(models.CREDITBORROWERACCOUNT)
        self.code = code 
        self.pi_c_code = cbacode.CBACode(self.cba_model, self.code)
        
        #set the code on use
        self.set_code(self.pi_c_code)
        
    def begin_validation(self):
        try:
            self.all_fields = self.pi_c_code.extract()
            self.examine_field(self.all_fields)
        except Exception as e:
            pass 
            
    def check_data_in_field(self, f, rules):
        self.passed = {}
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
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code)
                                self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                        else:
                            if(records.PI_Identification_Code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                                if(len(self.parseddata) == 6 or len(self.parseddata) <=8 ):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code.pi_identification_code)]["FORMAT"]=False
                #print self.passed
                yield self.passed
                 
            elif(f == "Branch_Identification_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Branch_Identification_Code.branch_code):
                                self.passed[records.Branch_Identification_Code.branch_code]={"Mandatory":True}
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code)
                                self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)
                        else:
                            if(len(str(records.Branch_Identification_Code.branch_code)) <= 15):
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                #print self.passed 
                yield self.passed
                
            elif(f == "Borrowers_Client_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        try:
                            if r == "M":
                                if(records.Borrowers_Client_Number.Client_Number):
                                    self.passed[records.Borrowers_Client_Number.Client_Number]={"Mandatory":True}
                                else:
                                    self.passed[records.Borrowers_Client_Number.Client_Number]={"Mandatory":False} 
                                
                            elif(isinstance(r, dict)):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrowers_Client_Number.Client_Number)
                                    self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=self.statuss.validate_field(records.Borrowers_Client_Number.Client_Number)
                            else:
                                if(records.Borrowers_Client_Number.Client_Number):
                                    if(len(str(records.Borrowers_Client_Number.Client_Number)) <= 30):
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrowers_Client_Number.Client_Number)
                                    else:
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                        except:
                            continue
                yield self.passed  
                
            elif(f == "Borrower_Classification"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Borrower_Classification):
                                self.passed[records.Borrower_Classification]={"Mandatory":True}
                            else:
                                self.passed[records.Borrower_Classification]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Classification)
                                self.passed[records.Borrower_Classification]["ENF"]=self.statuss.validate_field(records.Borrower_Classification)
                        else:
                            if(records.Borrower_Classification):
                                if(len(str(records.Borrower_Classification)) == 1):
                                    self.passed[records.Borrower_Classification]["FORMAT"]=checkformat.is_numeric(int(float(records.Borrower_Classification)))
                                else:
                                    self.passed[records.Borrower_Classification]["FORMAT"]=False
                            else:
                                self.passed[records.Borrower_Classification]["FORMAT"]=False
                yield self.passed  
                 
            elif(f == "Credit_Account_Reference"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Account_Reference):
                                self.passed[records.Credit_Account_Reference]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Account_Reference]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                             for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self.pi_c_code, records.Credit_Account_Reference)
                                self.passed[records.Credit_Account_Reference]["ENF"]=self.statuss.validate_field(records.Credit_Account_Reference)
                                #print self.statuss                   
                        else:
                            if(records.Credit_Account_Reference):
                                if(len(str(records.Credit_Account_Reference)) <= 30):
                                    self.passed[records.Credit_Account_Reference]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Credit_Account_Reference)
                                else:
                                    self.passed[records.Credit_Account_Reference]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Reference]["FORMAT"]=False
                yield self.passed   
                
            elif(f == "Credit_Account_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Account_Date):
                                self.passed[records.Credit_Account_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Account_Date]={"Mandatory":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Date)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Date)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Account_Date]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Date)
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Date, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Account_Date]["ENF"]=False 
                        else:
                            if(records.Credit_Account_Date):
                                if(len(str(records.Credit_Account_Date)) <= 8):
                                    self.passed[records.Credit_Account_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Date)))
                                else:
                                    self.passed[records.Credit_Account_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Date]["FORMAT"]=False
                yield self.passed   
                 
            elif(f == "Credit_Amount"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        try:
                            if r == "C":
                                if(records.Credit_Amount):
                                    self.passed[records.Credit_Amount]={"Conditional":True}
                                else:
                                    self.passed[records.Credit_Amount]={"Conditional":True}
                            elif(isinstance(r, dict)):
                                if(records.Credit_Amount):
                                    for key in r:
                                        self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Amount, priority=r.get(key))
                                        self.passed[records.Credit_Amount]["ENF"]=self.statuss.validate_field(records.Credit_Amount, records)
                                else:
                                    self.passed[records.Credit_Amount]["ENF"]=True
                            else:
                                if(records.Credit_Amount):
                                    if(len(str(records.Credit_Amount)) <= 21):
                                        if(records.Credit_Amount.strip().lstrip().rstrip()):
                                            self.passed[records.Credit_Amount]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Amount)))
                                        else:
                                            self.passed[records.Credit_Amount]["FORMAT"]=False
                                    else:
                                        self.passed[records.Credit_Amount]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Amount]["FORMAT"]=True
                        except:
                            raise 
                yield self.passed   
                 
            elif(f == "Facility_Amount_Granted"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        try:
                            if r == "C":
                                if(records.Facility_Amount_Granted):
                                    self.passed[records.Facility_Amount_Granted]={"Conditional":True}
                                else:
                                    self.passed[records.Facility_Amount_Granted]={"Conditional":True} 
                            elif(isinstance(r, dict)):
                                if(records.Facility_Amount_Granted):
                                    for key in r:
                                        self.statuss = checkenforcements.check_enforcements(key, self._model, records.Facility_Amount_Granted, priority=r.get(key))
                                        self.passed[records.Facility_Amount_Granted]["ENF"]=self.statuss.validate_field(records.Facility_Amount_Granted, more_validation=records)
                                else:
                                    self.passed[records.Facility_Amount_Granted]["ENF"]=True
                            else:
                                if(records.Facility_Amount_Granted):
                                    if(len(str(records.Facility_Amount_Granted)) <= 21):
                                        if(str(records.Facility_Amount_Granted).strip().lstrip().rstrip()):
                                            self.passed[records.Facility_Amount_Granted]["FORMAT"]=checkformat.is_numeric(int(float(records.Facility_Amount_Granted)))
                                        else:
                                            self.passed[records.Facility_Amount_Granted]["FORMAT"]=False
                                    else:
                                        self.passed[records.Facility_Amount_Granted]["FORMAT"]=False
                                else:
                                    self.passed[records.Facility_Amount_Granted]["FORMAT"]=True
                        except:
                            continue 
                yield self.passed   
                 
            elif(f == "Credit_Account_Type"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Account_Type):
                                self.passed[records.Credit_Account_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Account_Type]={"Mandatory":False}
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Account_Type, priority=r.get(key))
                                self.passed[records.Credit_Account_Type]["ENF"]=self.statuss.validate_field(records.Credit_Account_Type)

                        else:
                            if(records.Credit_Account_Type):
                                if(len(str(records.Credit_Account_Type)) <= 2):
                                    if(records.Credit_Account_Type.strip().lstrip().rstrip()):
                                        self.passed[records.Credit_Account_Type]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Type)))
                                    else:
                                        self.passed[records.Credit_Account_Type]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Account_Type]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Type]["FORMAT"]=False
                yield self.passed   
                 
            elif(f == "Group_Identification_Joint_Account_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            #print "B CLASSIFICA TION ", records.Borrower_Classification
                            if(records.Borrower_Classification == "1"):
                                if(records.Group_Identification_Joint_Account_Number):
                                    self.passed[records.Group_Identification_Joint_Account_Number]={"Conditional":True}
                                else:
                                    self.passed[records.Group_Identification_Joint_Account_Number]={"Conditional":False}
                            else:
                                self.passed[records.Group_Identification_Joint_Account_Number]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.Borrower_Classification == "1"):
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Group_Identification_Joint_Account_Number, priority=r.get(key))
                                    self.passed[records.Group_Identification_Joint_Account_Number]["ENF"]=self.statuss.validate_field(records.Group_Identification_Joint_Account_Number, records)
                                else:
                                    self.passed[records.Group_Identification_Joint_Account_Number]["ENF"]=True #self.statuss.validate_field(records.Group_Identification_Joint_Account_Number, records)
                        else:
                            if(records.Borrower_Classification == "1"):
                                if(len(str(records.Group_Identification_Joint_Account_Number)) <= 30):
                                    self.passed[records.Group_Identification_Joint_Account_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Group_Identification_Joint_Account_Number)
                                else:
                                    self.passed[records.Group_Identification_Joint_Account_Number]["FORMAT"]=False
                            else:
                                self.passed[records.Group_Identification_Joint_Account_Number]["FORMAT"]=True
                yield self.passed    
                
            elif(f == "Transaction_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Transaction_Date):
                                self.passed[records.Transaction_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Transaction_Date]={"Mandatory":True}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Transaction_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Transaction_Date, records=records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Transaction_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Transaction_Date, records=records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Transaction_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Transaction_Date]["ENF"]=True
                                    else:
                                        self.passed[records.Transaction_Date]["ENF"]=True
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Transaction_Date, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Transaction_Date, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Transaction_Date)
                                    self.validation_second = self.sec_enf.validate_field(records.Transaction_Date, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Transaction_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Transaction_Date]["ENF"]=True
                                    else:
                                        self.passed[records.Transaction_Date]["ENF"]=True 

                        else:
                            if(records.Transaction_Date):
                                if(len(str(records.Transaction_Date)) <= 12):
                                    self.passed[records.Transaction_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Transaction_Date)))
                                else:
                                    self.passed[records.Transaction_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Transaction_Date]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Currency"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Currency):
                                self.passed[records.Currency]={"Mandatory":True}
                            else:
                                self.passed[records.Currency]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Currency, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Currency)
                                    
                                    if(self.validation_first == True):
                                        #print "First validation has passed."
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Currency, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Currency)
                                        
                                        if(self.validation_second == True):
                                            #print "Second validation has passed..."
                                            self.passed[records.Currency]["ENF"]=True 
                                        else:
                                            #print "Second validation has failed...", self.sec_enf
                                            self.passed[records.Currency]["ENF"]=False
                                    else:
                                        #print "First validation has failed..."
                                        self.passed[records.Currency]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Currency, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Currency, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Currency)
                                    self.validation_second = self.sec_enf.validate_field(records.Currency, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Currency]["ENF"]=True
                                        else:
                                            self.passed[records.Currency]["ENF"]=False
                                    else:
                                        self.passed[records.Currency]["ENF"]=False
                        else:
                            if(records.Currency):
                                if(len(str(records.Currency)) <= 5):
                                    self.passed[records.Currency]["FORMAT"]=checkformat.sub_alphanumeric(records.Currency)
                                else:
                                    self.passed[records.Currency]["FORMAT"]=False
                            else:
                                self.passed[records.Currency]["FORMAT"]=False
                #print self.passed
                yield self.passed   
                  
            elif(f == "Opening_Balance_Indicator"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Opening_Balance_Indicator):
                                self.passed[records.Opening_Balance_Indicator]={"Mandatory":True}
                            else:
                                self.passed[records.Opening_Balance_Indicator]={"Mandatory":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Opening_Balance_Indicator, priority=r.get(key))
                                self.passed[records.Opening_Balance_Indicator]["ENF"]=self.statuss.validate_field(records)
                        else:
                            if(records.Opening_Balance_Indicator):
                                if(len(str(records.Opening_Balance_Indicator)) == 1):
                                    if(str(records.Opening_Balance_Indicator).strip().lstrip().rstrip()):
                                        self.passed[records.Opening_Balance_Indicator]["FORMAT"]=checkformat.is_numeric(int(float(records.Opening_Balance_Indicator)))
                                    else:
                                        self.passed[records.Opening_Balance_Indicator]["FORMAT"]=False
                                else:
                                    self.passed[records.Opening_Balance_Indicator]["FORMAT"]=False   
                            else:       
                                self.passed[records.Opening_Balance_Indicator]["FORMAT"]=False
                yield self.passed    
                 
            elif(f == "Maturity_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Maturity_Date):
                                self.passed[records.Maturity_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Maturity_Date]={"Mandatory":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Maturity_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Maturity_Date)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Maturity_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Maturity_Date)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Maturity_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Maturity_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Maturity_Date]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Maturity_Date, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Maturity_Date, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Maturity_Date)
                                    self.validation_second = self.sec_enf.validate_field(records.Maturity_Date, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Maturity_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Maturity_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Maturity_Date]["ENF"]=False 

                        else:
                            if(records.Maturity_Date):
                                if(len(str(records.Maturity_Date)) <= 8):
                                    if(str(records.Maturity_Date).strip().lstrip().rstrip()):
                                        self.passed[records.Maturity_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Maturity_Date)))
                                    else:
                                        self.passed[records.Maturity_Date]["FORMAT"]=False
                                else:
                                    self.passed[records.Maturity_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Maturity_Date]["FORMAT"]=False
                yield self.passed
                    
            elif(f == "Type_of_Interest"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Type_of_Interest):
                                self.passed[records.Type_of_Interest]={"Mandatory":True}
                            else:
                                self.passed[records.Type_of_Interest]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Type_of_Interest, priority=r.get(key))
                                self.passed[records.Type_of_Interest]["ENF"]=self.statuss.validate_field(records.Type_of_Interest)

                        else:
                            if(records.Type_of_Interest):
                                if(len(str(records.Type_of_Interest)) == 1):
                                    if(str(records.Type_of_Interest).strip().lstrip().rstrip()):
                                        self.passed[records.Type_of_Interest]["FORMAT"]=checkformat.is_numeric(int(float(records.Type_of_Interest)))
                                    else:
                                        self.passed[records.Type_of_Interest]["FORMAT"]=False
                                else:
                                    self.passed[records.Type_of_Interest]["FORMAT"]=False
                            else:
                                self.passed[records.Type_of_Interest]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Interest_Calculation_Method"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Interest_Calculation_Method):
                                self.passed[records.Interest_Calculation_Method]={"Mandatory":True}
                            else:
                                self.passed[records.Interest_Calculation_Method]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Interest_Calculation_Method, priority=r.get(key))
                                self.passed[records.Interest_Calculation_Method]["ENF"]=self.statuss.validate_field(records.Interest_Calculation_Method)

                        else:
                            if(str(records.Interest_Calculation_Method).strip().lstrip().rstrip()):
                                if(len(str(records.Interest_Calculation_Method).strip().lstrip().rstrip()) <= 4):
                                    self.passed[records.Interest_Calculation_Method]["FORMAT"]=checkformat.is_numeric(int(records.Interest_Calculation_Method))
                                else:
                                    self.passed[records.Interest_Calculation_Method]["FORMAT"]=False
                            else:                            
                                self.passed[records.Interest_Calculation_Method]["FORMAT"]=False
                yield self.passed    
                
            elif(f == "Annual_Interest_Rate_at_Disbursement"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Annual_Interest_Rate_at_Disbursement):
                                self.passed[records.Annual_Interest_Rate_at_Disbursement]={"Mandatory":True}
                            else:
                                self.passed[records.Annual_Interest_Rate_at_Disbursement]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Annual_Interest_Rate_at_Disbursement, priority=r.get(key))
                                self.passed[records.Annual_Interest_Rate_at_Disbursement]["ENF"]=self.statuss.validate_field(records.Annual_Interest_Rate_at_Disbursement)
                        else:
                            if(len(str(records.Annual_Interest_Rate_at_Disbursement).strip().lstrip().rstrip()) <= 10):
                                if(len(records.Annual_Interest_Rate_at_Disbursement) != 0):
                                    self.passed[records.Annual_Interest_Rate_at_Disbursement]["FORMAT"]=checkformat.is_float(float(records.Annual_Interest_Rate_at_Disbursement.strip().lstrip().rstrip()))
                                else:
                                    self.passed[records.Annual_Interest_Rate_at_Disbursement]["FORMAT"]=False
                            else:
                                self.passed[records.Annual_Interest_Rate_at_Disbursement]["FORMAT"]=False
                yield self.passed  
                   
            elif(f == "Annual_Interest_Rate_at_Reporting"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Annual_Interest_Rate_at_Reporting):
                                self.passed[records.Annual_Interest_Rate_at_Reporting]={"Mandatory":True}
                            else:
                                self.passed[records.Annual_Interest_Rate_at_Reporting]={"Mandatory":True}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Annual_Interest_Rate_at_Reporting, priority=r.get(key))
                                self.passed[records.Annual_Interest_Rate_at_Reporting]["ENF"]=True #self.statuss.validate_field(records.Annual_Interest_Rate_at_Reporting)

                        else:
                            if(records.Annual_Interest_Rate_at_Reporting):
                                if(len(str(records.Annual_Interest_Rate_at_Reporting)) <= 10):
                                    if(str(records.Annual_Interest_Rate_at_Reporting).strip().lstrip().rstrip()):
                                        self.passed[records.Annual_Interest_Rate_at_Reporting]["FORMAT"]=checkformat.is_float(float(records.Annual_Interest_Rate_at_Reporting.strip().lstrip().rstrip()))
                                    else:
                                        self.passed[records.Annual_Interest_Rate_at_Reporting]["FORMAT"]=True
                                else:
                                    self.passed[records.Annual_Interest_Rate_at_Reporting]["FORMAT"]=True
                            else:
                                self.passed[records.Annual_Interest_Rate_at_Reporting]["FORMAT"]=True
                yield self.passed
                    
            elif(f == "Date_of_First_Payment"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Date_of_First_Payment):
                                self.passed[records.Date_of_First_Payment]={"Conditional":True}
                            else:
                                self.passed[records.Date_of_First_Payment]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Date_of_First_Payment):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    self.third_priority = self.check_dict_values(r.get(key)[2])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2): 
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Date_of_First_Payment, records=records)
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.Date_of_First_Payment]["ENF"]=True 
                                            else:
                                                self.passed[records.Date_of_First_Payment]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Date_of_First_Payment,records=records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Date_of_First_Payment]["ENF"]=True
                                            else:
                                                self.passed[records.Date_of_First_Payment]["ENF"]=False 
                                        else:
                                            self.passed[records.Date_of_First_Payment]["ENF"]=False 
                                    
                                    elif(self.second_priority == 1 or self.second_priority == 2):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)

                                        if(self.validation_second == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Date_of_First_Payment,records=records)

                                            if(self.validation_first == True):
                                                self.passed[records.Date_of_First_Payment]["ENF"]=True 
                                            else:
                                                self.passed[records.Date_of_First_Payment]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Date_of_First_Payment,records=records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Date_of_First_Payment]["ENF"]=True
                                            else:
                                                self.passed[records.Date_of_First_Payment]["ENF"]=False
                                                
                                        else:
                                            self.passed[records.Date_of_First_Payment]["ENF"]=False
                                            
                                    elif(self.third_priority == 1 or self.third_priority == 2):
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Date_of_First_Payment, records=records)
                                        
                                        if(self.validation_third == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Date_of_First_Payment,records=records)

                                            if(self.validation_first == True):
                                                self.passed[records.Date_of_First_Payment]["ENF"]=True 
                                            else:
                                                self.passed[records.Date_of_First_Payment]["ENF"]=False
                                                
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            if(self.validation_second == True):
                                                self.passed[records.Date_of_First_Payment]["ENF"]=True
                                            else:
                                                self.passed[records.Date_of_First_Payment]["ENF"]=False
                                        else:
                                            self.passed[records.Date_of_First_Payment]["ENF"]=False
                                    else:
                                        self.passed[records.Date_of_First_Payment]["ENF"]=False
                            else:
                                self.passed[records.Date_of_First_Payment]["ENF"]=True
                        else:
                            if(records.Date_of_First_Payment):
                                if(len(str(records.Date_of_First_Payment)) <= 8):
                                    self.passed[records.Date_of_First_Payment]["FORMAT"]=checkformat.is_numeric(int(float(records.Date_of_First_Payment)))
                                else:
                                    self.passed[records.Date_of_First_Payment]["FORMAT"]=False
                            else:
                                self.passed[records.Date_of_First_Payment]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Credit_Amortization_Type"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Amortization_Type):
                                self.passed[records.Credit_Amortization_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Amortization_Type]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Amortization_Type, priority=r.get(key))
                                self.passed[records.Credit_Amortization_Type]["ENF"]=self.statuss.validate_field(records)
                        else:
                            if(records.Credit_Amortization_Type):
                                if(len(str(records.Credit_Amortization_Type)) == 1):
                                    if(str(records.Credit_Amortization_Type).strip().lstrip().rstrip()):
                                        self.passed[records.Credit_Amortization_Type]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Amortization_Type)))
                                    else:
                                        self.passed[records.Credit_Amortization_Type]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Amortization_Type]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Amortization_Type]["FORMAT"]=False
                yield self.passed
                
            elif(f == "Credit_Payment_Frequency"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Credit_Payment_Frequency):
                                self.passed[records.Credit_Payment_Frequency]={"Conditional":True}
                            else:
                                self.passed[records.Credit_Payment_Frequency]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Credit_Payment_Frequency):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Payment_Frequency, priority=r.get(key))
                                    self.passed[records.Credit_Payment_Frequency]["ENF"]=self.statuss.validate_field(records)
                            else:
                                self.passed[records.Credit_Payment_Frequency]["ENF"]=True

                        else:
                            if(records.Credit_Payment_Frequency):
                                if(len(str(records.Credit_Payment_Frequency).strip().lstrip().rstrip()) <= 5):
                                    self.passed[records.Credit_Payment_Frequency]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Payment_Frequency)))
                                else:
                                    self.passed[records.Credit_Payment_Frequency]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Payment_Frequency]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Number_of_Payments"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        try:
                            if r == "C":
                                if(records.Number_of_Payments):
                                    self.passed[records.Number_of_Payments]={"Conditional":True}
                                else:
                                    self.passed[records.Number_of_Payments]={"Conditional":True} 
                                
                            elif(isinstance(r, dict)):
                                if(records.Number_of_Payments):
                                    for key in r:
                                        self.statuss = checkenforcements.check_enforcements(key, self._model, records.Number_of_Payments, priority=r.get(key))
                                        self.passed[records.Number_of_Payments]["ENF"]=self.statuss.validate_field(records.Number_of_Payments, records=records)
                                else:
                                    self.passed[records.Number_of_Payments]["ENF"]=True
                            else:
                                if(records.Number_of_Payments):
                                    if(len(str(records.Number_of_Payments)) <= 4):
                                        if(str(records.Number_of_Payments).strip().lstrip().rstrip()):
                                            self.passed[records.Number_of_Payments]["FORMAT"]=checkformat.is_numeric(int(float(records.Number_of_Payments)))
                                        else:
                                            self.passed[records.Number_of_Payments]["FORMAT"]=False
                                    else:
                                        self.passed[records.Number_of_Payments]["FORMAT"]=False
                                else:
                                    self.passed[records.Number_of_Payments]["FORMAT"]=True
                        except:
                            continue
                yield self.passed    
                
            elif(f == "Monthly_Instalment_Amount"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        try:
                            if r == "C":
                                if(records.Monthly_Instalment_Amount):
                                    self.passed[records.Monthly_Instalment_Amount]={"Conditional":True}
                                else:
                                    self.passed[records.Monthly_Instalment_Amount]={"Conditional":True} 
                            elif(isinstance(r, dict)):
                                if(records.Monthly_Instalment_Amount):
                                    for key in r:
                                        self.statuss = checkenforcements.check_enforcements(key, self._model, records.Monthly_Instalment_Amount, priority=r.get(key))
                                        self.passed[records.Monthly_Instalment_Amount]["ENF"]=self.statuss.validate_field(records.Monthly_Instalment_Amount, records)
                                else:
                                    self.passed[records.Monthly_Instalment_Amount]["ENF"]=True
                            else:
                                if(records.Monthly_Instalment_Amount):
                                    if(len(str(records.Monthly_Instalment_Amount)) <= 21):
                                        if(str(records.Monthly_Instalment_Amount).strip().lstrip().rstrip()):
                                            self.passed[records.Monthly_Instalment_Amount]["FORMAT"]=checkformat.is_numeric(int(float(records.Monthly_Instalment_Amount)))
                                        else:
                                            self.passed[records.Monthly_Instalment_Amount]["FORMAT"]=False
                                    else:
                                        self.passed[records.Monthly_Instalment_Amount]["FORMAT"]=False
                                else:
                                    self.passed[records.Monthly_Instalment_Amount]["FORMAT"]=True
                        except:
                            continue
                yield self.passed
                
            elif(f == "Current_Balance_Amount"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Current_Balance_Amount):
                                self.passed[records.Current_Balance_Amount]={"Mandatory":True}
                            else:
                                self.passed[records.Current_Balance_Amount]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Current_Balance_Amount, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Current_Balance_Amount)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Current_Balance_Amount, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.Current_Balance_Amount]["ENF"]=True 
                                        else:
                                            self.passed[records.Current_Balance_Amount]["ENF"]=False
                                    else:
                                        self.passed[records.Current_Balance_Amount]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Current_Balance_Amount, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Current_Balance_Amount, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Current_Balance_Amount)
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Current_Balance_Amount]["ENF"]=True
                                        else:
                                            self.passed[records.Current_Balance_Amount]["ENF"]=False
                                    else:
                                        self.passed[records.Current_Balance_Amount]["ENF"]=False
                        else:
                            if(records.Current_Balance_Amount):
                                if(len(str(records.Current_Balance_Amount).strip().lstrip().rstrip()) != 0):
                                    if("-" in records.Current_Balance_Amount):
                                        pass
                                    else:
                                        self.passed[records.Current_Balance_Amount]["FORMAT"]=checkformat.is_numeric(int(float(records.Current_Balance_Amount)))
                                else:
                                    self.passed[records.Current_Balance_Amount]["FORMAT"]=False
                            else:
                                self.passed[records.Current_Balance_Amount]["FORMAT"]=False
                #print self.passed
                yield self.passed     
                
            elif(f == "Current_Balance_Indicator"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Current_Balance_Indicator):
                                self.passed[records.Current_Balance_Indicator]={"Mandatory":True}
                            else:
                                self.passed[records.Current_Balance_Indicator]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Current_Balance_Indicator, priority=r.get(key))
                                self.passed[records.Current_Balance_Indicator]["ENF"]=self.statuss.validate_field(records)
                        else:
                            if(records.Current_Balance_Indicator):
                                if(len(str(records.Current_Balance_Indicator)) == 1):
                                    if(str(records.Current_Balance_Indicator).strip().lstrip().rstrip()):
                                        self.passed[records.Current_Balance_Indicator]["FORMAT"]=checkformat.is_numeric(int(float(records.Current_Balance_Indicator)))
                                    else:
                                        self.passed[records.Current_Balance_Indicator]["FORMAT"]=False
                                else:
                                    self.passed[records.Current_Balance_Indicator]["FORMAT"]=False
                            else:
                                self.passed[records.Current_Balance_Indicator]["FORMAT"]=False
                yield self.passed    
                 
            elif(f == "Last_Payment_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Last_Payment_Date):
                                self.passed[records.Last_Payment_Date]={"Conditional":True}
                            else:
                                self.passed[records.Last_Payment_Date]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Last_Payment_Date):
                                for key in r:
                                    #print key, r
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    self.third_priority = self.check_dict_values(r.get(key)[2])
                                    self.forth_priority = self.check_dict_values(r.get(key)[3])
                                    self.fifth_priority = self.check_dict_values(r.get(key)[4])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date, records=records)
                                        #print "FIRST ", self.validation_first
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date, records=records)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            #print "THIRD ", self.third_ef    
                                            self.validation_third = self.third_ef.validate_field(records=records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                            
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fourth = self.third_ef.validate_field(records, records.Credit_Account_Date)
                                            if(self.validation_fourth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                            
                                            self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fifth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                        else:
                                            self.passed[records.Last_Payment_Date]["ENF"]=False 
                                    
                                    elif(self.second_priority == 1 or self.second_priority == 2):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)

                                        if(self.validation_second == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)

                                            if(self.validation_first == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records=records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fourth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                                
                                            self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fifth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                                
                                        else:
                                            self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                    elif(self.third_priority == 1 or self.third_priority == 2):
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records=records)
                                        
                                        if(self.validation_third == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)

                                            if(self.validation_first == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                                
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)
                                            if(self.validation_second == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fourth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                                
                                            self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fifth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                                
                                        else:
                                            self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                    elif(self.forth_priority == 1 or self.third_priority==2):
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                        
                                        if(self.validation_fourth == True):
                                            self.passed[records.Last_Payment_Date]["ENF"]=False 
                                            
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)
                                            #perform the first enforcement validations
                                            if(self.validation_first == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                            
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)
                                            #perform the second validations
                                            if(self.validation_second == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records=records)
                                            if(self.validation_third == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                                
                                            self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fifth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                                
                                        else:
                                            self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                    elif(self.fifth_priority == 1 or self.fifth_priority == 2):
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                        
                                        if(self.validation_fifth == True):
                                            self.passed[records.Last_Payment_Date]["ENF"]=True
                                            
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)
                                            if(self.validation_second == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                                
                                            #First enforements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)
                                            #perform the first enforcement validations
                                            if(self.validation_first == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                            
                                            #Third enforcements  
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records=records)
                                            if(self.validation_third == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False 
                                            
                                            #Fofth enforcements
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                            self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                            if(self.validation_fourth == True):
                                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Last_Payment_Date]["ENF"]=False
                                        else:
                                            self.passed[records.Last_Payment_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Last_Payment_Date]["ENF"]=False
                            else:
                                self.passed[records.Last_Payment_Date]["ENF"]=True
                                
                        else:
                            if(records.Last_Payment_Date):
                                if(len(str(records.Last_Payment_Date)) <= 8):
                                    if(str(records.Last_Payment_Date).strip().lstrip().rstrip()):
                                        self.passed[records.Last_Payment_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Last_Payment_Date)))
                                    else:
                                        self.passed[records.Last_Payment_Date]["FORMAT"]=False
                                else:
                                    self.passed[records.Last_Payment_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Last_Payment_Date]["FORMAT"]=True
                yield self.passed    
                
            elif(f == "Last_Payment_Amount"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Last_Payment_Amount):
                                self.passed[records.Last_Payment_Amount]={"Conditional":True}
                            else:
                                self.passed[records.Last_Payment_Amount]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Last_Payment_Amount):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records)
                                        
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                        else:
                                            self.passed[records.Last_Payment_Amount]["ENF"]=False
                                            
                                        if(self.validation_first==True):
                                            if(self.validation_second == True):
                                                self.passed[records.Last_Payment_Amount]["ENF"]=True
                                            else:
                                                #Perform a logging
                                                self.passed[records.Last_Payment_Amount]["ENF"]=False
                                        else:
                                            self.passed[records.Last_Payment_Amount]["ENF"]=False 
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                        
                                        self.validation_first = self.vstatus.validate_field(records)
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        
                                        if(self.validation_second==True):
                                            if(self.validation_first == True):
                                                self.passed[records.Last_Payment_Amount]["ENF"]=True
                                            else:
                                                #Perform a logging
                                                self.passed[records.Last_Payment_Amount]["ENF"]=False
                                        else:
                                            self.passed[records.Last_Payment_Amount]["ENF"]=False
                            else:
                                self.passed[records.Last_Payment_Amount]["ENF"]=True 

                        else:
                            if(records.Last_Payment_Amount):
                                if(len(records.Last_Payment_Amount) <= 21):
                                    if(str(records.Last_Payment_Amount).strip().lstrip().rstrip()):
                                        self.passed[records.Last_Payment_Amount]["FORMAT"]=checkformat.is_numeric(int(float(records.Last_Payment_Amount)))
                                    else:
                                        self.passed[records.Last_Payment_Amount]["FORMAT"]=False
                                else:
                                    self.passed[records.Last_Payment_Amount]["FORMAT"]=False
                            else:
                                self.passed[records.Last_Payment_Amount]["FORMAT"]=True
                yield self.passed   
                  
            elif(f == "Credit_Account_Status"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Account_Status):
                                self.passed[records.Credit_Account_Status]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Account_Status]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                self.forth_priority = self.check_dict_values(r.get(key)[3])
                                self.fifth_priority = self.check_dict_values(r.get(key)[4])
                                self.sixth_priority = self.check_dict_values(r.get(key)[5])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        #print "First phase validation has passsed."
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        #print "SECOND PHASE ", self.sec_enf
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        
                                        if(self.validation_second == True):
                                            #print "Second phase validation has passed."
                                            self.passed[records.Credit_Account_Status]["ENF"]=True 
                                        else:
                                            #print "Second phase validation has passed."
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        
                                        if(self.validation_third == True):
                                           # print "Third phase validation has passed."
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            #print "Third phase validation has failed.", self.third_ef
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fourth = self.fourth_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            #print "Forth phase validation has passed."
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            #print "Forth phase validation has failed.", self.fourth_ef
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            #print "Fifth phase validation has passed."
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            #print "Fifth phase validation has failed.", self.fifth_ef
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                        if(self.validation_sixth == True):
                                            #print "Sixth phase validation has passed.", self.six_ef
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            #print "Sixth phase validation has fialed.", self.six_ef
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Credit_Account_Status]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)

                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                        
                                        self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                        if(self.validation_sixth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)

                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fourth = self.fourth_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                        if(self.validation_sixth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                elif(self.forth_priority == 1 or self.third_priority==2):
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records)
                                    
                                    if(self.validation_fourth == True):
                                        self.passed[records.Credit_Account_Status]["ENF"]=False 
                                        
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        #perform the second validations
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                        
                                        self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                        if(self.validation_sixth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                elif(self.fifth_priority == 1 or self.fifth_priority == 2):
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    
                                    if(self.validation_fifth == True):
                                        self.passed[records.Credit_Account_Status]["ENF"]=True
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Status)
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        #First enforements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                        #Third enforcements  
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                        
                                        #Fofth enforcements
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fourth = self.fourth_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                        if(self.validation_sixth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                elif(self.sixth_priority == 1 or self.sixth_priority == 2):
                                    self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_sixth == True):
                                        self.passed[records.Credit_Account_Status]["ENF"]=True
                                            
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                            
                                        #First enforements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False
                                        
                                        #Third enforcements  
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status)
                                        if(self.validation_third == True):
                                            self.passed[records.Last_Payment_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Last_Payment_Date]["ENF"]=False 
                                        
                                        #Fofth enforcements
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                        
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Status]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Status]["ENF"]=False 
                                else:
                                    self.passed[records.Credit_Account_Status]["ENF"]=False
                        else:
                            if(records.Credit_Account_Status):
                                if(len(str(records.Credit_Account_Status)) == 1):
                                    if(str(records.Credit_Account_Status).strip().lstrip().rstrip()):
                                        self.passed[records.Credit_Account_Status]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Status)))
                                    else:
                                        self.passed[records.Credit_Account_Status]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Account_Status]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Status]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Last_Status_Change_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Last_Status_Change_Date):
                                self.passed[records.Last_Status_Change_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Last_Status_Change_Date]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        #print "First phase validation has passed."
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field_cba(records.Last_Status_Change_Date, records)
                                        
                                        if(self.validation_second == True):
                                            #print "Seconf phase validation has passed"
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=True 
                                        else:
                                            #print "Second phase validation has failed"
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date)
                                        
                                        if(self.validation_third == True):
                                            #print "Third phase validation has passed."
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=True
                                        else:
                                            #print "Third phase validation has failed.", self.third_ef
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=False 
                                    else:
                                        #print "Fist phase validation has failed."
                                        self.passed[records.Last_Status_Change_Date]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Last_Status_Change_Date]["ENF"]=False
                                else:
                                    self.passed[records.Last_Status_Change_Date]["ENF"]=False
                        else:
                            if(records.Last_Status_Change_Date):
                                if(len(str(records.Last_Status_Change_Date)) <= 8):
                                    if(str(records.Last_Status_Change_Date).strip().lstrip().rstrip()):
                                        self.passed[records.Last_Status_Change_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Last_Status_Change_Date)))
                                    else:
                                        self.passed[records.Last_Status_Change_Date]["FORMAT"]=False
                                else:
                                    self.passed[records.Last_Status_Change_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Last_Status_Change_Date]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Credit_Account_Risk_Classification"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Account_Risk_Classification):
                                self.passed[records.Credit_Account_Risk_Classification]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Account_Risk_Classification]={"Mandatory":False}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Account_Risk_Classification, priority=r.get(key))
                                self.passed[records.Credit_Account_Risk_Classification]["ENF"]=self.statuss.validate_field(records.Credit_Account_Risk_Classification)
                        else:
                            if(records.Credit_Account_Risk_Classification):
                                if(len(str(records.Credit_Account_Risk_Classification)) == 1):
                                    if(str(records.Credit_Account_Risk_Classification).strip().rstrip().lstrip()):
                                        self.passed[records.Credit_Account_Risk_Classification]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Risk_Classification)))
                                    else:
                                        self.passed[records.Credit_Account_Risk_Classification]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Account_Risk_Classification]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Risk_Classification]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Credit_Account_Arrears_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Credit_Account_Arrears_Date):
                                self.passed[records.Credit_Account_Arrears_Date]={"Conditional":True}
                            else:
                                self.passed[records.Credit_Account_Arrears_Date]={"Conditional":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                self.forth_priority = self.check_dict_values(r.get(key)[3])
                                self.fifth_priority = self.check_dict_values(r.get(key)[4])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field_cba(records.Credit_Account_Arrears_Date, records)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        #print "Phase one validation has passed."
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date, records=records)
                                        
                                        if(self.validation_second == True):
                                            #print "Phase two validation has passed"
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True 
                                        else:
                                            #print "Phase two validation has failed"
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        
                                        if(self.validation_third == True):
                                            #print "Phase three validatioin has passed"
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            #print "Phase three validation has failed."
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            #print "Phase four validation has passed."
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            #print "Phase four validation has failed."
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            #print "Phase five validation has passed."
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            #print "Phase five validation has failed."
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                    else:
                                        #print "Phase one validation has failed"
                                        self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                        
                                elif(self.forth_priority == 1 or self.third_priority==2):
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                    
                                    if(self.validation_fourth == True):
                                        self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                        
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date)
                                        #perform the second validations
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                        
                                elif(self.fifth_priority == 1 or self.fifth_priority == 2):
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    
                                    if(self.validation_fifth == True):
                                        self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                            
                                        #First enforements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                        
                                        #Third enforcements  
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False 
                                        
                                        #Fofth enforcements
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False
                                else:
                                    self.passed[records.Credit_Account_Arrears_Date]["ENF"]=False

                        else:
                            if(records.Credit_Account_Arrears_Date):
                                if(len(str(records.Credit_Account_Arrears_Date)) <= 8):
                                    if(str(records.Credit_Account_Arrears_Date).strip().lstrip().rstrip()):
                                        self.passed[records.Credit_Account_Arrears_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Arrears_Date)))
                                    else:
                                        self.passed[records.Credit_Account_Arrears_Date]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Account_Arrears_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Arrears_Date]["FORMAT"]=False
                #print self.passed 
                yield self.passed     
                
            elif(f == "Number_of_Days_in_Arrears"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Number_of_Days_in_Arrears):
                                self.passed[records.Number_of_Days_in_Arrears]={"Conditional":True}
                            else:
                                self.passed[records.Number_of_Days_in_Arrears]={"Conditional":True} 
                        elif(isinstance(r, dict)):
                            if(records.Number_of_Days_in_Arrears):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Number_of_Days_in_Arrears, priority=r.get(key))
                                    self.passed[records.Number_of_Days_in_Arrears]["ENF"]=self.statuss.validate_field(records.Number_of_Days_in_Arrears, records=records)    
                            else:
                                self.passed[records.Number_of_Days_in_Arrears]["ENF"]=True
                        else:
                            if(records.Number_of_Days_in_Arrears):
                                if(len(str(records.Number_of_Days_in_Arrears)) <= 10):
                                    if(str(records.Number_of_Days_in_Arrears).strip().lstrip().rstrip()):
                                        self.passed[records.Number_of_Days_in_Arrears]["FORMAT"]=checkformat.is_numeric(int(float(records.Number_of_Days_in_Arrears)))
                                    else:
                                        self.passed[records.Number_of_Days_in_Arrears]["FORMAT"]=False
                                else:
                                    self.passed[records.Number_of_Days_in_Arrears]["FORMAT"]=False
                            else:
                                self.passed[records.Number_of_Days_in_Arrears]["FORMAT"]=True
                yield self.passed    
                
            elif(f == "Balance_Overdue"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Balance_Overdue):
                                self.passed[records.Balance_Overdue]={"Conditional":True}
                            else:
                                self.passed[records.Balance_Overdue]={"Conditional":True} 
                        elif(isinstance(r, dict)):
                            if(records.Balance_Overdue):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Balance_Overdue, priority=r.get(key))
                                    self.passed[records.Balance_Overdue]["ENF"]=self.statuss.validate_field(records.Balance_Overdue, records=records)
                            else:
                                self.passed[records.Balance_Overdue]["ENF"]=True
                        else:
                            if(records.Balance_Overdue):
                                if(len(str(records.Balance_Overdue)) <= 21):
                                    if(str(records.Balance_Overdue).strip().rstrip().lstrip()):
                                        self.passed[records.Balance_Overdue]["FORMAT"]=checkformat.is_numeric(int(float(records.Balance_Overdue)))
                                    else:
                                        self.passed[records.Balance_Overdue]["FORMAT"]=False
                                else:
                                    self.passed[records.Balance_Overdue]["FORMAT"]=False
                            else:
                                self.passed[records.Balance_Overdue]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Flag_for_Restructured_Credit"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Flag_for_Restructured_Credit):
                                self.passed[records.Flag_for_Restructured_Credit]={"Mandatory":True}
                            else:
                                self.passed[records.Flag_for_Restructured_Credit]={"Mandatory":False}
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Flag_for_Restructured_Credit, priority=r.get(key))
                                self.passed[records.Flag_for_Restructured_Credit]["ENF"]=self.statuss.validate_field(records.Flag_for_Restructured_Credit)
                        else:
                            if(records.Flag_for_Restructured_Credit):
                                if(len(str(records.Flag_for_Restructured_Credit)) == 1):
                                    if(str(records.Flag_for_Restructured_Credit).strip().lstrip().rstrip()):
                                        self.passed[records.Flag_for_Restructured_Credit]["FORMAT"]=checkformat.is_numeric(int(float(records.Flag_for_Restructured_Credit)))
                                    else:
                                        self.passed[records.Flag_for_Restructured_Credit]["FORMAT"]=False
                                else:
                                    self.passed[records.Flag_for_Restructured_Credit]["FORMAT"]=False
                            else:
                                self.passed[records.Flag_for_Restructured_Credit]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Old_Branch_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Old_Branch_Code):
                                self.passed[records.Old_Branch_Code]={"Conditional":True}
                            else:
                                self.passed[records.Old_Branch_Code]={"Conditional":True} 
                        elif(isinstance(r, dict)):
                            if(records.Old_Branch_Code):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Old_Branch_Code, priority=r.get(key))
                                    self.passed[records.Old_Branch_Code]["ENF"]=self.statuss.validate_field(records.Old_Branch_Code, records)
                            else:
                                self.passed[records.Old_Branch_Code]["ENF"]=True
                        else:
                            if(records.Old_Branch_Code):
                                if(len(str(records.Old_Branch_Code)) <= 10):
                                    self.passed[records.Old_Branch_Code]["FORMAT"]=checkformat.sub_alphanumeric(records.Old_Branch_Code)
                                else:
                                    self.passed[records.Old_Branch_Code]["FORMAT"]=False
                            else:
                                self.passed[records.Old_Branch_Code]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Old_Account_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Old_Account_Number):
                                self.passed[records.Old_Account_Number]={"Conditional":True}
                            else:
                                self.passed[records.Old_Account_Number]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Old_Account_Number):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Old_Account_Number, priority=r.get(key))
                                    self.passed[records.Old_Account_Number]["ENF"]=self.statuss.validate_field(records.Old_Account_Number, records=records)
                            else:
                                self.passed[records.Old_Account_Number]["ENF"]=True
                        else:
                            if(records.Old_Account_Number):
                                if(len(str(records.Old_Account_Number)) <= 30):
                                    self.passed[records.Old_Account_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.Old_Account_Number)
                                else:
                                    self.passed[records.Old_Account_Number]["FORMAT"]=False
                            else:
                                self.passed[records.Old_Account_Number]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Old_Client_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.Old_Client_Number):
                                self.passed[records.Old_Client_Number]={"Optional":True}
                            else:
                                self.passed[records.Old_Client_Number]={"Optional":True} 
                        elif(isinstance(r, dict)):
                            if(records.Old_Client_Number):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Old_Client_Number, priority=r.get(key))
                                    self.passed[records.Old_Client_Number]["ENF"]=self.statuss.validate_field(records.Old_Client_Number, records=records)
                            else:
                                self.passed[records.Old_Client_Number]["ENF"]=True
                        else:
                            if(records.Old_Client_Number):
                                if(len(str(records.Old_Client_Number)) <= 30):
                                    self.passed[records.Old_Client_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.Old_Client_Number)
                                else:
                                    self.passed[records.Old_Client_Number]["FORMAT"]=True
                            else:
                                self.passed[records.Old_Client_Number]["FORMAT"]=True
                #print self.passed #Old client number
                yield self.passed     
                
            elif(f == "Balance_Overdue_Indicator"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Balance_Overdue_Indicator):
                                self.passed[records.Balance_Overdue_Indicator]={"Conditional":True}
                            else:
                                self.passed[records.Balance_Overdue_Indicator]={"Conditional":True}
                            
                        elif(isinstance(r, dict)):
                            if(records.Balance_Overdue_Indicator):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records)
                                        
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            #print "First phase validation has passed."#, self.vstatus
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            if(self.validation_second == True):
                                                #print "Seconf phase validation has also passed."#, self.sec_enf
                                                self.passed[records.Balance_Overdue_Indicator]["ENF"]=True
                                            else:
                                                #Perform a logging
                                                #print "Second phase validation has failed "
                                                self.passed[records.Balance_Overdue_Indicator]["ENF"]=False
                                        else:
                                            #print "First phase validation has failed."
                                            self.passed[records.Balance_Overdue_Indicator]["ENF"]=False
                                            
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                        
                                        self.validation_first = self.vstatus.validate_field(records)
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        
                                        if(self.validation_second==True):
                                            if(self.validation_first == True):
                                                self.passed[records.Balance_Overdue_Indicator]["ENF"]=True
                                            else:
                                                #Perform a logging
                                                self.passed[records.Balance_Overdue_Indicator]["ENF"]=False
                                        else:
                                            self.passed[records.Balance_Overdue_Indicator]["ENF"]=False
                            else:
                                self.passed[records.Balance_Overdue_Indicator]["ENF"]=True

                        else:
                            if(records.Balance_Overdue_Indicator):
                                if(len(str(records.Balance_Overdue_Indicator)) <= 8):
                                    if(str(records.Balance_Overdue_Indicator)):
                                        self.passed[records.Balance_Overdue_Indicator]["FORMAT"]=checkformat.is_numeric(int(float(records.Balance_Overdue_Indicator)))
                                    else:
                                        self.passed[records.Balance_Overdue_Indicator]["FORMAT"]=False
                                else:
                                    self.passed[records.Balance_Overdue_Indicator]["FORMAT"]=False
                            else:
                                self.passed[records.Balance_Overdue_Indicator]["FORMAT"]=T
                #print self.passed 
                yield self.passed    
                
            elif(f == "Credit_Account_Closure_Date"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Credit_Account_Closure_Date):
                                self.passed[records.Credit_Account_Closure_Date]={"Conditional":True}
                            else:
                                self.passed[records.Credit_Account_Closure_Date]={"Conditional":True}
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.Credit_Account_Closure_Date):
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    self.third_priority = self.check_dict_values(r.get(key)[2])
                                    self.forth_priority = self.check_dict_values(r.get(key)[3])
                                  
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        #print "ACCOUNT ", r.get(key)[0]
                                        self.validation_first = self.vstatus.validate_field_cba(records.Credit_Account_Closure_Date, credit_field=records)
                                        
                                        if(self.validation_first == True):
                                            #print "First phase validation has passed ", self.vstatus
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            #print "VALIDTE ", r.get(key)[1]
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            
                                            if(self.validation_second == True):
                                                #print "Second phase validation has passed..", self.sec_enf
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True 
                                            else:
                                                #print "Second phase validation has failed."
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                            
                                            if(self.validation_third == True):
                                                #print "Third phase validation has passed..", self.third_ef
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                #print "Third phase validation has passed.."
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                                
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_fourth = self.fourth_ef.validate_field(records.Credit_Account_Closure_Date, records=records)
                                            if(self.validation_fourth == True):
                                                #print "Forth phase validation has passed.", self.fourth_ef
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                #print "Forth phase validation has failed."
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                        else:
                                            #print "first phase validation has failed", self.vstatus
                                            self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                    
                                    elif(self.second_priority == 1 or self.second_priority == 2):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)

                                        if(self.validation_second == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field_cba(records.Credit_Account_Closure_Date, credit_field=records)

                                            if(self.validation_first == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                            
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_fourth = self.fourth_ef.validate_field(records.Credit_Account_Closure_Date, records=records)
                                            if(self.validation_fourth == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                                
                                        else:
                                            self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                            
                                    elif(self.third_priority == 1 or self.third_priority == 2):
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                        
                                        if(self.validation_third == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Date)

                                            if(self.validation_first == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                                
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            if(self.validation_second == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                            
                                            self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_fourth = self.fourth_ef.validate_field(records.Credit_Account_Closure_Date, records=records)
                                            if(self.validation_fourth == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                                
                                        else:
                                            self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                            
                                    elif(self.forth_priority == 1 or self.third_priority==2):
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_fourth = self.fourth_ef.validate_field(records.Credit_Account_Closure_Date, records=records)
                                        
                                        if(self.validation_fourth == True):
                                            self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Date)
                                            
                                            #perform the first enforcement validations
                                            if(self.validation_first == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                            
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            
                                            #perform the second validations
                                            if(self.validation_second == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True 
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Date]["ENF"]=False 
                                        else:
                                            self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Account_Closure_Date]["ENF"]=False
                                else:
                                    self.passed[records.Credit_Account_Closure_Date]["ENF"]=True
                        else:
                            if(records.Credit_Account_Closure_Date):
                                if(len(records.Credit_Account_Closure_Date) <= 8):
                                    if(str(records.Credit_Account_Closure_Date).strip().rstrip().lstrip()):
                                        self.passed[records.Credit_Account_Closure_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Closure_Date)))
                                    else:
                                        self.passed[records.Credit_Account_Closure_Date]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Account_Closure_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Closure_Date]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Credit_Account_Closure_Reason"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Credit_Account_Closure_Reason):
                                self.passed[records.Credit_Account_Closure_Reason]={"Conditional":True}
                            else:
                                self.passed[records.Credit_Account_Closure_Reason]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Credit_Account_Closure_Reason):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    self.third_priority = self.check_dict_values(r.get(key)[2])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        #print "It's True "
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Reason)
                                        
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            #print "First Phase validation has passed"
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date, records.Credit_Account_Closure_Reason)
                                            
                                            if(self.validation_second == True):
                                                #print "Second phase validation has passed"
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True 
                                            else:
                                                #print "Second phase validation has failed.", self.sec_enf
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status, records.Credit_Account_Closure_Reason)
                                            
                                            if(self.validation_third == True):
                                                #print "Third phase validation has passed"
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True
                                            else:
                                                #print "Third phase validation has failed.", self.third_ef
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False 
                                        else:
                                            #print "First phase validation has failed", self.vstatus
                                            self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False 
                                    
                                    elif(self.second_priority == 1 or self.second_priority == 2):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Date_of_First_Payment)

                                        if(self.validation_second == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Date, records.Credit_Account_Closure_Reason)

                                            if(self.validation_first == True):
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True 
                                            else:
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status, records.Credit_Account_Closure_Reason)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                                
                                        else:
                                            self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                            
                                    elif(self.third_priority == 1 or self.third_priority == 2):
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status, records.Credit_Account_Closure_Reason)
                                        
                                        if(self.validation_third == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Reason)

                                            if(self.validation_first == True):
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True 
                                            else:
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                                
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date, records.Credit_Account_Closure_Reason)
                                            if(self.validation_second == True):
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True
                                            else:
                                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                        else:
                                            self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Account_Closure_Reason]["ENF"]=False
                            else:
                                self.passed[records.Credit_Account_Closure_Reason]["ENF"]=True

                        else:
                            if(records.Credit_Account_Closure_Reason):
                                if(len(records.Credit_Account_Closure_Reason) == 1):
                                    if(str(records.Credit_Account_Closure_Reason).strip().lstrip().rstrip()):
                                        self.passed[records.Credit_Account_Closure_Reason]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Closure_Reason)))
                                    else:
                                        self.passed[records.Credit_Account_Closure_Reason]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Account_Closure_Reason]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_Closure_Reason]["FORMAT"]=True
                yield self.passed     
                
            elif(f == "Specific_Provision_Amount"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Specific_Provision_Amount):
                                self.passed[records.Specific_Provision_Amount]={"Conditional":True}
                            else:
                                self.passed[records.Specific_Provision_Amount]={"Conditional":True}
                            
                        elif(isinstance(r, dict)):
                            #self.statuss = checkenforcements.check_enforcements(r, self.pi_c_code, records.Specific_Provision_Amount)    
                            #self.passed["ENF"]=self.statuss.validate_field(records.Specific_Provision_Amount)
                            #if(self.status):
                            self.passed[records.Specific_Provision_Amount]["ENF"]=True
                            #self.statuss.validate_field(records.Specific_Provision_Amount)
                            #else:
                            #    self.passed["ENF"]=None
                        else:
                            if(records.Specific_Provision_Amount):
                                if(len(str(records.Specific_Provision_Amount)) <= 21):
                                    self.passed[records.Specific_Provision_Amount]["FORMAT"]=checkformat.is_numeric(int(float(records.Specific_Provision_Amount)))
                                else:
                                    self.passed[records.Specific_Provision_Amount]["FORMAT"]=False
                            else:
                                self.passed[records.Specific_Provision_Amount]["FORMAT"]=True
                yield self.passed   
                 
            elif(f == "Client_Consent_Flag"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Client_Consent_Flag):
                                self.passed[records.Client_Consent_Flag]={"Mandatory":True}
                            else:
                                self.passed[records.Client_Consent_Flag]={"Mandatory":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Consent_Flag, priority=r.get(key))
                                self.passed[records.Client_Consent_Flag]["ENF"]=self.statuss.validate_field(records.Client_Consent_Flag)    

                        else:
                            if(records.Client_Consent_Flag):
                                if(len(str(records.Client_Consent_Flag)) <= 10):
                                    self.passed[records.Client_Consent_Flag]["FORMAT"]=checkformat.sub_alphanumeric(records.Client_Consent_Flag)
                                else:
                                    self.passed[records.Client_Consent_Flag]["FORMAT"]=False
                            else:
                                self.passed[records.Client_Consent_Flag]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Client_Advice_Notice_Flag"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Client_Advice_Notice_Flag):
                                self.passed[records.Client_Advice_Notice_Flag]={"Mandatory":True}
                            else:
                                self.passed[records.Client_Advice_Notice_Flag]={"Mandatory":False}
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Advice_Notice_Flag, priority=r.get(key))
                                self.passed[records.Client_Advice_Notice_Flag]["ENF"]=self.statuss.validate_field(records.Client_Advice_Notice_Flag)    
                        else:
                            if(records.Client_Advice_Notice_Flag):
                                if(len(str(records.Client_Advice_Notice_Flag)) <= 5):
                                    self.passed[records.Client_Advice_Notice_Flag]["FORMAT"]=checkformat.sub_alphanumeric(records.Client_Advice_Notice_Flag)
                                else:
                                    self.passed[records.Client_Advice_Notice_Flag]["FORMAT"]=False
                            else:
                                self.passed[records.Client_Advice_Notice_Flag]["FORMAT"]=False
                yield self.passed     
                
            elif(f == "Term"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Term):
                                self.passed[records.Term]={"Conditional":True}
                            else:
                                self.passed[records.Term]={"Conditional":True}
                        elif(isinstance(r, dict)):
                            if(records.Term):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Term, priority=r.get(key))
                                    self.passed[records.Term]["ENF"]=self.statuss.validate_field(records, records=records)
                            else:
                                self.passed[records.Term]["ENF"]=True #self.statuss.validate_field(records.Term)
                        else:
                            if(records.Term):
                                if(len(str(records.Term)) <= 50):
                                    if(str(records.Term).strip().lstrip().rstrip()):
                                        self.passed[records.Term]["FORMAT"]=checkformat.is_numeric(int(float(records.Term)))
                                    else:
                                        self.passed[records.Term]["FORMAT"]=False
                                else:
                                    self.passed[records.Term]["FORMAT"]=False
                            else:
                                self.passed[records.Term]["FORMAT"]=True
                yield self.passed  
                   
            elif(f == "Loan_Purpose"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Loan_Purpose):
                                self.passed[records.Loan_Purpose]={"Mandatory":True}
                            else:
                                self.passed[records.Loan_Purpose]={"Mandatory":False}
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Loan_Purpose, priority=r.get(key))
                                self.passed[records.Loan_Purpose]["ENF"]=self.statuss.validate_field(records.Loan_Purpose)
                        else:
                            if(len(str(records.Loan_Purpose).strip().lstrip().rstrip()) <= 15):
                                if(str(records.Loan_Purpose).strip().lstrip().rstrip()):
                                    self.passed[records.Loan_Purpose]["FORMAT"]=checkformat.is_numeric(int(float(records.Loan_Purpose)))
                                else:
                                    self.passed[records.Loan_Purpose]["FORMAT"]=False
                            else:
                                self.passed[records.Loan_Purpose]["FORMAT"]=False
                yield self.passed     
            else:
                pass
        except Exception as e:
            # Log
            pass  
