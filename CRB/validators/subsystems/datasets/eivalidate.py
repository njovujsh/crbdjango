from validators.subsystems import eicode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus

class EIValidate(ibvalidate.IBValidate):
    def __init__(self, code="EI"):
        super(EIValidate, self).__init__()
        self._model = models.EMPLOYMENT_INFORMATION
        self.all_records = models.EMPLOYMENT_INFORMATION.objects.all()
        self.code = code 
        self.pi_c_code = eicode.EICode(self._model, self.code)
        
        self.all_records = models.CREDIT_APPLICATION.objects.all()
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }

        try:
            if(f == "EI_Employment_Type"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Employment_Type):
                                self.passed[records.ei.EI_Employment_Type]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Employment_Type]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.ei.EI_Employment_Type, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.ei.EI_Employment_Type, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.ei.EI_Employment_Type, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.ei.EI_Employment_Type)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.ei.EI_Employment_Type]["ENF"]=True 
                                        else:
                                            self.passed[records.ei.EI_Employment_Type]["ENF"]=False
                                    else:
                                        self.passed[records.ei.EI_Employment_Type]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.ei.EI_Employment_Type, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.ei.EI_Employment_Type, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.ei.EI_Employment_Type)
                                    self.validation_second = self.sec_enf.validate_field(records.ei.EI_Employment_Type)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.ei.EI_Employment_Type]["ENF"]=True
                                        else:
                                            self.passed[records.ei.EI_Employment_Type]["ENF"]=False
                                    else:
                                        self.passed[records.ei.EI_Employment_Type]["ENF"]=False
                        else:
                            if(records.ei.EI_Employment_Type):
                                if(len(records.ei.EI_Employment_Type) == 1):
                                    self.passed[records.ei.EI_Employment_Type]["FORMAT"]=checkformat.has_numerics_re(records.ei.EI_Employment_Type)
                                else:
                                    self.passed[records.ei.EI_Employment_Type]["FORMAT"]=False
                            else:
                                self.passed[str(records.ei.EI_Employment_Type)]["FORMAT"]=False
                #print self.passed
                yield self.passed  
               
            elif(f == "EI_Primary_Occupation"):
                self.pass_it = { }
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Primary_Occupation):
                                self.passed[records.ei.EI_Primary_Occupation]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Primary_Occupation]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                #print "KEY ", key 
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.ei.EI_Primary_Occupation, priority=r.get(key))
                                self.passed[records.ei.EI_Primary_Occupation]["ENF"]=self.statuss.validate_field(records, records)

                        else:
                            if(len(records.ei.EI_Primary_Occupation) <= 100):
                                self.passed[records.ei.EI_Primary_Occupation]["FORMAT"]=checkformat.sub_alphanumeric(records.ei.EI_Primary_Occupation)
                            else:
                                self.passed[records.ei.EI_Primary_Occupation]["FORMAT"]=False
                yield self.passed 

            elif(f == "EI_Employer_Name"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Employer_Name):
                                self.passed[records.ei.EI_Employer_Name]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Employer_Name]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.ei.EI_Employer_Name, priority=r.get(key))
                                self.passed[records.ei.EI_Employer_Name]["ENF"]=self.statuss.validate_field(records, records)

                        else:
                            if(len(records.ei.EI_Employer_Name)  <= 100):
                                self.passed[records.ei.EI_Employer_Name]["FORMAT"]=True #checkformat.has_numerics_re(records.ei.EI_Employer_Name)
                            else:
                                self.passed[records.ei.EI_Employer_Name]["FORMAT"]=False
                yield self.passed 

            elif(f == "EI_Employee_Number"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Employee_Number):
                                self.passed[records.ei.EI_Employee_Number]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Employee_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #
                            self.passed[records.ei.EI_Employee_Number]["ENF"]=True
                        else:
                            if(len(str(records.ei.EI_Employee_Number)) <= 20):
                                self.passed[records.ei.EI_Employee_Number]["FORMAT"]=checkformat.has_numerics_re(records.ei.EI_Employee_Number)
                            else:
                                self.passed[records.ei.EI_Employee_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "EI_Employment_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Employment_Date):
                                self.passed[records.ei.EI_Employment_Date]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Employment_Date]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.ei.EI_Employment_Date, priority=r.get(key))
                                self.passed[records.ei.EI_Employment_Date]["ENF"]=self.statuss.validate_field(records.ei.EI_Employment_Date, records)
                        else:
                            if(records.ei.EI_Employment_Date):
                                self.ei_date = records.ei.EI_Employment_Date.replace("-", "", 20)
                                if(len(str(self.ei_date)) >= 6):
                                    self.passed[records.ei.EI_Employment_Date]["FORMAT"]=checkformat.is_numeric(self.ei_date)
                                else:
                                    self.passed[records.ei.EI_Employment_Date]["FORMAT"]=False
                            else:
                                self.passed[records.ei.EI_Employment_Date]["FORMAT"]=False
                #print "DATE EI ", self.passed
                yield self.passed 

            elif(f == "EI_Income_Band"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Income_Band):
                                self.passed[records.ei.EI_Income_Band]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Income_Band]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.ei.EI_Income_Band, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records,  records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.ei.EI_Income_Band, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.ei.EI_Income_Band)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.ei.EI_Income_Band]["ENF"]=True 
                                        else:
                                            self.passed[records.ei.EI_Income_Band]["ENF"]=False
                                    else:
                                        self.passed[records.ei.EI_Income_Band]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.ei.EI_Income_Band, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.ei.EI_Income_Band, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.ei.EI_Income_Band)
                                    self.validation_second = self.sec_enf.validate_field(records.ei.EI_Income_Band)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.ei.EI_Income_Band]["ENF"]=True
                                        else:
                                            self.passed[records.ei.EI_Income_Band]["ENF"]=False
                                    else:
                                        self.passed[records.ei.EI_Income_Band]["ENF"]=False
                        else:
                            if(records.ei.EI_Income_Band):
                                if(len(str(records.ei.EI_Income_Band)) <= 2):
                                    self.passed[records.ei.EI_Income_Band]["FORMAT"]=checkformat.is_numeric(records.ei.EI_Income_Band)
                                else:
                                    self.passed[records.ei.EI_Income_Band]["FORMAT"]=False
                            else:
                                self.passed[str(records.ei.EI_Income_Band)]["FORMAT"]=False
                yield self.passed 

            elif(f == "EI_Salary_Frequency"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.ei.EI_Salary_Frequency):
                                self.passed[records.ei.EI_Salary_Frequency]={"Conditional":True}
                            else:
                                self.passed[records.ei.EI_Salary_Frequency]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.ei.EI_Salary_Frequency, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.ei.EI_Salary_Frequency, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.ei.EI_Salary_Frequency)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.ei.EI_Salary_Frequency]["ENF"]=True 
                                        else:
                                            self.passed[records.ei.EI_Salary_Frequency]["ENF"]=False
                                    else:
                                        self.passed[records.ei.EI_Salary_Frequency]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.ei.EI_Salary_Frequency, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.ei.EI_Salary_Frequency, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.ei.EI_Salary_Frequency)
                                    self.validation_second = self.sec_enf.validate_field(records.ei.EI_Salary_Frequency)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.ei.EI_Salary_Frequency]["ENF"]=True
                                        else:
                                            self.passed[records.ei.EI_Salary_Frequency]["ENF"]=False
                                    else:
                                        self.passed[records.ei.EI_Salary_Frequency]["ENF"]=False
                        else:
                            if(records.ei.EI_Salary_Frequency):
                                if(len(str(records.ei.EI_Salary_Frequency)) <= 2):
                                    self.passed[records.ei.EI_Salary_Frequency]["FORMAT"]=checkformat.is_numeric(records.ei.EI_Salary_Frequency)
                                else:
                                    self.passed[records.ei.EI_Salary_Frequency]["FORMAT"]=False
                            else:
                                self.passed[str(records.ei.EI_Salary_Frequency)]["FORMAT"]=False
                yield self.passed
        except Exception as e:
            # Log
            pass  
