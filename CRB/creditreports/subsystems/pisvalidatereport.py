from validators.subsystems import piscode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 

class ReportPISValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="PIS"):
        super(ReportPISValidate, self).__init__()
        self._model = models.PARTICIPATINGINSTITUTIONSTAKEHOLDER
        self.all_records = models.PARTICIPATINGINSTITUTIONSTAKEHOLDER.objects.all()
        self.all_count = models.PARTICIPATINGINSTITUTIONSTAKEHOLDER.objects.all().count()
        self.code = code 
        self.pi_c_code = piscode.PISCode(self._model, self.code)
        self.record_fields = 4
        self.dict_list = []
        self.passed_by_id = {}
        self.real_passed = {}
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }
        self.all_records_passed = {}
        self.final_result={}
        
        try:
           self.validate_PI(f, rules) 
           self.Stakeholder_Type(f, rules) 
           self.Stakeholder_Category(f, rules) 
           self.Stakeholder_Category(f, rules) 
        except Exception as e:
            # Log
            pass 
        else:
            yield self.final_result
    
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
    def Stakeholder_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Stakeholder_Type"):
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Stakeholder_Type):
                                self.passed[records.id]={"Mandatory":True}
                            else:
                                self.passed[records.id]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Stakeholder_Type, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Stakeholder_Type)
                        else:
                            if(len(records.Stakeholder_Type) == 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Stakeholder_Type)
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
    def Stakeholder_Category(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Stakeholder_Category"):
                for r in rules:
                    if r == "M":
                        if(records.Stakeholder_Category):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                            
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Stakeholder_Category, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Stakeholder_Category)

                    else:
                        if(len(records.Stakeholder_Category) == 1 or  len(records.Stakeholder_Category) == 2):
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Stakeholder_Category)
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
    def Stakeholder_Category(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Stakeholder_Category"):
                for r in rules:
                    if r == "M":
                        if(records.Shareholder_Percentage):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Shareholder_Percentage, priority=r.get(key))
                            self.is_valid = self.statuss.validate_field(records.Shareholder_Percentage)
                            if(self.is_valid == True):
                                if(records.Shareholder_Percentage):
                                    self.passed[records.id]["ENF"]=True
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.passed[records.id]["ENF"]=True
                    else:
                        if(len(str(records.Shareholder_Percentage))):
                            self.passed[records.id]["FORMAT"]=checkformat.is_float(records.Shareholder_Percentage)
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
