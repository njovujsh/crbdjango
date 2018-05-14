from validators.subsystems import cbacode  
from datasetrecords import models 
from validators.subsystems import checkstatus 
from validators.subsystems import checkformat 
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate 
from validators.subsystems.enforcements import enf007
from validators.subsystems.datasets import validationstatus
from validators.subsystems.datasets import ibvalidate
from creditreports.subsystems import pivalidatereport 

class ReportCBAValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="CBA"):
        super(ReportCBAValidate, self).__init__()
        self.cba_model = models.CREDITBORROWERACCOUNT
        self.all_records = models.CREDITBORROWERACCOUNT.objects.all()
        self.code = code 
        self.pi_c_code = cbacode.CBACode(self.cba_model, self.code)
        self.all_count = models.CREDITBORROWERACCOUNT.objects.all().count()
        #set the code on use
        self.record_fields = 45 
        self.set_code(self.pi_c_code)
      
    def begin_validation(self):
        try:
            self.all_fields = self.pi_c_code.extract()
            self.examine_field(self.all_fields)
        except:
            pass
            
    def check_data_in_field(self, f, rules):
        
        self.passed = {}
        self.all_records_passed = {}
        self.final_result={}
        try:
            self.PI_Identification_Code(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Borrowers_Client_Number(f, rules)
            self.Borrower_Classification(f, rules) 
            self.Credit_Account_Reference(f, rules) 
            self.Credit_Account_Date(f, rules) 
            self.Credit_Amount(f, rules) 
            self.Facility_Amount_Granted(f, rules) 
            self.Credit_Account_Type(f, rules) 
            self.Group_Identification_Joint_Account_Number(f, rules) 
            self.Transaction_Date(f, rules) 
            self.Currency(f, rules) 
            self.Opening_Balance_Indicator(f, rules) 
            self.Maturity_Date(f, rules) 
            self.Type_of_Interest(f, rules) 
            self.Interest_Calculation_Method(f, rules) 
            self.Annual_Interest_Rate_at_Disbursement(f, rules) 
            self.Annual_Interest_Rate_at_Reporting(f, rules) 
            self.Date_of_First_Payment(f, rules) 
            self.Credit_Amortization_Type(f, rules) 
            self.Credit_Payment_Frequency(f, rules) 
            self.Number_of_Payments(f, rules) 
            self.Monthly_Instalment_Amount(f, rules) 
            self.Current_Balance_Amount(f, rules) 
            self.Current_Balance_Indicator(f, rules) 
            self.Last_Payment_Date(f, rules) 
            self.Last_Payment_Amount(f, rules) 
            self.Credit_Account_Status(f, rules) 
            self.Last_Status_Change_Date(f, rules) 
            self.Credit_Account_Risk_Classification(f, rules) 
            self.Credit_Account_Arrears_Date(f, rules) 
            self.Number_of_Days_in_Arrears(f, rules) 
            self.Balance_Overdue(f, rules) 
            self.Flag_for_Restructured_Credit(f, rules) 
            self.Old_Branch_Code(f, rules) 
            self.Old_Account_Number(f, rules) 
            self.Old_Client_Number(f, rules) 
            self.Balance_Overdue_Indicator(f, rules) 
            self.Credit_Account_Closure_Date(f, rules) 
            self.Credit_Account_Closure_Reason(f, rules) 
            self.Specific_Provision_Amount(f, rules) 
            self.Client_Consent_Flag(f, rules) 
            self.Client_Advice_Notice_Flag(f, rules) 
            self.Term(f, rules) 
            self.Loan_Purpose(f, rules)

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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code)
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                    else:
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata)  <= 8):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(self.parseddata)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_list = []
                self.passed_list.append(self.passed.get(keys).values().count(True))
                self.passed_by_id[keys]=self.passed_list
                #print "FINAL 1", self.passed_by_id.get(keys)
                
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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code)
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)
                    else:
                        if(len(records.Branch_Identification_Code.branch_code) <= 15):
                            self.passed[records.id]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
                
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #.append(self.passed.get(keys).values().count(True))
                #print "2 ", self.passed_list
                #print "FINAL 2", self.passed_by_id.get(keys)
            
    def Borrowers_Client_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Borrowers_Client_Number"):
                for r in rules:
                    if(records.Borrowers_Client_Number):
                        if r == "M":
                            if(records.Borrowers_Client_Number.Client_Number):
                                self.passed[records.id]={"Mandatory":True}
                            else:
                                self.passed[records.id]={"Mandatory":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrowers_Client_Number.Client_Number)
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Borrowers_Client_Number.Client_Number)
                        else:
                            if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrowers_Client_Number.Client_Number)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                    self.final_result[records.id]=self.passed
        #print "All count ", self.all_count
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 3", self.passed_by_id.get(keys)
        else:
            print "PASSED ", self.passed  
            
    def Borrower_Classification(self, f, rules):
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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Classification)
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Borrower_Classification)
                    else:
                        if(len(records.Borrower_Classification) == 1):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Borrower_Classification)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
                 
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print keys, "FINAL 4 KEY ", self.passed.get(keys).values(),  self.passed.get(keys).values().count(True), "LENG", self.passed_by_id.get(keys)
                #print "FINAL 4", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Credit_Account_Reference(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Reference"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Account_Reference):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                         for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self.pi_c_code, records.Credit_Account_Reference)
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Account_Reference)
                            #print self.statuss                   
                    else:
                        if(len(records.Credit_Account_Reference) <= 30):
                            self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Credit_Account_Reference)
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 5", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Credit_Account_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Account_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False} 
                        
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
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Credit_Account_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Date, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                    else:
                        if(records.Credit_Account_Date):
                            if(len(records.Credit_Account_Date) <= 8):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Date)))
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
                 
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 6", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Credit_Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Amount"):
                for r in rules:
                    if r == "C":
                        if(records.Credit_Amount):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True}
                    elif(isinstance(r, dict)):
                        if(records.Credit_Amount):
                            for key in r:
                                #print key,r
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Amount, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Amount, records=records)
                                #print self.statuss
                        else:
                            self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Credit_Amount):
                            if(len(records.Credit_Amount) <= 21):
                                if(records.Credit_Amount.strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Amount)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
                 
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 7", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Facility_Amount_Granted(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Facility_Amount_Granted"):
                for r in rules:
                    if(records.Borrowers_Client_Number):
                        if r == "C":
                            if(records.Facility_Amount_Granted):
                                self.passed[records.id]={"Conditional":True}
                            else:
                                self.passed[records.id]={"Conditional":True} 
                        elif(isinstance(r, dict)):
                            if(records.Facility_Amount_Granted):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Facility_Amount_Granted, priority=r.get(key))
                                    self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Facility_Amount_Granted, more_validation=records)
                            else:
                                self.passed[records.id]["ENF"]=True
                        else:
                            if(records.Facility_Amount_Granted):
                                if(len(records.Facility_Amount_Granted) <= 21):
                                    if(str(records.Facility_Amount_Granted).strip().lstrip().rstrip()):
                                        self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Facility_Amount_Granted)))
                                    else:
                                        self.passed[records.id]["FORMAT"]=False
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=True
                    self.final_result[records.id]=self.passed
                 
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 8", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Credit_Account_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Account_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Account_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Account_Type)
                    else:
                        if(records.Credit_Account_Type):
                            if(len(records.Credit_Account_Type) <= 2):
                                if(records.Credit_Account_Type.strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Type)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed 
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 9", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Group_Identification_Joint_Account_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Group_Identification_Joint_Account_Number"):
                for r in rules:
                    if r == "C":
                        if(records.Borrower_Classification == "1"):
                            if(records.Group_Identification_Joint_Account_Number):
                                self.passed[records.id]={"Conditional":True}
                            else:
                                self.passed[records.id]={"Conditional":False}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            if(records.Borrower_Classification == "1"):
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Group_Identification_Joint_Account_Number, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Group_Identification_Joint_Account_Number, records)
                            else:
                                self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Group_Identification_Joint_Account_Number, records)
                    else:
                        if(records.Borrower_Classification == "1"):
                            if(len(str(records.Group_Identification_Joint_Account_Number)) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Group_Identification_Joint_Account_Number)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 10", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Transaction_Date(self, f, rules): 
        self.passed = {}
        for records in self.all_records:
            if(f == "Transaction_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Transaction_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":True}
                        
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
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=True
                                else:
                                    self.passed[records.id]["ENF"]=True
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Transaction_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Transaction_Date, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Transaction_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Transaction_Date, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=True
                                else:
                                    self.passed[records.id]["ENF"]=True 
                    else:
                        if(records.Transaction_Date):
                            if(len(str(records.Transaction_Date)) <= 12):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Transaction_Date)))
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 11", self.passed_by_id.get(keys)
        else:
            pass 
    
    def Currency(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Currency"):
                for r in rules:
                    if r == "M":
                        if(records.Currency):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Currency, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Currency)
                                
                                if(self.validation_first == True):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Currency, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Currency)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Currency, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Currency, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Currency)
                                self.validation_second = self.sec_enf.validate_field(records.Currency, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                    else:
                        if(records.Currency):
                            if(len(str(records.Currency)) <= 5):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Currency)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 12", self.passed_by_id.get(keys)
        else:
            pass 
                  
    def Opening_Balance_Indicator(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Opening_Balance_Indicator"):
                for r in rules:
                    if r == "M":
                        if(records.Opening_Balance_Indicator):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False} 
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Opening_Balance_Indicator, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records)
                            #print self.statuss
                    else:
                        if(records.Opening_Balance_Indicator):
                            if(len(str(records.Opening_Balance_Indicator)) == 1):
                                if(str(records.Opening_Balance_Indicator).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Opening_Balance_Indicator)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False 
                            else:
                                self.passed[records.id]["FORMAT"]=False       
                        else:   
                            self.passed[records.id]["FORMAT"]=False        
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 13", self.passed_by_id.get(keys)
        else:
            pass 
                       
    def Maturity_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Maturity_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Maturity_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False} 
                        
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
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Maturity_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Maturity_Date, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Maturity_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Maturity_Date, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(records.Maturity_Date):
                            if(len(str(records.Maturity_Date)) <= 8):
                                if(str(records.Maturity_Date).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Maturity_Date)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 14 ", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Type_of_Interest(self, f, rules):   
        self.passed = {}
        for records in self.all_records:     
            if(f == "Type_of_Interest"):
                for r in rules:
                    if r == "M":
                        if(records.Type_of_Interest):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Type_of_Interest, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Type_of_Interest)

                    else:
                        if(records.Type_of_Interest):
                            if(len(records.Type_of_Interest) == 1):
                                if(str(records.Type_of_Interest).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Type_of_Interest)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 15", self.passed_by_id.get(keys)
        else:
            pass 

    def Interest_Calculation_Method(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Interest_Calculation_Method"):
                for r in rules:
                    if r == "M":
                        if(records.Interest_Calculation_Method):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Interest_Calculation_Method, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Interest_Calculation_Method)

                    else:
                        if(records.Interest_Calculation_Method):
                            if(len(records.Interest_Calculation_Method) == 1):
                                if(str(records.Interest_Calculation_Method).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Interest_Calculation_Method)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False 
                        else:                           
                            self.passed[records.id]["FORMAT"]=False  
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 16", self.passed_by_id.get(keys)
        else:
            pass 
                              
    def Annual_Interest_Rate_at_Disbursement(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Annual_Interest_Rate_at_Disbursement"):
                for r in rules:
                    if r == "M":
                        if(records.Annual_Interest_Rate_at_Disbursement):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Annual_Interest_Rate_at_Disbursement, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Annual_Interest_Rate_at_Disbursement)
                    else:
                        if(len(records.Annual_Interest_Rate_at_Disbursement) <= 12):
                            if(len(records.Annual_Interest_Rate_at_Disbursement) != 0):
                                self.passed[records.id]["FORMAT"]=checkformat.is_float(float(records.Annual_Interest_Rate_at_Disbursement))
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 17", self.passed_by_id.get(keys)
        else:
            pass 
                   
    def Annual_Interest_Rate_at_Reporting(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Annual_Interest_Rate_at_Reporting"):
                for r in rules:
                    if r == "M":
                        if(records.Annual_Interest_Rate_at_Reporting):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":True}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Annual_Interest_Rate_at_Reporting, priority=r.get(key))
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Annual_Interest_Rate_at_Reporting)

                    else:
                        if(records.Annual_Interest_Rate_at_Reporting):
                            if(len(records.Annual_Interest_Rate_at_Reporting) <= 10):
                                if(str(records.Annual_Interest_Rate_at_Reporting).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_float(float(records.Annual_Interest_Rate_at_Reporting))
                                else:
                                    self.passed[records.id]["FORMAT"]=True
                            else:
                                self.passed[records.id]["FORMAT"]=True
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL18 ", self.passed_by_id.get(keys)
        else:
            pass 
                    
    def Date_of_First_Payment(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Date_of_First_Payment"):
                for r in rules:
                    if r == "C":
                        if(records.Date_of_First_Payment):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                      
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
                                        self.validation_second = self.sec_enf.validate_field(records=records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Date_of_First_Payment,records=records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records=records)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Date_of_First_Payment,records=records)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Date_of_First_Payment,records=records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Date_of_First_Payment,records=records)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Date_of_First_Payment,records=records)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records=records)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                        else:
                            self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Date_of_First_Payment):
                            if(len(str(records.Date_of_First_Payment).strip().lstrip().rstrip()) <= 8):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Date_of_First_Payment)))
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 19", self.passed_by_id.get(keys)
        else:
            pass 
                
    def Credit_Amortization_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Amortization_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Amortization_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Amortization_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records)
                    else:
                        if(records.Credit_Amortization_Type):
                            if(len(str(records.Credit_Amortization_Type)) == 1):
                                if(str(records.Credit_Amortization_Type).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Amortization_Type)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL20 ", self.passed_by_id.get(keys)
        else:
            pass 
                
    def Credit_Payment_Frequency(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Payment_Frequency"):
                for r in rules:
                    if r == "C":
                        if(records.Credit_Payment_Frequency):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
                    elif(isinstance(r, dict)):
                        if(records.Credit_Payment_Frequency):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Payment_Frequency, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records)
                        else:
                            self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Credit_Payment_Frequency):
                            if(len(str(records.Credit_Payment_Frequency).strip().lstrip().rstrip()) <= 5):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Payment_Frequency)))
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL21 ", self.passed_by_id.get(keys)
        else:
            pass 
                
    def Number_of_Payments(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Number_of_Payments"):
                for r in rules:
                    if(records.Borrowers_Client_Number):
                        if r == "C":
                            if(records.Number_of_Payments):
                                self.passed[records.id]={"Conditional":True}
                            else:
                                self.passed[records.id]={"Conditional":True} 
                            
                        elif(isinstance(r, dict)):
                            if(records.Number_of_Payments):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Number_of_Payments, priority=r.get(key))
                                    self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Number_of_Payments, records=records)
                            else:
                                self.passed[records.id]["ENF"]=True
                        else:
                            if(records.Number_of_Payments):
                                if(len(records.Number_of_Payments) <= 4):
                                    if(str(records.Number_of_Payments).strip().lstrip().rstrip()):
                                        self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Number_of_Payments)))
                                    else:
                                        self.passed[records.id]["FORMAT"]=False
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=True
                    self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL22 ", self.passed_by_id.get(keys)
        else:
            pass 

    def Monthly_Instalment_Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:  
            if(f == "Monthly_Instalment_Amount"):
                for r in rules:
                    if(records.Borrowers_Client_Number):
                        if r == "C":
                            if(records.Monthly_Instalment_Amount):
                                self.passed[records.id]={"Conditional":True}
                            else:
                                self.passed[records.id]={"Conditional":True} 
                        elif(isinstance(r, dict)):
                            if(records.Monthly_Instalment_Amount):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Monthly_Instalment_Amount, priority=r.get(key))
                                    self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Monthly_Instalment_Amount, records)
                            else:
                                self.passed[records.id]["ENF"]=True
                        else:
                            if(records.Monthly_Instalment_Amount):
                                if(len(str(records.Monthly_Instalment_Amount)) <= 21):
                                    if(str(records.Monthly_Instalment_Amount).strip().lstrip().rstrip()):
                                        self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Monthly_Instalment_Amount)))
                                    else:
                                        self.passed[records.id]["FORMAT"]=False
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=True
                    self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 23", self.passed_by_id.get(keys)
        else:
            pass 
      
    def Current_Balance_Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Current_Balance_Amount"):
                for r in rules:
                    if r == "M":
                        if(records.Current_Balance_Amount):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
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
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Current_Balance_Amount, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Current_Balance_Amount, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records)
                                self.validation_second = self.sec_enf.validate_field(records)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                    else:
                        if(records.Current_Balance_Amount):
                            if("-" in records.Current_Balance_Amount):
                                self.replace_ = records.Current_Balance_Amount.replace("-", "", 10)
                                self.replaced = self.replace_.strip().lstrip().rstrip()
                                if(len(str(self.replaced)) != 0):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.replaced)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                if(len(str(records.Current_Balance_Amount)) != 0):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Current_Balance_Amount)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[recors.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass 
                
    def Current_Balance_Indicator(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Current_Balance_Indicator"):
                for r in rules:
                    if r == "M":
                        if(records.Current_Balance_Indicator):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Current_Balance_Indicator, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records)
                    else:
                        if(records.Current_Balance_Indicator):
                            if(len(records.Current_Balance_Indicator) == 1):
                                if(str(records.Current_Balance_Indicator).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Current_Balance_Indicator)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 25", self.passed_by_id.get(keys)
        else:
            pass 
                 
    def Last_Payment_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Last_Payment_Date"):
                for r in rules:
                    if r == "C":
                        if(records.Last_Payment_Date):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
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
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date,records=records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records=records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records, records.Credit_Account_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records=records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records=records)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.forth_priority == 1 or self.third_priority==2):
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                    
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=False 
                                        
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)
                                        #perform the second validations
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records=records)
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.fifth_priority == 1 or self.fifth_priority == 2):
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records.Last_Payment_Date)
                                    
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Payment_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        #First enforements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Payment_Date)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        #Third enforcements  
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records=records)
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        #Fofth enforcements
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Last_Payment_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Last_Payment_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                        else:
                            self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Last_Payment_Date):
                            if(len(str(records.Last_Payment_Date)) <= 8):
                                if(str(records.Last_Payment_Date).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Last_Payment_Date)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=True
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 26", self.passed_by_id.get(keys)
        else:
            pass 
                
    def Last_Payment_Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Last_Payment_Amount"):
                for r in rules:
                    if r == "C":
                        if(records.Last_Payment_Amount):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
                    elif(isinstance(r, dict)):
                        if(records.Last_Payment_Amount):
                            for key in r:
                                #print r
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    #print r.get(key)[0]
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    if(self.validation_first==True):
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            #Perform a logging
                                            self.passed[records.id]["ENF"]=False
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Payment_Amount, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records)
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    
                                    if(self.validation_second==True):
                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            #Perform a logging
                                            self.passed[records.id]["ENF"]=False
                                    else:
                                        self.passed[records.id]["ENF"]=False
                        else:
                            self.passed[records.id]["ENF"]=True

                    else:
                        if(records.Last_Payment_Amount):
                            if(len(str(records.Last_Payment_Amount).strip().lstrip().rstrip()) <= 21):
                                if(str(records.Last_Payment_Amount).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Last_Payment_Amount)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 27", self.passed_by_id.get(keys)
        else:
            pass 
                  
    def Credit_Account_Status(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Status"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Account_Status):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False} #robert@access access@robert
                        
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
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records)
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_sixth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            
                            elif(self.second_priority == 1 or self.second_priority == 2):
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                self.validation_second = self.sec_enf.validate_field(records)

                                if(self.validation_second == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                    
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                    
                                    self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_sixth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.third_priority == 1 or self.third_priority == 2):
                                self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                self.validation_third = self.third_ef.validate_field(records)
                                
                                if(self.validation_third == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                    
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records)
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_sixth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.forth_priority == 1 or self.third_priority==2):
                                self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Status)
                                
                                if(self.validation_fourth == True):
                                    self.passed[records.id]["ENF"]=False 
                                    
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)
                                    #perform the first enforcement validations
                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=False 
                                    
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    #perform the second validations
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records)
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                        
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                    
                                    self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_sixth == True):
                                        self.passed[records.Credit_Account_Status]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.fifth_priority == 1 or self.fifth_priority == 2):
                                self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                self.validation_fifth = self.fifth_ef.validate_field(records)
                                
                                if(self.validation_fifth == True):
                                    self.passed[records.id]["ENF"]=True
                                    
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    #First enforements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records)
                                    #perform the first enforcement validations
                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                    
                                    #Third enforcements  
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records)
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                    
                                    #Fofth enforcements
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records)
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_sixth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.sixth_priority == 1 or self.sixth_priority == 2):
                                self.six_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                self.validation_sixth = self.six_ef.validate_field(records.Credit_Account_Status)
                                if(self.validation_sixth == True):
                                    self.passed[records.id]["ENF"]=True
                                        
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Status)
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    #First enforements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Status)
                                    #perform the first enforcement validations
                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                    
                                    #Third enforcements  
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                    
                                    #Fofth enforcements
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                    
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Status, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records.Credit_Account_Status)
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                            else:
                                self.passed[records.id]["ENF"]=False
                    else:
                        if(records.Credit_Account_Status):
                            if(len(records.Credit_Account_Status) == 1):
                                if(str(records.Credit_Account_Status).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Status)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL28 ", self.passed_by_id.get(keys)
        else:
            pass 
               
    def Last_Status_Change_Date(self, f,rules): 
        self.passed = {}
        for records in self.all_records:
            if(f == "Last_Status_Change_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Last_Status_Change_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
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
                                    #print "KEY ", key, "HERE ", r.get(key)[1]
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field_cba(records.Last_Status_Change_Date, records)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            
                            elif(self.second_priority == 1 or self.second_priority == 2):
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date)

                                if(self.validation_second == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.third_priority == 1 or self.third_priority == 2):
                                self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date)
                                
                                if(self.validation_third == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date)
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.passed[records.id]["ENF"]=False
                    else:
                        if(records.Last_Status_Change_Date):
                            if(len(records.Last_Status_Change_Date) <= 8):
                                if(str(records.Last_Status_Change_Date).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Last_Status_Change_Date)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 29", self.passed_by_id.get(keys)
        else:
            pass 

    def Credit_Account_Risk_Classification(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Risk_Classification"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Account_Risk_Classification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Account_Risk_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Account_Risk_Classification)
                    else:
                        if(records.Credit_Account_Risk_Classification):
                            if(len(records.Credit_Account_Risk_Classification) == 1):
                                if(str(records.Credit_Account_Risk_Classification).strip().rstrip().lstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Risk_Classification)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 30", self.passed_by_id.get(keys)
        else:
            pass 

    def Credit_Account_Arrears_Date(self, f, rules): 
        self.passed = {}  
        for records in self.all_records:
            if(f == "Credit_Account_Arrears_Date"):
                for r in rules:
                    if r == "C":
                        if(records.Credit_Account_Arrears_Date):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
                    elif(isinstance(r, dict)):
                        if(records.Credit_Account_Arrears_Date):
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
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date, records=records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date, records=records)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date, records)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date, records)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date, records=records)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.forth_priority == 1 or self.third_priority==2):
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                    
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=False 
                                        
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date, records)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date, records=records)
                                        #perform the second validations
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fifth = self.fifth_ef.validate_field(records)
                                        if(self.validation_fifth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.fifth_priority == 1 or self.fifth_priority == 2):
                                    self.fifth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                    self.validation_fifth = self.fifth_ef.validate_field(records)
                                    
                                    if(self.validation_fifth == True):
                                        self.passed[records.id]["ENF"]=True
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Arrears_Date, records=records)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        #First enforements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Arrears_Date, records)
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        #Third enforcements  
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        #Fofth enforcements
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Arrears_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Arrears_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                        else:
                            self.passed[records.id]["ENF"]=True

                    else:
                        if(records.Credit_Account_Arrears_Date):
                            if(len(str(records.Credit_Account_Arrears_Date).strip().lstrip().rstrip()) <= 8):
                                if(str(records.Credit_Account_Arrears_Date).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Arrears_Date)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL31 ", self.passed_by_id.get(keys)
        else:
            pass 
                
    def Number_of_Days_in_Arrears(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Number_of_Days_in_Arrears"):
                for r in rules:
                    if r == "C":
                        if(records.Number_of_Days_in_Arrears):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                    elif(isinstance(r, dict)):
                        if(records.Number_of_Days_in_Arrears):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Number_of_Days_in_Arrears, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Number_of_Days_in_Arrears, records=records)
                                #print self.statuss
                        else:
                            self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Number_of_Days_in_Arrears):
                            if(len(records.Number_of_Days_in_Arrears) <= 10):
                                if(str(records.Number_of_Days_in_Arrears).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Number_of_Days_in_Arrears)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 32", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Balance_Overdue(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Balance_Overdue"):
                for r in rules:
                    if r == "C":
                        if(records.Balance_Overdue):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                    elif(isinstance(r, dict)):
                        if(records.Balance_Overdue):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Balance_Overdue, priority=r.get(key))
                                #print key, r
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(field=records.Balance_Overdue, records=records)
                        else:
                            self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Balance_Overdue):
                            if(len(str(records.Balance_Overdue).strip().lstrip().rstrip()) <= 21):
                                if(str(records.Balance_Overdue).strip().rstrip().lstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Balance_Overdue)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL33 ", self.passed_by_id.get(keys)
        else:
            pass 

    def Flag_for_Restructured_Credit(self, f,rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Flag_for_Restructured_Credit"):
                for r in rules:
                    if r == "M":
                        if(records.Flag_for_Restructured_Credit):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Flag_for_Restructured_Credit, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Flag_for_Restructured_Credit)    
                    else:
                        if(records.Flag_for_Restructured_Credit):
                            if(len(records.Flag_for_Restructured_Credit) == 1):
                                if(str(records.Flag_for_Restructured_Credit).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Flag_for_Restructured_Credit)
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL34 ", self.passed_by_id.get(keys)
        else:
            pass 

    def Old_Branch_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Old_Branch_Code"):
                for r in rules:
                    if r == "C":
                        if(records.Old_Branch_Code):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Old_Branch_Code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Old_Branch_Code, records)    

                    else:
                        if(records.Old_Branch_Code):
                            if(len(records.Old_Branch_Code) == 3):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Old_Branch_Code)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL35 ", self.passed_by_id.get(keys)
        else:
            pass 
                             
    def Old_Account_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Old_Account_Number"):
                for r in rules:
                    if r == "C":
                        if(records.Old_Account_Number):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Old_Account_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Old_Account_Number, records=records)    
                    else:
                        if(records.Old_Account_Number):
                            if(len(records.Old_Account_Number) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Old_Account_Number)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 36", self.passed_by_id.get(keys)
        else:
            pass 

    def Old_Client_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Old_Client_Number"):
                for r in rules:
                    if r == "O":
                        if(records.Old_Client_Number):
                            self.passed[records.id]={"Optional":True}
                        else:
                            self.passed[records.id]={"Optional":True} 
                    elif(isinstance(r, dict)):
                        for key in r:
                            #print "KEY ", key
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Old_Client_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Old_Client_Number, records=records)    
                    else:
                        if(records.Old_Client_Number):
                            if(len(records.Old_Client_Number) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Old_Client_Number)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL37 ", self.passed_by_id.get(keys)
        else:
            pass 
                
    def Balance_Overdue_Indicator(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Balance_Overdue_Indicator"):
                for r in rules:
                    if r == "C":
                        if(records.Balance_Overdue_Indicator):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                    #print "FIELD ", r.get(key)[1]
                                    self.validation_second = self.sec_enf.validate_field(records)
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                                if(self.validation_first==True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        #Perform a logging
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Balance_Overdue_Indicator, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records)
                                self.validation_second = self.sec_enf.validate_field(records)
                                
                                if(self.validation_second==True):
                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        #Perform a logging
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(records.Balance_Overdue_Indicator):
                            if(len(str(records.Balance_Overdue_Indicator).strip().lstrip().rstrip()) <= 8):
                                if(str(records.Balance_Overdue_Indicator)):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Balance_Overdue_Indicator)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 38", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Credit_Account_Closure_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Closure_Date"):
                for r in rules:
                    if r == "C":
                        if(records.Credit_Account_Closure_Date):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True}
                        
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
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        #print "VALIDTE ", r.get(key)[1]
                                        self.validation_second = self.sec_enf.validate_field(records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Closure_Date,records=records)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Date_of_First_Payment)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                        
                                        self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                        if(self.validation_fourth == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.forth_priority == 1 or self.third_priority==2):
                                    self.fourth_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                    self.validation_fourth = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                    
                                    if(self.validation_fourth == True):
                                        self.passed[records.id]["ENF"]=False 
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Date)
                                        
                                        #perform the first enforcement validations
                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=False 
                                        
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date)
                                        
                                        #perform the second validations
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Closure_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Closure_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.passed[records.id]["ENF"]=True
                    else:
                        if(records.Credit_Account_Closure_Date):
                            if(len(records.Credit_Account_Closure_Date) <= 8):
                                if(str(records.Credit_Account_Closure_Date).strip().rstrip().lstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Closure_Date)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 39 ", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Credit_Account_Closure_Reason(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_Closure_Reason"):
                for r in rules:
                    if r == "C":
                        if(records.Credit_Account_Closure_Reason):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True} 
                        
                    elif(isinstance(r, dict)):
                        if(records.Credit_Account_Closure_Reason):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Reason)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date, records.Credit_Account_Closure_Reason)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status, records.Credit_Account_Closure_Reason)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_of_First_Payment, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date, records.Credit_Account_Closure_Reason)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status, records.Credit_Account_Closure_Reason)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Account_Status, records.Credit_Account_Closure_Reason)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Account_Closure_Reason)

                                        if(self.validation_first == True):
                                            self.passed[records.id]["ENF"]=True 
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Account_Closure_Reason, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Account_Closure_Date, records.Credit_Account_Closure_Reason)
                                        if(self.validation_second == True):
                                            self.passed[records.id]["ENF"]=True
                                        else:
                                            self.passed[records.id]["ENF"]=False
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                        else:
                            self.passed[records.id]["ENF"]=True

                    else:
                        if(records.Credit_Account_Closure_Reason):
                            if(len(records.Credit_Account_Closure_Reason) == 1):
                                if(str(records.Credit_Account_Closure_Reason).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Account_Closure_Reason)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 40", self.passed_by_id.get(keys)
                
        else:
            pass 
            
    def Specific_Provision_Amount(self,f,rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Specific_Provision_Amount"):
                for r in rules:
                    if r == "C":
                        if(records.Specific_Provision_Amount):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True}
                        
                    elif(isinstance(r, dict)):
                        #self.statuss = checkenforcements.check_enforcements(r, self.pi_c_code, records.Specific_Provision_Amount)    
                        #self.passed["ENF"]=self.statuss.validate_field(records.Specific_Provision_Amount)
                        #if(self.status):
                        self.passed[records.id]["ENF"]=True
                        #self.statuss.validate_field(records.Specific_Provision_Amount)
                        #else:
                        #    self.passed["ENF"]=None
                    else:
                        if(records.Specific_Provision_Amount):
                            if(len(records.Specific_Provision_Amount) <= 21):
                                if(str(records.Specific_Provision_Amount).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Specific_Provision_Amount)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 41 ", self.passed_by_id.get(keys)
        else:
            pass 
                   
    def Client_Consent_Flag(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Client_Consent_Flag"):
                for r in rules:
                    if r == "M":
                        if(records.Client_Consent_Flag):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False} 
                        
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Consent_Flag, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Client_Consent_Flag)    

                    else:
                        if(records.Client_Consent_Flag):
                            if(len(records.Client_Consent_Flag) == 1):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Client_Consent_Flag)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 42", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Client_Advice_Notice_Flag(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Client_Advice_Notice_Flag"):
                for r in rules:
                    if r == "M":
                        if(records.Client_Advice_Notice_Flag):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Advice_Notice_Flag, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Client_Advice_Notice_Flag)    
                    else:
                        if(records.Client_Advice_Notice_Flag):
                            if(len(records.Client_Advice_Notice_Flag) == 1):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Client_Advice_Notice_Flag)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 43", self.passed_by_id.get(keys)
        else:
            pass 
            
    def Term(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Term"):
                for r in rules:
                    if r == "C":
                        if(records.Term):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":True}
                    elif(isinstance(r, dict)):
                        if(records.Term.strip().lstrip().rstrip()):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Term, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records, records=records)
                        else:
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Term)
                    else:
                        if(records.Term.strip().lstrip().rstrip()):
                            if(len(str(records.Term)) <= 50):
                                if(str(records.Term).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Term)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
                            else:
                                self.passed[records.id]["FORMAT"]=True
                        else:
                            self.passed[records.id]["FORMAT"]=True
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL 44 ", self.passed_by_id.get(keys)
            
    def Loan_Purpose(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Loan_Purpose"):
                for r in rules:
                    if r == "M":
                        if(records.Loan_Purpose):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Loan_Purpose, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Loan_Purpose)
                    else:
                        if(len(str(records.Loan_Purpose).strip().lstrip().rstrip()) <= 15):
                            if(str(records.Loan_Purpose).strip().lstrip().rstrip()):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Loan_Purpose)))
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
        if(not len(self.passed)):
            pass 
        elif(len(self.passed)):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
                #print "FINAL ", self.passed_by_id.get(keys)
