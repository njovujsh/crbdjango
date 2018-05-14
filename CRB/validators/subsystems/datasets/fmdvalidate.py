from validators.subsystems import fmdcode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus

class FMDValidate(ibvalidate.IBValidate):
    def __init__(self, code="FRA"):
        super(FMDValidate, self).__init__()
        self._model = models.FINANCIAL_MALPRACTICE_DATA
        self.all_records = self.filter_new_old_records(models.FINANCIAL_MALPRACTICE_DATA)
        self.code = code
        self.pi_c_code = fmdcode.FMDCode(self._model, self.code)

        self.set_code(self.pi_c_code)

    def begin_validation(self):
        try:
            self.all_field = self.pi_c_code.extract()
            self.examine_field(self.all_field)
        except Exception as e:
            # Log
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
                            if(records.PI_Identification_Code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                                if(len(self.parseddata) == 6 or len(self.parseddata) <= 8 ):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code)]["FORMAT"]=False
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
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)

                        else:
                            if(len(records.Branch_Identification_Code.branch_code) >= 3):
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                yield self.passed 

            elif(f == "Borrowers_Client_Number"):
                self.pass_in = {}
                for records in self.all_records:
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
                yield self.passed

            elif(f == "Consumer_Classification"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Consumer_Classification):
                                self.passed[records.Consumer_Classification]={"Conditional":True}
                            else:
                                self.passed[records.Consumer_Classification]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Consumer_Classification, priority=r.get(key))
                                self.passed[records.Consumer_Classification]["ENF"]=self.statuss.validate_field(records.Consumer_Classification)

                        else:
                            if(len(records.Consumer_Classification) == 1):
                                self.passed[records.Consumer_Classification]["FORMAT"]=checkformat.is_numeric(records.Consumer_Classification)
                            else:
                                self.passed[records.Consumer_Classification]["FORMAT"]=False
                yield self.passed 

            elif(f == "Category_Code"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Category_Code):
                                self.passed[records.Category_Code]={"Conditional":True}
                            else:
                                self.passed[str(records.Category_Code)]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.Category_Code):
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Category_Code, priority=r.get(key))
                                    self.passed[records.Category_Code]["ENF"]=self.statuss.validate_field(records.Category_Code)
                                else:
                                    self.passed[str(records.Category_Code)]["ENF"]=False #self.statuss.validate_field(records.Category_Code)

                        else:
                            if(records.Category_Code):
                                if(len(records.Category_Code) == 2 or len(records.Category_Code) == 1):
                                    self.passed[records.Category_Code]["FORMAT"]=checkformat.is_numeric(records.Category_Code)
                                else:
                                    self.passed[records.Category_Code]["FORMAT"]=False
                            else:
                                self.passed[str(records.Category_Code)]["FORMAT"]=False
                yield self.passed 

            elif(f == "Sub_Category_Code"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Sub_Category_Code):
                                self.passed[records.Sub_Category_Code]={"Conditional":True}
                            else:
                                self.passed[str(records.Sub_Category_Code)]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.Sub_Category_Code):
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Sub_Category_Code, priority=r.get(key))
                                    self.passed[records.Sub_Category_Code]["ENF"]=self.statuss.validate_field(records.Sub_Category_Code)
                                else:
                                    self.passed[str(records.Sub_Category_Code)]["ENF"]=False #self.statuss.validate_field(records.Sub_Category_Code)

                        else:
                            if(records.Sub_Category_Code):
                                if(len(records.Sub_Category_Code) >= 2 or len(records.Sub_Category_Code) == 1):
                                    self.passed[records.Sub_Category_Code]["FORMAT"]=checkformat.is_numeric(records.Sub_Category_Code)
                                else:
                                    self.passed[records.Sub_Category_Code]["FORMAT"]=False
                            else:
                                self.passed[str(records.Sub_Category_Code)]["FORMAT"]=False
                yield self.passed 

            elif(f == "Incident_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Incident_Date):
                                self.passed[records.Incident_Date]={"Conditional":True}
                            else:
                                self.passed[records.Incident_Date]={"Conditional":False}

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
                                            self.passed[records.Incident_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.Incident_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Incident_Date]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Incident_Date, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Incident_Date, priority=r.get(key))
                                    
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Incident_Date)
                                    self.validation_second = self.sec_enf.validate_field(records.Incident_Date)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Incident_Date]["ENF"]=True
                                        else:
                                            self.passed[records.Incident_Date]["ENF"]=False
                                    else:
                                        self.passed[records.Incident_Date]["ENF"]=False 
                        else:
                            if(len(records.Incident_Date) >= 8):
                                self.replaced = records.Incident_Date.replace("-", "", len(records.Incident_Date))
                                if(self.replaced):
                                    print "HERE IS THE REPLACE ", records.Incident_Date
                                    self.passed[records.Incident_Date]["FORMAT"]=checkformat.is_numeric(self.replaced)
                                else:
                                    self.passed[records.Incident_Date]["FORMAT"]=True
                            else:
                                self.passed[records.Incident_Date]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Loss_Amount"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Loss_Amount):
                                self.passed[records.Loss_Amount]={"Conditional":True}
                            else:
                                self.passed[records.Loss_Amount]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                #self.statuss = checkenforcements.check_enforcements(key, self._model, records.Sub_Category_Code, priority=r.get(key))
                                self.passed[records.Loss_Amount]["ENF"]=True #self.statuss.validate_field(records.Loss_Amount)

                        else:
                            if(len(records.Loss_Amount) <= 21):
                                self.passed[records.Loss_Amount]["FORMAT"]=checkformat.is_numeric(records.Loss_Amount)
                            else:
                                self.passed[records.Loss_Amount]["FORMAT"]=False

                yield self.passed 
                
            elif(f == "Currency_Type"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Currency_Type):
                                self.passed[records.Currency_Type]={"Conditional":True}
                            else:
                                self.passed[records.Currency_Type]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Currency_Type, priority=r.get(key))
                                self.passed[records.Currency_Type]["ENF"]=self.statuss.validate_field(records.Currency_Type)

                        else:
                            if(len(records.Currency_Type) == 3):
                                self.passed[records.Currency_Type]["FORMAT"]=checkformat.sub_alphanumeric(records.Currency_Type)
                            else:
                                self.passed[records.Currency_Type]["FORMAT"]=False
                yield self.passed 

            elif(f == "Incident_Details"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Incident_Details):
                                self.passed[records.Incident_Details]={"Conditional":True}
                            else:
                                self.passed[records.Incident_Details]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                #pass 
                                #self.statuss = checkenforcements.check_enforcements(key, self._model, records.Incident_Details, priority=r.get(key))
                                self.passed[records.Incident_Details]["ENF"]=True #self.statuss.validate_field(records.Incident_Details, re_enfor=self.sec_enf)

                        else:
                            if(len(records.Incident_Details) <= 1000):
                                self.passed[records.Incident_Details]["FORMAT"]=checkformat.sub_alphanumeric(records.Incident_Details)
                            else:
                                self.passed[records.Incident_Details]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Forensic_Information_Available"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.Forensic_Information_Available):
                                self.passed[records.Forensic_Information_Available]={"Conditional":True}
                            else:
                                self.passed[records.Forensic_Information_Available]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Forensic_Information_Available, priority=r.get(key))
                                self.passed[records.Forensic_Information_Available]["ENF"]=self.statuss.validate_field(records.Forensic_Information_Available)

                        else:
                            if(len(records.Forensic_Information_Available) == 1):
                                self.passed[records.Forensic_Information_Available]["FORMAT"]=checkformat.sub_alphanumeric(records.Forensic_Information_Available)
                            else:
                                self.passed[records.Forensic_Information_Available]["FORMAT"]=False
                yield self.passed 

            else:
                print "Something nusty has happend"
        except Exception as e:
            # Log
            #raise
            pass 

    def check_dict_values(self, s):
        for value in s.values():
            return value.get("P")
            
    def get_keys(self, key_list):
        for k in key_list.keys():
            return k

