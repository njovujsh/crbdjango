from validators.subsystems import capcode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from branchcode import models as branchcodemodels

class CAPValidate(ibvalidate.IBValidate):
    def __init__(self, code="CAP"):
        super(CAPValidate, self).__init__()
        self._model = models.CREDIT_APPLICATION
        self.all_records = self.filter_new_old_records(models.CREDIT_APPLICATION)
        self.code = code
        self.pi_c_code = capcode.CAPCode(self._model, self.code)

        self.set_code(self.pi_c_code)
        self.DATE_FORMAT = "%Y%m%d"
        
    def begin_validation(self):
        try:
            self.all_field = self.pi_c_code.extract()
            self.examine_field(self.all_field)
        except Exception as e:
            pass 

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
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                        else:
                            if(records.PI_Identification_Code.pi_identification_code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                                if(len(self.parseddata) == 6 or len(self.parseddata) <= 8 ):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code.pi_identification_code)]["FORMAT"]=False
                    print "PASSED ", self.passed
                    yield self.passed
                    
            elif(f == "Branch_Identification_Code"):
                self.pass_it = { }
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Branch_Identification_Code):
                                self.passed[records.Branch_Identification_Code.branch_code]={"Mandatory":True}
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                #print "ENFORMENTS ", key, r
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)

                        else:
                            if(records.Branch_Identification_Code.branch_code):
                                if(len(records.Branch_Identification_Code.branch_code) <= 15):
                                    self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Branch_Identification_Code)
                                else:
                                    self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                yield self.passed

            elif(f == "Client_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            #print "SOME IS OPTIONAL"
                            if(records.Client_Number):
                                self.passed[records.Client_Number]={"Optional":True}
                            else:
                                self.passed[records.Client_Number]={"Optional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                #print "My KEY ", key, r
                                #self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Number, priority=r.get(key))
                                self.passed[records.Client_Number]["ENF"]= True #self.statuss.validate_field(records.Client_Number)

                        else:
                            if(records.Client_Number):
                                if(len(str(records.Client_Number)) <= 30):
                                    self.passed[records.Client_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Number)
                                else:
                                    self.passed[records.Client_Number]["FORMAT"]=False
                            else:
                                self.passed[records.Client_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "Credit_Application_Reference"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Application_Reference):
                                self.passed[records.Credit_Application_Reference]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Application_Reference]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Application_Reference, priority=r.get(key))
                                self.passed[records.Credit_Application_Reference]["ENF"]=self.statuss.validate_field(records.Credit_Application_Reference)

                        else:
                            if(records.Credit_Application_Reference):
                                if(len(records.Credit_Application_Reference) <= 30):
                                    self.passed[records.Credit_Application_Reference]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Credit_Application_Reference)
                                else:
                                    self.passed[records.Credit_Application_Reference]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Application_Reference]["FORMAT"]=False
                yield self.passed

            elif(f == "Applicant_Classification"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Applicant_Classification):
                                self.passed[records.Applicant_Classification]={"Mandatory":True}
                            else:
                                self.passed[records.Applicant_Classification]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Applicant_Classification, priority=r.get(key))
                                self.passed[records.Applicant_Classification]["ENF"]=self.statuss.validate_field(records.Applicant_Classification)

                        else:
                            if(records.Applicant_Classification):
                                if(len(records.Applicant_Classification) == 1):
                                    self.passed[records.Applicant_Classification]["FORMAT"]=checkformat.is_numeric(records.Applicant_Classification)
                                else:
                                    self.passed[records.Applicant_Classification]["FORMAT"]=False
                            else:
                                self.passed[records.Applicant_Classification]["FORMAT"]=False
                yield self.passed

            elif(f == "Credit_Application_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Application_Date):
                                self.passed[records.Credit_Application_Date]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Application_Date]={"Mandatory":False}

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
                                            self.passed[records.Credit_Application_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Application_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Application_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Application_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Application_Date]["ENF"]=False 
                                    else:
                                        self.passed[records.Credit_Application_Date]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Credit_Application_Date)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Application_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Application_Date]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Credit_Application_Date)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Credit_Application_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Application_Date]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Credit_Application_Date]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Credit_Application_Date)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date)

                                        if(self.validation_first == True):
                                            self.passed[records.Credit_Application_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Credit_Application_Date]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Credit_Application_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Credit_Application_Date)
                                        if(self.validation_second == True):
                                            self.passed[records.Credit_Application_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Credit_Application_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Credit_Application_Date]["ENF"]=False
                                else:
                                    self.passed[records.Credit_Application_Date]["ENF"]=False 

                        else:
                            if(records.Credit_Application_Date):
                                if(len(str(records.Credit_Application_Date)) <= 8):
                                    self.passed[records.Credit_Application_Date]["FORMAT"]=checkformat.is_numeric(int(float(records.Credit_Application_Date)))
                                else:
                                    self.passed[records.Credit_Application_Date]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Application_Date]["FORMAT"]=False
                yield self.passed

            elif(f == "Amount"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Amount):
                                self.passed[records.Amount]={"Mandatory":True}
                            else:
                                self.passed[records.Amount]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Amount, priority=r.get(key))
                                self.passed[records.Amount]["ENF"]=self.statuss.validate_field(records.Amount) 
                        else:
                            if(records.Amount !=  None):
                                if(len(records.Amount) <= 21):
                                    self.passed[records.Amount]["FORMAT"]=checkformat.is_numeric(records.Amount)
                                else:
                                    self.passed[records.Amount]["FORMAT"]=False
                            else:
                                self.passed[records.Amount]["FORMAT"]=False
                yield self.passed
                
            elif(f == "Currency"):
                self.pass_lid = {}
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
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Currency, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Currency)
                                    else:
                                        self.passed[records.Currency]["ENF"]=False
                                        
                                    if(self.validation_first==True):
                                        if(self.validation_second == True):
                                            self.passed[records.Currency]["ENF"]=True
                                        else:
                                            #Perform a logging
                                            self.passed[records.Currency]["ENF"]=False
                                    else:
                                        self.passed[records.Currency]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Currency, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Currency, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Currency)
                                    self.validation_second = self.sec_enf.validate_field(records.Currency)
                                    
                                    if(self.validation_second==True):
                                        if(self.validation_first == True):
                                            self.passed[records.Currency]["ENF"]=True
                                        else:
                                            #Perform a logging
                                            self.passed[records.Currency]["ENF"]=False
                                    else:
                                        self.passed[records.Currency]["ENF"]=False 

                        else:
                            if(records.Currency):
                                if(len(records.Currency) == 3):
                                    self.passed[records.Currency]["FORMAT"]=checkformat.sub_alphanumeric(records.Currency)
                                else:
                                    self.passed[records.Currency]["FORMAT"]=False
                            else:
                                self.passed[records.Currency]["FORMAT"]=False
                yield self.passed
                
            elif(f == "Credit_Account_or_Loan_Product_Type"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Account_or_Loan_Product_Type):
                                self.passed[records.Credit_Account_or_Loan_Product_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Account_or_Loan_Product_Type]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Account_or_Loan_Product_Type, priority=r.get(key))
                                self.passed[records.Credit_Account_or_Loan_Product_Type]["ENF"]=self.statuss.validate_field(records.Credit_Account_or_Loan_Product_Type)

                        else:
                            if(records.Credit_Account_or_Loan_Product_Type):
                                if(len(records.Credit_Account_or_Loan_Product_Type) <= 5):
                                    self.passed[records.Credit_Account_or_Loan_Product_Type]["FORMAT"]=checkformat.is_numeric(records.Credit_Account_or_Loan_Product_Type)
                                else:
                                    self.passed[records.Credit_Account_or_Loan_Product_Type]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Account_or_Loan_Product_Type]["FORMAT"]=False
                yield self.passed

            elif(f == "Credit_Application_Status"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Application_Status):
                                self.passed[records.Credit_Application_Status]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Application_Status]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r: 
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Application_Status, priority=r.get(key))
                                self.passed[records.Credit_Application_Status]["ENF"]=self.statuss.validate_field(records.Credit_Application_Status)

                        else:
                            if(records.Credit_Application_Status):
                                if(len(str(records.Credit_Application_Status)) == 1):
                                    self.stripped = str(records.Credit_Application_Status).strip().lstrip().rstrip()
                                    if(self.stripped):
                                        self.passed[records.Credit_Application_Status]["FORMAT"]=checkformat.is_numeric(int(float(self.stripped)))
                                    else:
                                        self.passed[records.Credit_Application_Status]["FORMAT"]=False
                                else:
                                    self.passed[records.Credit_Application_Status]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Application_Status]["FORMAT"]=False
                yield self.passed
                
            elif(f == "Last_Status_Change_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Last_Status_Change_Date):
                                self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]={"Mandatory":True}
                            else:
                                self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]={"Mandatory":False}

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
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=True 
                                        else:
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=True
                                        else:
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False 
                                    else:
                                        self.passed[records.Currency]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                        #self.validation_first = self.vstatus.validate_field(records.Credit_Application_Date)
                                        self.validation_first = self.vstatus.validate_field(rrecords.Last_Status_Change_Date.strftime(self.DATE_FORMAT))

                                        if(self.validation_first == True):
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=True 
                                        else:
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=True
                                        else:
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))

                                        if(self.validation_first == True):
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=True 
                                        else:
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Last_Status_Change_Date.strftime(self.DATE_FORMAT), priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                        if(self.validation_second == True):
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=True
                                        else:
                                            self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                    else:
                                        self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False
                                else:
                                    self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["ENF"]=False

                        else:
                            if(records.Last_Status_Change_Date != None):
                                if(len(str(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))) <= 16):
                                    if(str(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)).rstrip().strip().rstrip()):
                                        self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["FORMAT"]=True #checkformat.is_numeric(records.Last_Status_Change_Date.strftime(self.DATE_FORMAT))
                                    else:
                                        self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["FORMAT"]=False
                                else:
                                    self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["FORMAT"]=False
                            else:
                                self.passed[records.Last_Status_Change_Date.strftime(self.DATE_FORMAT)]["FORMAT"]=False
                print self.passed 
                yield self.passed
                
            elif(f == "Credit_Application_Duration"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Credit_Application_Duration):
                                self.passed[records.Credit_Application_Duration]={"Mandatory":True}
                            else:
                                self.passed[records.Credit_Application_Duration]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Credit_Application_Duration, priority=r.get(key))
                                self.passed[records.Credit_Application_Duration]["ENF"]=self.statuss.validate_field(records.Credit_Application_Duration)

                        else:
                            if(records.Credit_Application_Duration != None):
                                if(len(str(records.Credit_Application_Duration)) <= 50):
                                    self.passed[records.Credit_Application_Duration]["FORMAT"]=checkformat.is_numeric(records.Credit_Application_Duration)
                                else:
                                    self.passed[records.Credit_Application_Duration]["FORMAT"]=False
                            else:
                                self.passed[records.Credit_Application_Duration]["FORMAT"]=False
                yield self.passed

            elif(f == "Rejection_Reason"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Rejection_Reason):
                                self.passed[records.Rejection_Reason]={"Conditional":True}
                            else:
                                self.passed[records.Rejection_Reason]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Rejection_Reason, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Rejection_Reason)
                                    #print "V STATUS ", self.vstatus
                                    if(self.validation_first == True):
                                        #print "Phase 1 validation first is entirely true"
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Rejection_Reason, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Rejection_Reason)
                                        
                                        if(self.validation_second == True):
                                            #print "Phase 1 validation two is True"
                                            self.passed[records.Rejection_Reason]["ENF"]=True 
                                        else:
                                            #print "Phase 1 validation two is falses"
                                            self.passed[records.Rejection_Reason]["ENF"]=False
                                    else:
                                        #print "Phase 1 validation first is fale"
                                        self.passed[records.Rejection_Reason]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Rejection_Reason, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Rejection_Reason, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Rejection_Reason)
                                    self.validation_second = self.sec_enf.validate_field(records.Rejection_Reason)
                                    
                                    if(self.validation_first == True):
                                        #print "First validation is true"
                                        if(self.validation_second == True):
                                            #print "Second validation has passed "
                                            self.passed[records.Rejection_Reason]["ENF"]=True
                                        else:
                                            #print "Looks like second validation has failed in last"
                                            self.passed[records.Rejection_Reason]["ENF"]=False
                                    else:
                                        #print "First validation is not true.."
                                        self.passed[records.Rejection_Reason]["ENF"]=False

                        else:
                            if(records.Rejection_Reason):
                                #print "Validation in progress...", records.Rejection_Reason, checkformat.is_numeric(records.Rejection_Reason)
                                if(len(str(records.Rejection_Reason)) <= 20):
                                    self.passed[records.Rejection_Reason]["FORMAT"]=checkformat.is_numeric(records.Rejection_Reason)
                                else:
                                    self.passed[records.Rejection_Reason]["FORMAT"]=False
                            else:
                                self.passed[records.Rejection_Reason]["FORMAT"]=False
                #print self.passed 
                yield self.passed
                
            elif(f == "Client_Consent_flag"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Client_Consent_flag):
                                self.passed[records.Client_Consent_flag]={"Mandatory":True}
                            else:
                                self.passed[records.Client_Consent_flag]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Client_Consent_flag, priority=r.get(key))
                                self.passed[records.Client_Consent_flag]["ENF"]=self.statuss.validate_field(records.Client_Consent_flag)

                        else:
                            if(records.Client_Consent_flag):
                                if(len(str(records.Client_Consent_flag)) <= 10):
                                    self.passed[records.Client_Consent_flag]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Consent_flag)
                                else:
                                    self.passed[records.Client_Consent_flag]["FORMAT"]=False
                            else:
                                self.passed[records.Client_Consent_flag]["FORMAT"]=False
                yield self.passed

            else:
                print "Yes", f
                #print "Something nusty has happend"
        except Exception as e:
            # Log
            pass  

    def check_dict_values(self, s):
        for value in s.values():
            return value.get("P")
            
    def get_keys(self, key_list):
        for k in key_list.keys():
            return k


