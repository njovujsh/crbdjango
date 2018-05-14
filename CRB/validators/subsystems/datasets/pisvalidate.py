from validators.subsystems import piscode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import validationstatus

class PISValidate(pivalidate.PIValidate):
    def __init__(self, code="PIS"):
        super(PISValidate, self).__init__()
        self._model = models.PARTICIPATINGINSTITUTIONSTAKEHOLDER
        self.all_records = self.filter_new_old_records(models.PARTICIPATINGINSTITUTIONSTAKEHOLDER)
        self.code = code 
        self.pi_c_code = piscode.PISCode(self._model, self.code)
     
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
                                if(len(self.parseddata) == 6 or len(self.parseddata) <=8 ):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code)]["FORMAT"]=False
                yield self.passed  
                
            elif(f == "Stakeholder_Type"):
                self.pass_it = { }
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
                            if(len(records.Stakeholder_Type) == 1):
                                self.passed[records.Stakeholder_Type]["FORMAT"]=checkformat.is_numeric(records.Stakeholder_Type)
                            else:
                                self.passed[records.Stakeholder_Type]["FORMAT"]=False
                yield self.passed 

            elif(f == "Stakeholder_Category"):
                self.pass_in = {}
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
                            if(len(records.Stakeholder_Category) == 1 or  len(records.Stakeholder_Category)  == 2):
                                self.passed[records.Stakeholder_Category]["FORMAT"]=checkformat.is_numeric(records.Stakeholder_Category)
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
                                self.is_valid = self.statuss.validate_field(records.Shareholder_Percentage)
                                if(self.is_valid == True):
                                    if(records.Shareholder_Percentage):
                                        self.passed[records.Shareholder_Percentage]["ENF"]=True
                                    else:
                                        self.passed[records.Shareholder_Percentage]["ENF"]=False 
                                else:
                                    self.passed[records.Shareholder_Percentage]["ENF"]=True
                        else:
                            if(len(str(records.Shareholder_Percentage))):
                                self.passed[records.Shareholder_Percentage]["FORMAT"]=checkformat.is_float(records.Shareholder_Percentage)
                            else:
                                self.passed[records.Shareholder_Percentage]["FORMAT"]=False
                yield self.passed 
        except Exception as e:
            # Log
            pass  
