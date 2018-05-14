from validators.subsystems import capcode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 

class ReportCAPValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="CAP"):
        super(ReportCAPValidate, self).__init__()
        self._model = models.CREDIT_APPLICATION
        self.all_records = models.CREDIT_APPLICATION.objects.all()
        self.code = code
        self.pi_c_code = capcode.CAPCode(self._model, self.code)
        self.all_count = models.CREDIT_APPLICATION.objects.all().count()
        self.set_code(self.pi_c_code)
        self.DATE_FORMAT = "%Y%m%d"
        self.record_fields=14

    def begin_validation(self):
        try:
            self.all_field = self.pi_c_code.extract()
            self.examine_field(self.all_field)
        except:
            pass

    def check_data_in_field(self, f, rules):
        self.final_result={}
        try:
            self.PI_Identification_Code(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Client_Number(f, rules)
            self.Credit_Application_Reference(f, rules)
            self.Applicant_Classification(f, rules)
            self.Credit_Application_Date(f, rules)
            self.Amount(f, rules)
            self.Currency(f, rules)
            self.Credit_Account_or_Loan_Product_Type(f, rules)
            self.Credit_Application_Status(f, rules)
            self.Last_Status_Change_Date(f, rules)
            self.Credit_Application_Duration(f, rules)
            self.Rejection_Reason(f, rules)
            self.Client_Consent_flag(f, rules)
        except Exception as e:
            pass 
        else:
            #print self.final_result
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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                    else:
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata) <= 16):
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
                #print "Counted Trues PI_Id_Code", keys, self.passed.get(keys) #.values().count(True)
                self.passed_list.append(self.passed.get(keys).values().count(True))
                self.passed_by_id[keys]=self.passed_list
                print self.passed_list
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
                            #print "ENFORMENTS ", key, r
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)

                    else:
                        if(records.Branch_Identification_Code.branch_code):
                            if(len(str(records.Branch_Identification_Code.branch_code)) <= 15):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Branch_Identification_Code)
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
    
    def Client_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Client_Number"):
                for r in rules:
                    if r == "O":
                        #print "SOME IS OPTIONAL"
                        if(records.Client_Number):
                            self.passed[records.id]={"Optional":True}
                        else:
                            self.passed[records.id]={"Optional":True}

                    elif(isinstance(r, dict)):
                        for key in r:
                            #print "My KEY ", key, r
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]= True #self.statuss.validate_field(records.Client_Number)

                    else:
                        if(records.Client_Number):
                            if(len(str(records.Client_Number)) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Number)
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
                
    def Credit_Application_Reference(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Application_Reference"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Application_Reference):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Application_Reference, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Application_Reference)

                    else:
                        if(records.Credit_Application_Reference):
                            if(len(str(records.Credit_Application_Reference)) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Credit_Application_Reference)
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
                
    def Applicant_Classification(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Applicant_Classification"):
                for r in rules:
                    if r == "M":
                        if(records.Applicant_Classification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Applicant_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Applicant_Classification)

                    else:
                        if(records.Applicant_Classification):
                            if(len(str(records.Applicant_Classification)) == 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Applicant_Classification)))
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
            
    def Credit_Application_Date(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Application_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Application_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            self.third_priority = self.check_dict_values(r.get(key)[2])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    #print "DATES ", r.get(key)[1]
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Application_Date, records)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Application_Date)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            
                            elif(self.second_priority == 1 or self.second_priority == 2):
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                self.validation_second = self.sec_enf.validate_field(records.Credit_Application_Date)

                                if(self.validation_second == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Application_Date)
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.third_priority == 1 or self.third_priority == 2):
                                self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                self.validation_third = self.third_ef.validate_field(records.Credit_Application_Date)
                                
                                if(self.validation_third == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date)

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Application_Date)
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.passed[records.id]["ENF"]=False 

                    else:
                        if(records.Credit_Application_Date):
                            if(len(records.Credit_Application_Date) <= 8):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Application_Date)))
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
                
    def Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Amount"):
                for r in rules:
                    if r == "M":
                        if(records.Amount):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Amount, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Amount) 
                    else:
                        if(records.Amount !=  None):
                            if(len(str(records.Amount)) <= 21):
                                if(str(records.Amount).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.Amount)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Currency, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Currency)
                                else:
                                    self.passed[records.Currency]["ENF"]=False
                                    
                                if(self.validation_first==True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        #Perform a logging
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Currency, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Currency, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Currency)
                                self.validation_second = self.sec_enf.validate_field(records.Currency)
                                
                                if(self.validation_second==True):
                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        #Perform a logging
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                    else:
                        if(records.Currency):
                            if(len(str(records.Currency)) == 3):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Currency)
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
                
    def Credit_Account_or_Loan_Product_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Account_or_Loan_Product_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Account_or_Loan_Product_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Account_or_Loan_Product_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Account_or_Loan_Product_Type)

                    else:
                        if(records.Credit_Account_or_Loan_Product_Type):
                            if(len(str(records.Credit_Account_or_Loan_Product_Type)) <= 5):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Credit_Account_or_Loan_Product_Type)
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
    
    def Credit_Application_Status(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Application_Status"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Application_Status):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            #print "ENFORMENTS Status ", key, r
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Application_Status, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Application_Status)

                    else:
                        if(records.Credit_Application_Status):
                            if(len(str(records.Credit_Application_Status)) <= 1):
                                self.stripped = str(records.Credit_Application_Status).strip().lstrip().rstrip()
                                if(self.stripped):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.stripped)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
                
    def Last_Status_Change_Date(self,f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Last_Status_Change_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            #print key, r
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            self.third_priority = self.check_dict_values(r.get(key)[2])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            
                            elif(self.second_priority == 1 or self.second_priority == 2):
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))

                                if(self.validation_second == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date.strftime(self.DATE_FORMAT))

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                    
                                    if(self.validation_third == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                else:
                                    self.passed[records.id]["ENF"]=False
                                    
                            elif(self.third_priority == 1 or self.third_priority == 2):
                                self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                
                                if(self.validation_third == True):
                                    #Perform the second validation given the first enforcements
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))

                                    if(self.validation_first == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                        
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.passed[records.id]["ENF"]=False

                    else:
                        if(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT) != None):
                            if(len(str(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))) <= 12):
                                if(str(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
                
    def Credit_Application_Duration(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Credit_Application_Duration"):
                for r in rules:
                    if r == "M":
                        if(records.Credit_Application_Duration):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Application_Duration, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Credit_Application_Duration)

                    else:
                        if(records.Credit_Application_Duration != None):
                            if(len(str(records.Credit_Application_Duration)) <= 50):
                                if(str(records.Credit_Application_Duration).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(records.Credit_Application_Duration))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
    
    def Rejection_Reason(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Rejection_Reason"):
                for r in rules:
                    if r == "C":
                        if(records.Rejection_Reason):
                            self.passed[records.id]={"Conditional":True}
                        else:
                            self.passed[records.id]={"Conditional":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Rejection_Reason, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Rejection_Reason)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Rejection_Reason, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Rejection_Reason)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Rejection_Reason, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Rejection_Reason, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Rejection_Reason)
                                self.validation_second = self.sec_enf.validate_field(records.Rejection_Reason)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False

                    else:
                        if(records.Rejection_Reason):
                            if(len(str(records.Rejection_Reason)) <= 20):
                                if(str(records.Rejection_Reason).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Rejection_Reason)
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
                
    def Client_Consent_flag(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Client_Consent_flag"):
                #print "CONSENT ", records.Client_Consent_flag
                for r in rules:
                    if r == "M":
                        if(records.Client_Consent_flag):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Consent_flag, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Client_Consent_flag)

                    else:
                        if(records.Client_Consent_flag):
                            if(len(str(records.Client_Consent_flag)) <= 10):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Consent_flag)
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

    def check_dict_values(self, s):
        for value in s.values():
            return value.get("P")
            
    def get_keys(self, key_list):
        for k in key_list.keys():
            return k
