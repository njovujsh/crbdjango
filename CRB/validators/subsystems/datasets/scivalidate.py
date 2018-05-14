from validators.subsystems import scicode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus


class SCIValidate(ibvalidate.IBValidate):
    def __init__(self, code="SCI"):
        super(SCIValidate, self).__init__(code=code)

        self._model = models.SCI
        self.all_records = models.SCI.objects.all()
        self.code = code
        self.pi_c_code = scicode.SCICode(self._model, self.code)

    def check_data_in_field(self, f, rules):
        self.passed = { }
        try:
            if(f == "SCI_Unit_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Unit_Number):
                                self.passed[records.SCI_Unit_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Unit_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Unit_Number, priority=r.get(key))
                                self.passed[records.SCI_Unit_Number]["ENF"]=self.statuss.validate_field(records.SCI_Unit_Number)
                        else:
                            if(records.SCI_Unit_Number):
                                if(len(records.SCI_Unit_Number) <=50):
                                    self.passed[records.SCI_Unit_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Unit_Number)
                                else:
                                    self.passed[records.SCI_Unit_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Unit_Number)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Unit_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Unit_Name):
                                self.passed[records.SCI_Unit_Name]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Unit_Name]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Unit_Name, priority=r.get(key))
                                self.passed[records.SCI_Unit_Name]["ENF"]=self.statuss.validate_field(records.SCI_Unit_Name)
                        else:
                            if(records.SCI_Unit_Name):
                                if(len(records.SCI_Unit_Name) <=50):
                                    self.passed[records.SCI_Unit_Name]["FORMAT"]=True ##checkformat.sub_alphanumeric(records.SCI_Unit_Name)
                                else:
                                    self.passed[records.SCI_Unit_Name]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Unit_Name)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Floor_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Floor_Number):
                                self.passed[records.SCI_Floor_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Floor_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Floor_Number, priority=r.get(key))
                                self.passed[records.SCI_Floor_Number]["ENF"]=self.statuss.validate_field(records.SCI_Floor_Number)
                        else:
                            if(records.SCI_Floor_Number):
                                if(len(records.SCI_Floor_Number) <=80):
                                    self.passed[records.SCI_Floor_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Floor_Number)
                                else:
                                    self.passed[records.SCI_Floor_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Floor_Number)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Plot_or_Street_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.SCI_Plot_or_Street_Number):
                                self.passed[records.SCI_Plot_or_Street_Number]={"Optional":True}
                            else:
                                self.passed[records.SCI_Plot_or_Street_Number]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.SCI_Plot_or_Street_Number]["ENF"]= True #self.statuss.validate_field(records.SCI_Plot_or_Street_Number)
                        else:
                            if(records.SCI_Plot_or_Street_Number):
                                if(len(records.SCI_Plot_or_Street_Number) <=60):
                                    self.passed[records.SCI_Plot_or_Street_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Plot_or_Street_Number)
                                else:
                                    self.passed[records.SCI_Plot_or_Street_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Plot_or_Street_Number)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_LC_or_Street_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.SCI_LC_or_Street_Name):
                                self.passed[records.SCI_LC_or_Street_Name]={"Optional":True}
                            else:
                                self.passed[records.SCI_LC_or_Street_Name]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.SCI_LC_or_Street_Name]["ENF"]= True #self.statuss.validate_field(records.SCI_Plot_or_Street_Number)
                        else:
                            if(records.SCI_LC_or_Street_Name):
                                if(len(records.SCI_LC_or_Street_Name) <=50):
                                    self.passed[records.SCI_LC_or_Street_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.SCI_LC_or_Street_Name)
                                else:
                                    self.passed[records.SCI_LC_or_Street_Name]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_LC_or_Street_Name)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Parish"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Parish):
                                self.passed[records.SCI_Parish]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Parish]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.SCI_Parish):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])

                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_Parish, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.SCI_Parish)

                                        if(self.validation_first == True):
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_Parish, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.SCI_Parish)

                                            if(self.validation_second == True):
                                                self.passed[records.SCI_Parish]["ENF"]=True
                                            else:
                                                self.passed[records.SCI_Parish]["ENF"]=False
                                        else:
                                            self.passed[records.SCI_Parish]["ENF"]=False
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_Parish, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_Parish, priority=r.get(key))

                                        self.validation_first = self.vstatus.validate_field(records.SCI_Parish)
                                        self.validation_second = self.sec_enf.validate_field(records.SCI_Parish)

                                        if(self.validation_first == True):
                                            if(self.validation_second == True):
                                                self.passed[records.SCI_Parish]["ENF"]=True
                                            else:
                                                self.passed[records.SCI_Parish]["ENF"]=False
                                        else:
                                            self.passed[records.SCI_Parish]["ENF"]=False
                            else:
                                self.passed[records.SCI_Parish]["ENF"]=True
                        else:
                            if(records.SCI_Parish):
                                if(len(records.SCI_Parish) <=50):
                                    self.passed[records.SCI_Parish]["FORMAT"]=True #=checkformat.sub_alphanumeric(records.SCI_Parish)
                                else:
                                    self.passed[records.SCI_Parish]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Parish)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Suburb"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.SCI_Suburb):
                                self.passed[records.SCI_Suburb]={"Optional":True}
                            else:
                                self.passed[records.SCI_Suburb]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.SCI_Suburb]["ENF"]= True #self.statuss.validate_field(records.SCI_Plot_or_Street_Number)
                        else:
                            if(records.SCI_Suburb):
                                if(len(records.SCI_Suburb) <=50):
                                    self.passed[records.SCI_Suburb]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Suburb)
                                else:
                                    self.passed[records.SCI_Suburb]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Suburb)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Village"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.SCI_Village):
                                self.passed[records.SCI_Village]={"Optional":True}
                            else:
                                self.passed[records.SCI_Village]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.SCI_Village]["ENF"]= True #self.statuss.validate_field(records.SCI_Plot_or_Street_Number)
                        else:
                            if(records.SCI_Village):
                                if(len(records.SCI_Village) <=50):
                                    self.passed[records.SCI_Village]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Village)
                                else:
                                    self.passed[records.SCI_Village]["FORMAT"]=True
                            else:
                                if(self.passed.get(str(records.SCI_Village))):
                                    self.passed[str(records.SCI_Village)]["FORMAT"]=True
                                else:
                                    self.passed[str("")]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_County_or_Town"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_County_or_Town):
                                self.passed[records.SCI_County_or_Town]={"Conditional":True}
                            else:
                                self.passed[records.SCI_County_or_Town]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.SCI_County_or_Town):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])

                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_County_or_Town, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.SCI_County_or_Town, records.SCI_County_or_Town)

                                        if(self.validation_first == True):
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_County_or_Town, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.SCI_County_or_Town)

                                            if(self.validation_second == True):
                                                self.passed[records.SCI_County_or_Town]["ENF"]=True
                                            else:
                                                self.passed[records.SCI_County_or_Town]["ENF"]=False
                                        else:
                                            self.passed[records.SCI_County_or_Town]["ENF"]=False
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_County_or_Town, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_County_or_Town, priority=r.get(key))

                                        self.validation_first = self.vstatus.validate_field(records.SCI_County_or_Town, records.PCI_Country_Code)
                                        self.validation_second = self.sec_enf.validate_field(records.SCI_County_or_Town)

                                        if(self.validation_first == True):
                                            if(self.validation_second == True):
                                                self.passed[records.SCI_County_or_Town]["ENF"]=True
                                            else:
                                                self.passed[records.SCI_County_or_Town]["ENF"]=False
                                        else:
                                            self.passed[records.SCI_County_or_Town]["ENF"]=False
                            else:
                                self.passed[records.SCI_County_or_Town]["ENF"]=True
                        else:
                            if(records.SCI_County_or_Town):
                                if(len(records.SCI_County_or_Town) <=50):
                                    self.passed[records.SCI_County_or_Town]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_County_or_Town)
                                else:
                                    self.passed[records.SCI_County_or_Town]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_County_or_Town)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_District"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_District):
                                self.passed[records.SCI_District]={"Conditional":True}
                            else:
                                self.passed[str(records.SCI_District)]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_District, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.SCI_District, records=records.SCI_Country_Code)
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_District, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.SCI_District)

                                        if(self.validation_second == True):
                                            self.passed[records.SCI_District]["ENF"]=True
                                        else:
                                            self.passed[records.SCI_District]["ENF"]=False
                                    else:
                                        self.passed[records.SCI_District]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_District, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_District, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.SCI_District, records=records.SCI_Country_Code)
                                    self.validation_second = self.sec_enf.validate_field(records.SCI_District)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.SCI_District]["ENF"]=True
                                        else:
                                            self.passed[records.SCI_District]["ENF"]=False
                                    else:
                                        self.passed[records.SCI_District]["ENF"]=False
                        else:
                            if(records.SCI_District):
                                if(len(records.SCI_District) <=50):
                                    self.passed[records.SCI_District]["FORMAT"]=checkformat.sub_alphanumeric(records.SCI_District)
                                else:
                                    self.passed[records.SCI_District]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_District)]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Region"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Region):
                                self.passed[records.SCI_Region]={"Conditional":True}
                            else:
                                self.passed[str(records.SCI_Region)]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_Region, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.SCI_Region)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_Region, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.SCI_Region)

                                        if(self.validation_second == True):
                                            self.passed[records.SCI_Region]["ENF"]=True
                                        else:
                                            self.passed[records.SCI_Region]["ENF"]=False
                                    else:
                                        self.passed[records.SCI_Region]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_Region, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_Region, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.SCI_Region)
                                    self.validation_second = self.sec_enf.validate_field(records.SCI_Region)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.SCI_Region]["ENF"]=True
                                        else:
                                            self.passed[records.SCI_Region]["ENF"]=False
                                    else:
                                        self.passed[records.SCI_Region]["ENF"]=False
                        else:
                            if(records.SCI_Region):
                                if(len(records.SCI_Region) <=50):
                                    self.passed[records.SCI_Region]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Region)
                                else:
                                    self.passed[records.SCI_Region]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Region)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_PO_Box_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_PO_Box_Number):
                                self.passed[records.SCI_PO_Box_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_PO_Box_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.SCI_PO_Box_Number):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_PO_Box_Number, priority=r.get(key))
                                    self.passed[records.SCI_PO_Box_Number]["ENF"]=self.statuss.validate_field(records.SCI_PO_Box_Number)
                            else:
                                self.passed[records.SCI_PO_Box_Number]["ENF"]=self.statuss.validate_field(records.SCI_PO_Box_Number)
                        else:
                            if(records.SCI_PO_Box_Number):
                                if(len(records.SCI_PO_Box_Number) <=60):
                                    self.passed[records.SCI_PO_Box_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_PO_Box_Number)
                                else:
                                    self.passed[records.SCI_PO_Box_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_PO_Box_Number)]["FORMAT"]=True
                yield self.passed

            elif(f == "SCI_Post_Office_Town"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Post_Office_Town):
                                self.passed[records.SCI_Post_Office_Town]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Post_Office_Town]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Post_Office_Town, priority=r.get(key))
                                self.passed[records.SCI_Post_Office_Town]["ENF"]=self.statuss.validate_field(records.SCI_Post_Office_Town)
                        else:
                            if(records.SCI_Post_Office_Town):
                                if(len(records.SCI_Post_Office_Town) <=50):
                                    self.passed[records.SCI_Post_Office_Town]["FORMAT"]=True #checkformat.sub_alphanumeric(records.SCI_Post_Office_Town)
                                else:
                                    self.passed[records.SCI_Post_Office_Town]["FORMAT"]=False
                            else:
                                self.passed[records.SCI_Post_Office_Town]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Country_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.SCI_Country_Code):
                                self.passed[records.SCI_Country_Code]={"Mandatory":True}
                            else:
                                self.passed[records.SCI_Country_Code]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_Country_Code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.SCI_Country_Code)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_Country_Code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.SCI_Country_Code)

                                        if(self.validation_second == True):
                                            self.passed[records.SCI_Country_Code]["ENF"]=True
                                        else:
                                            self.passed[records.SCI_Country_Code]["ENF"]=False
                                    else:
                                        self.passed[records.SCI_Country_Code]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.SCI_Country_Code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.SCI_Country_Code, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.SCI_Country_Code)
                                    self.validation_second = self.sec_enf.validate_field(records.SCI_Country_Code)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.SCI_Country_Code]["ENF"]=True
                                        else:
                                            self.passed[records.SCI_Country_Code]["ENF"]=False
                                    else:
                                        self.passed[records.SCI_Country_Code]["ENF"]=False
                        else:
                            if(records.SCI_Country_Code):
                                if(len(records.SCI_Country_Code) <=5):
                                    self.passed[records.SCI_Country_Code]["FORMAT"]=checkformat.sub_alphanumeric(records.SCI_Country_Code)
                                else:
                                    self.passed[records.SCI_Country_Code]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Country_Code)]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Period_At_Address"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.SCI_Period_At_Address):
                                self.passed[records.SCI_Period_At_Address]={"Mandatory":True}
                            else:
                                self.passed[records.SCI_Period_At_Address]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Period_At_Address, priority=r.get(key))
                                self.passed[records.SCI_Period_At_Address]["ENF"]=self.statuss.validate_field(records.SCI_Period_At_Address)
                        else:
                            if(records.SCI_Period_At_Address):
                                if(len(records.SCI_Period_At_Address) <=300):
                                    self.passed[records.SCI_Period_At_Address]["FORMAT"]=checkformat.is_numeric(records.SCI_Period_At_Address)
                                else:
                                    self.passed[records.SCI_Period_At_Address]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.SCI_Period_At_Address))):
                                    self.passed[str(records.SCI_Period_At_Address)]["FORMAT"]=False
                                else:
                                    self.passed[str("")]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Flag_for_ownership"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.SCI_Flag_for_ownership):
                                self.passed[records.SCI_Flag_for_ownership]={"Mandatory":True}
                            else:
                                self.passed[records.SCI_Flag_for_ownership]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Flag_for_ownership, priority=r.get(key))
                                self.passed[records.SCI_Flag_for_ownership]["ENF"]=self.statuss.validate_field(records.SCI_Flag_for_ownership)
                        else:
                            if(records.SCI_Flag_for_ownership):
                                if(len(records.SCI_Flag_for_ownership) <=5):
                                    self.passed[records.SCI_Flag_for_ownership]["FORMAT"]=checkformat.sub_alphanumeric(records.SCI_Flag_for_ownership)
                                else:
                                    self.passed[records.SCI_Flag_for_ownership]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Flag_for_ownership)]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Primary_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Primary_Number_Telephone_Number):
                                self.passed[records.SCI_Primary_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Primary_Number_Telephone_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Primary_Number_Telephone_Number, priority=r.get(key))
                                self.passed[records.SCI_Primary_Number_Telephone_Number]["ENF"]=self.statuss.validate_field(records.SCI_Primary_Number_Telephone_Number)
                        else:
                            if(records.SCI_Primary_Number_Telephone_Number):
                                if(len(records.SCI_Primary_Number_Telephone_Number) <=100):
                                    self.passed[records.SCI_Primary_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.SCI_Primary_Number_Telephone_Number)
                                else:
                                    self.passed[records.SCI_Primary_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.SCI_Primary_Number_Telephone_Number))):
                                    self.passed[str(records.SCI_Primary_Number_Telephone_Number)]["FORMAT"]=False
                                else:
                                    self.passed[str("")]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Other_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Other_Number_Telephone_Number):
                                self.passed[records.SCI_Other_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Other_Number_Telephone_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Other_Number_Telephone_Number, priority=r.get(key))
                            self.passed[records.SCI_Other_Number_Telephone_Number]["ENF"]= True #self.statuss.validate_field(records.SCI_Other_Number_Telephone_Number)
                        else:
                            if(records.SCI_Other_Number_Telephone_Number):
                                if(len(records.SCI_Other_Number_Telephone_Number) <=50):
                                    self.passed[records.SCI_Other_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.SCI_Other_Number_Telephone_Number)
                                else:
                                    self.passed[records.SCI_Other_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.SCI_Other_Number_Telephone_Number))):
                                    self.passed[str(records.SCI_Other_Number_Telephone_Number)]["FORMAT"]=False
                                else:
                                    self.passed[str("")]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Mobile_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Mobile_Number_Telephone_Number):
                                self.passed[records.SCI_Mobile_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Mobile_Number_Telephone_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Mobile_Number_Country_Dialling_Code, priority=r.get(key))
                            self.passed[records.SCI_Mobile_Number_Telephone_Number]["ENF"]= True #self.statuss.validate_field(records.SCI_Mobile_Number_Country_Dialling_Code)
                        else:
                            if(records.SCI_Mobile_Number_Telephone_Number):
                                if(len(records.SCI_Mobile_Number_Telephone_Number) <=50):
                                    self.passed[records.SCI_Mobile_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.SCI_Mobile_Number_Telephone_Number)
                                else:
                                    self.passed[records.SCI_Mobile_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Mobile_Number_Telephone_Number)]["FORMAT"]=False
                yield self.passed


            elif(f == "SCI_Facsimile_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Facsimile_Number):
                                self.passed[records.SCI_Facsimile_Number]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Facsimile_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.SCI_Facsimile_Number]["ENF"]= True #self.statuss.validate_field(records.SCI_Facsimile_Number)
                        else:
                            if(records.SCI_Facsimile_Number):
                                if(len(records.SCI_Facsimile_Number) <=10):
                                    self.passed[records.SCI_Facsimile_Number]["FORMAT"]=checkformat.is_numeric(records.SCI_Facsimile_Number)
                                else:
                                    self.passed[records.SCI_Facsimile_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Facsimile_Number)]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Email_Address"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Email_Address):
                                self.passed[records.SCI_Email_Address]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Email_Address]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.SCI_Email_Address]["ENF"]= True #self.statuss.validate_field(records.SCI_Facsimile_Number)
                        else:
                            if(records.SCI_Email_Address):
                                if(len(records.SCI_Email_Address) <=50):
                                    self.passed[records.SCI_Email_Address]["FORMAT"]=checkformat.sub_alphanumeric(records.SCI_Email_Address)
                                else:
                                    self.passed[records.SCI_Email_Address]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Email_Address)]["FORMAT"]=False
                yield self.passed

            elif(f == "SCI_Web_site"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.SCI_Web_site):
                                self.passed[records.SCI_Web_site]={"Conditional":True}
                            else:
                                self.passed[records.SCI_Web_site]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.SCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.SCI_Web_site]["ENF"]= True #self.statuss.validate_field(records.SCI_Facsimile_Number)
                        else:
                            if(records.SCI_Web_site):
                                if(len(records.SCI_Web_site) <=50):
                                    self.passed[records.SCI_Web_site]["FORMAT"]=checkformat.sub_alphanumeric(records.SCI_Web_site)
                                else:
                                    self.passed[records.SCI_Web_site]["FORMAT"]=False
                            else:
                                self.passed[str(records.SCI_Web_site)]["FORMAT"]=False
                yield self.passed
        except Exception as e:
            # Log
            pass  
