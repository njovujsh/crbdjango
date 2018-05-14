from validators.subsystems import ibcode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import validationstatus

class IBValidate(pivalidate.PIValidate):
    def __init__(self, code="IB"):
        super(IBValidate, self).__init__()
        self._model = models.INSTITUTION_BRANCH
        self.all_records = self.filter_new_old_records(models.INSTITUTION_BRANCH)
        self.code = code
        self.pi_c_code = ibcode.IBCode(self._model, self.code)

        #Set the code of model/datasets to be used
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
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "",10)
                                if(len(self.parseddata) == 6 or len(self.parseddata) <= 8):
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
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=checkformat.sub_alphanumeric(records.Branch_Identification_Code.branch_code)
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                yield self.passed

            elif(f == "Branch_Name"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Branch_Name):
                                self.passed[records.Branch_Name]={"Mandatory":True}
                            else:
                                self.passed[records.Branch_Name]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Name, priority=r.get(key))
                                self.passed[records.Branch_Name]["ENF"]=self.statuss.validate_field(records.Branch_Name)

                        else:
                            if(len(records.Branch_Name) <= 100):
                                self.passed[records.Branch_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.Branch_Name)
                            else:
                                self.passed[records.Branch_Name]["FORMAT"]=False

                yield self.passed

            elif(f == "Branch_Type"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Branch_Type):
                                self.passed[records.Branch_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Branch_Type]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Type, priority=r.get(key))
                                self.passed[records.Branch_Type]["ENF"]=self.statuss.validate_field(records.Branch_Type)

                        else:
                            if(len(records.Branch_Type) == 1):
                                self.passed[records.Branch_Type]["FORMAT"]=checkformat.sub_alphanumeric(records.Branch_Type)
                            else:
                                self.passed[records.Branch_Type]["FORMAT"]=False

                yield self.passed

            elif(f == "Date_Opened"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Date_Opened):
                                self.passed[records.Date_Opened]={"Mandatory":True}
                            else:
                                self.passed[records.Date_Opened]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_Opened, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.Date_Opened)

                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_Opened, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.Date_Opened)

                                        if(self.validation_second == True):
                                            self.passed[records.Date_Opened]["ENF"]=True
                                        else:
                                            self.passed[records.Date_Opened]["ENF"]=False
                                    else:
                                        self.passed[records.Date_Opened]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Date_Opened, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Date_Opened, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.Date_Opened)
                                    self.validation_second = self.sec_enf.validate_field(records.Date_Opened, headers=self.headers)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Date_Opened]["ENF"]=True
                                        else:
                                            self.passed[records.Date_Opened]["ENF"]=False
                                    else:
                                        self.passed[records.Date_Opened]["ENF"]=False

                        else:
                            if(len(records.Date_Opened.replace("-", "", 12)) == 8):
                                self.passed[records.Date_Opened]["FORMAT"]=checkformat.is_numeric(records.Date_Opened.replace("-", "",12))
                            else:
                                self.passed[records.Date_Opened]["FORMAT"]=False

                yield self.passed

            else:
                print "Something nusty has happend"
        except Exception as e:
            # Log
            pass  

    def check_dict_values(self, s):
        for value in s.values():
            return value.get("P")

    def get_keys(self, key_list):
        for k in key_list.keys():
            return k
