from validators.subsystems import pcicode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus


class PCIValidate(ibvalidate.IBValidate):
    def __init__(self, code="PCI"):
        super(PCIValidate, self).__init__(code=code)
        
        self._model = models.PCI
        self.all_records = models.PCI.objects.all()
        self.code = code 
        self.pi_c_code = pcicode.PCICode(self._model, self.code)
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }
        
        try:
            if(f == "PCI_Building_Unit_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Building_Unit_Number):
                                self.passed[records.PCI_Building_Unit_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Building_Unit_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_Building_Unit_Number):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Building_Unit_Number, priority=r.get(key))
                                    self.passed[records.PCI_Building_Unit_Number]["ENF"]=self.statuss.validate_field(records.PCI_Building_Unit_Number)
                            else:
                                self.passed[records.PCI_Building_Unit_Number]["ENF"]=True #self.statuss.validate_field(records.PCI_Building_Unit_Number)
                        else:
                            if(records.PCI_Building_Unit_Number):
                                if(len(str(records.PCI_Building_Unit_Number)) <=40):
                                    self.passed[records.PCI_Building_Unit_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_Building_Unit_Number)
                                else:
                                    self.passed[records.PCI_Building_Unit_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Building_Unit_Number)]["FORMAT"]=True
                #print "passed ", self.passed 
                yield self.passed  
                
            elif(f == "PCI_Building_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Building_Name):
                                self.passed[records.PCI_Building_Name]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Building_Name]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_Building_Name):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Building_Name, priority=r.get(key))
                                    self.passed[records.PCI_Building_Name]["ENF"]=self.statuss.validate_field(records.PCI_Building_Name)
                            else:
                                self.passed[records.PCI_Building_Name]["ENF"]=True #self.statuss.validate_field(records.PCI_Building_Name)
                        else:
                            if(records.PCI_Building_Name):
                                if(len(str(records.PCI_Building_Name)) <=50):
                                    self.passed[records.PCI_Building_Name]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_Building_Name)
                                else:
                                    self.passed[records.PCI_Building_Name]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Building_Name)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Floor_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Floor_Number):
                                self.passed[records.PCI_Floor_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Floor_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_Floor_Number):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Floor_Number, priority=r.get(key))
                                    self.passed[records.PCI_Floor_Number]["ENF"]=self.statuss.validate_field(records.PCI_Floor_Number)
                            else:
                                self.passed[records.PCI_Floor_Number]["ENF"]=True #self.statuss.validate_field(records.PCI_Floor_Number)
                        else:
                            if(records.PCI_Floor_Number):
                                if(len(records.PCI_Floor_Number) <=10):
                                    self.passed[records.PCI_Floor_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_Floor_Number)
                                else:
                                    self.passed[records.PCI_Floor_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Floor_Number)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Plot_or_Street_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.PCI_Plot_or_Street_Number):
                                self.passed[records.PCI_Plot_or_Street_Number]={"Optional":True}
                            else:
                                self.passed[records.PCI_Plot_or_Street_Number]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.PCI_Plot_or_Street_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(records.PCI_Plot_or_Street_Number):
                                if(len(records.PCI_Plot_or_Street_Number) <=50):
                                    self.passed[records.PCI_Plot_or_Street_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_Plot_or_Street_Number)
                                else:
                                    self.passed[records.PCI_Plot_or_Street_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Plot_or_Street_Number)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_LC_or_Street_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.PCI_LC_or_Street_Name):
                                self.passed[records.PCI_LC_or_Street_Name]={"Optional":True}
                            else:
                                self.passed[records.PCI_LC_or_Street_Name]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.PCI_LC_or_Street_Name]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(records.PCI_LC_or_Street_Name):
                                if(len(records.PCI_LC_or_Street_Name) <=50):
                                    self.passed[records.PCI_LC_or_Street_Name]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_LC_or_Street_Name)
                                else:
                                    self.passed[records.PCI_LC_or_Street_Name]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_LC_or_Street_Name)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Parish"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Parish):
                                self.passed[records.PCI_Parish]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Parish]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_Parish):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_Parish, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.PCI_Parish)
                                        
                                        if(self.validation_first == True):
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_Parish, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.PCI_Parish)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_Parish]["ENF"]=True 
                                            else:
                                                self.passed[records.PCI_Parish]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_Parish]["ENF"]=False
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_Parish, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_Parish, priority=r.get(key))
                                        
                                        self.validation_first = self.vstatus.validate_field(records.PCI_Parish)
                                        self.validation_second = self.sec_enf.validate_field(records.PCI_Parish)
                                        
                                        if(self.validation_first == True):
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_Parish]["ENF"]=True
                                            else:
                                                self.passed[records.PCI_Parish]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_Parish]["ENF"]=False
                            else:
                                self.passed[records.PCI_Parish]["ENF"]=True
                        else:
                            if(records.PCI_Parish):
                                if(len(records.PCI_Parish) <=50):
                                    self.passed[records.PCI_Parish]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_Parish)
                                else:
                                    self.passed[records.PCI_Parish]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Parish)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Suburb"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.PCI_Suburb):
                                self.passed[records.PCI_Suburb]={"Optional":True}
                            else:
                                self.passed[records.PCI_Suburb]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.PCI_Suburb]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(records.PCI_Suburb):
                                if(len(records.PCI_Suburb) <=50):
                                    self.passed[records.PCI_Suburb]["FORMAT"]=checkformat.sub_alphanumeric(records.PCI_Suburb)
                                else:
                                    self.passed[records.PCI_Suburb]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Suburb)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Village"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.PCI_Village):
                                self.passed[records.PCI_Village]={"Optional":True}
                            else:
                                self.passed[records.PCI_Village]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.PCI_Village]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(records.PCI_Village):
                                if(len(records.PCI_Village) <=50):
                                    self.passed[records.PCI_Village]["FORMAT"]=checkformat.sub_alphanumeric(records.PCI_Village)
                                else:
                                    self.passed[records.PCI_Village]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.PCI_Village))):
                                    self.passed[str(records.PCI_Village)]["FORMAT"]=True
                                else:
                                    #self.passed[str("")]["FORMAT"]=False
                                    self.passed[records.PCI_Village]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_County_or_Town"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_County_or_Town):
                                self.passed[records.PCI_County_or_Town]={"Conditional":True}
                            else:
                                self.passed[records.PCI_County_or_Town]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_County_or_Town):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_County_or_Town, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.PCI_County_or_Town, records=records.PCI_Country_Code)
                                        
                                        if(self.validation_first == True):
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_County_or_Town, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.PCI_County_or_Town)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_County_or_Town]["ENF"]=True 
                                            else:
                                                self.passed[records.PCI_County_or_Town]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_County_or_Town]["ENF"]=False
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_County_or_Town, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_County_or_Town, priority=r.get(key))
                                        
                                        self.validation_first = self.vstatus.validate_field(records.PCI_County_or_Town, records.PCI_Country_Code)
                                        self.validation_second = self.sec_enf.validate_field(records.PCI_County_or_Town)
                                        
                                        if(self.validation_first == True):
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_County_or_Town]["ENF"]=True
                                            else:
                                                self.passed[records.PCI_County_or_Town]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_County_or_Town]["ENF"]=False
                            else:
                                self.passed[records.PCI_County_or_Town]["ENF"]=True
                        else:
                            if(records.PCI_County_or_Town):
                                if(len(records.PCI_County_or_Town) <=50):
                                    self.passed[records.PCI_County_or_Town]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_County_or_Town)
                                else:
                                    self.passed[records.PCI_County_or_Town]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_County_or_Town)]["FORMAT"]=True
                #print self.passed 
                yield self.passed  
                
            elif(f == "PCI_District"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_District):
                                self.passed[records.PCI_District]={"Conditional":True}
                            else:
                                self.passed[records.PCI_District]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_District):
                                #print "HERE WER ARE ", records.PCI_District
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_District, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.PCI_District, records=records.PCI_Country_Code)
                                        if(self.validation_first == True):
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_District, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.PCI_District)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_District]["ENF"]=True 
                                            else:
                                                self.passed[records.PCI_District]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_District]["ENF"]=False
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_District, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_District, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.PCI_District, records=records.PCI_Country_Code)
                                        self.validation_second = self.sec_enf.validate_field(records.PCI_District)
                                        
                                        if(self.validation_first == True):
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_District]["ENF"]=True
                                            else:
                                                self.passed[records.PCI_District]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_District]["ENF"]=False
                            else:
                                self.passed[records.PCI_District]["ENF"]=True
                        else:
                            if(records.PCI_District):
                                if(len(records.PCI_District) <=50):
                                    self.passed[records.PCI_District]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_District)
                                else:
                                    self.passed[records.PCI_District]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_District)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Region"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Region):
                                self.passed[records.PCI_Region]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Region]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_Region):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2):
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_Region, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.PCI_Region)
                                        
                                        if(self.validation_first == True):
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_Region, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.PCI_Region)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_Region]["ENF"]=True 
                                            else:
                                                self.passed[records.PCI_Region]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_Region]["ENF"]=False
                                    else:
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_Region, priority=r.get(key))
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_Region, priority=r.get(key))
                                        
                                        self.validation_first = self.vstatus.validate_field(records.PCI_Region)
                                        self.validation_second = self.sec_enf.validate_field(records.PCI_Region)
                                        
                                        if(self.validation_first == True):
                                            if(self.validation_second == True):
                                                self.passed[records.PCI_Region]["ENF"]=True
                                            else:
                                                self.passed[records.PCI_Region]["ENF"]=False
                                        else:
                                            self.passed[records.PCI_Region]["ENF"]=False
                            else:
                                self.passed[records.PCI_Region]["ENF"]=True
                        else:
                            if(records.PCI_Region):
                                if(len(records.PCI_Region) <=5):
                                    self.passed[records.PCI_Region]["FORMAT"]=checkformat.is_numeric(records.PCI_Region)
                                else:
                                    self.passed[records.PCI_Region]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Region)]["FORMAT"]=False
                yield self.passed  
                
            elif(f == "PCI_PO_Box_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_PO_Box_Number):
                                self.passed[records.PCI_PO_Box_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_PO_Box_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_PO_Box_Number):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_PO_Box_Number, priority=r.get(key))
                                    self.passed[records.PCI_PO_Box_Number]["ENF"]=self.statuss.validate_field(records.PCI_PO_Box_Number)
                            else:
                                self.passed[records.PCI_PO_Box_Number]["ENF"]=True #self.statuss.validate_field(records.PCI_PO_Box_Number)
                        else:
                            if(records.PCI_PO_Box_Number):
                                if(len(records.PCI_PO_Box_Number) <=60):
                                    self.passed[records.PCI_PO_Box_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_PO_Box_Number)
                                else:
                                    self.passed[records.PCI_PO_Box_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_PO_Box_Number)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Post_Office_Town"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Post_Office_Town):
                                self.passed[records.PCI_Post_Office_Town]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Post_Office_Town]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            if(records.PCI_Post_Office_Town):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Post_Office_Town, priority=r.get(key))
                                    self.passed[records.PCI_Post_Office_Town]["ENF"]=self.statuss.validate_field(records.PCI_Post_Office_Town)
                            else:
                                self.passed[records.PCI_Post_Office_Town]["ENF"]=True #self.statuss.validate_field(records.PCI_Post_Office_Town)
                        else:
                            if(records.PCI_Post_Office_Town):
                                if(len(records.PCI_Post_Office_Town) <=50):
                                    self.passed[records.PCI_Post_Office_Town]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PCI_Post_Office_Town)
                                else:
                                    self.passed[records.PCI_Post_Office_Town]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Post_Office_Town)]["FORMAT"]=True
                yield self.passed  
                
            elif(f == "PCI_Country_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.PCI_Country_Code):
                                self.passed[records.PCI_Country_Code]={"Mandatory":True}
                            else:
                                self.passed[records.PCI_Country_Code]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_Country_Code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.PCI_Country_Code)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_Country_Code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.PCI_Country_Code)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.PCI_Country_Code]["ENF"]=True 
                                        else:
                                            self.passed[records.PCI_Country_Code]["ENF"]=False
                                    else:
                                        self.passed[records.PCI_Country_Code]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PCI_Country_Code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PCI_Country_Code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.PCI_Country_Code)
                                    self.validation_second = self.sec_enf.validate_field(records.PCI_Country_Code)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.PCI_Country_Code]["ENF"]=True
                                        else:
                                            self.passed[records.PCI_Country_Code]["ENF"]=False
                                    else:
                                        self.passed[records.PCI_Country_Code]["ENF"]=False
                        else:
                            if(records.PCI_Country_Code):
                                if(len(records.PCI_Country_Code) <=5):
                                    self.passed[records.PCI_Country_Code]["FORMAT"]=checkformat.sub_alphanumeric(records.PCI_Country_Code)
                                else:
                                    self.passed[records.PCI_Country_Code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Country_Code)]["FORMAT"]=False
                yield self.passed  
                
            elif(f == "PCI_Period_At_Address"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.PCI_Period_At_Address):
                                self.passed[records.PCI_Period_At_Address]={"Mandatory":True}
                            else:
                                self.passed[records.PCI_Period_At_Address]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Period_At_Address, priority=r.get(key))
                                self.passed[records.PCI_Period_At_Address]["ENF"]=self.statuss.validate_field(records.PCI_Period_At_Address)
                        else:
                            if(records.PCI_Period_At_Address):
                                if(len(records.PCI_Period_At_Address) <= 300):
                                    self.passed[records.PCI_Period_At_Address]["FORMAT"]=checkformat.is_numeric(records.PCI_Period_At_Address)
                                else:
                                    self.passed[records.PCI_Period_At_Address]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.PCI_Period_At_Address))):
                                    self.passed[str(records.PCI_Period_At_Address)]["FORMAT"]=True
                                else:
                                    self.passed[str("")]["FORMAT"]=False
                yield self.passed
                
            elif(f == "PCI_Flag_of_Ownership"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.PCI_Flag_of_Ownership):
                                self.passed[records.PCI_Flag_of_Ownership]={"Mandatory":True}
                            else:
                                self.passed[records.PCI_Flag_of_Ownership]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Flag_of_Ownership, priority=r.get(key))
                                self.passed[records.PCI_Flag_of_Ownership]["ENF"]=self.statuss.validate_field(records.PCI_Flag_of_Ownership)
                        else:
                            if(records.PCI_Flag_of_Ownership):
                                if(len(records.PCI_Flag_of_Ownership) <=5):
                                    self.passed[records.PCI_Flag_of_Ownership]["FORMAT"]=checkformat.sub_alphanumeric(records.PCI_Flag_of_Ownership)
                                else:
                                    self.passed[records.PCI_Flag_of_Ownership]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Flag_of_Ownership)]["FORMAT"]=False
                yield self.passed
                
            elif(f == "PCI_Primary_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Primary_Number_Telephone_Number):
                                self.passed[records.PCI_Primary_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Primary_Number_Telephone_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Primary_Number_Telephone_Number, priority=r.get(key))
                                self.passed[records.PCI_Primary_Number_Telephone_Number]["ENF"]=self.statuss.validate_field(records.PCI_Primary_Number_Telephone_Number)
                        else:
                            if(records.PCI_Primary_Number_Telephone_Number):
                                if(len(records.PCI_Primary_Number_Telephone_Number) <=10):
                                    self.passed[records.PCI_Primary_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.PCI_Primary_Number_Telephone_Number)
                                else:
                                    self.passed[records.PCI_Primary_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.PCI_Primary_Number_Telephone_Number))):
                                    self.passed[str(records.PCI_Primary_Number_Telephone_Number)]["FORMAT"]=True
                                else:
                                    self.passed[str("")]["FORMAT"]=True
                yield self.passed
                
            elif(f == "PCI_Other_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Other_Number_Telephone_Number):
                                self.passed[records.PCI_Other_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Other_Number_Telephone_Number]={"Conditional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Other_Number_Telephone_Number, priority=r.get(key))
                            self.passed[records.PCI_Other_Number_Telephone_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Other_Number_Telephone_Number)
                        else:
                            if(records.PCI_Other_Number_Telephone_Number):
                                if(len(records.PCI_Other_Number_Telephone_Number) <=50):
                                    self.passed[records.PCI_Other_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.PCI_Other_Number_Telephone_Number)
                                else:
                                    self.passed[records.PCI_Other_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                if(self.passed.get(str(records.PCI_Other_Number_Telephone_Number))):
                                    self.passed[str(records.PCI_Other_Number_Telephone_Number)]["FORMAT"]=True
                                else:
                                    self.passed[str("")]["FORMAT"]=True
                yield self.passed
                
            elif(f == "PCI_Mobile_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Mobile_Number_Telephone_Number):
                                self.passed[records.PCI_Mobile_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Mobile_Number_Telephone_Number]={"Conditional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Mobile_Number_Country_Dialling_Code, priority=r.get(key))
                            self.passed[records.PCI_Mobile_Number_Telephone_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Mobile_Number_Country_Dialling_Code)
                        else:
                            if(records.PCI_Mobile_Number_Telephone_Number):
                                if(len(records.PCI_Mobile_Number_Telephone_Number) <=50):
                                    self.passed[records.PCI_Mobile_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.PCI_Mobile_Number_Telephone_Number)
                                else:
                                    self.passed[records.PCI_Mobile_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Mobile_Number_Telephone_Number)]["FORMAT"]=True
                yield self.passed
                
                
            elif(f == "PCI_Facsimile_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Facsimile_Number):
                                self.passed[records.PCI_Facsimile_Number]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Facsimile_Number]={"Conditional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.PCI_Facsimile_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Facsimile_Number)
                        else:
                            if(records.PCI_Facsimile_Number):
                                if(len(records.PCI_Facsimile_Number) <=10):
                                    self.passed[records.PCI_Facsimile_Number]["FORMAT"]=checkformat.is_numeric(records.PCI_Facsimile_Number)
                                else:
                                    self.passed[records.PCI_Facsimile_Number]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Facsimile_Number)]["FORMAT"]=True
                yield self.passed
                
            elif(f == "PCI_Email_Address"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Email_Address):
                                self.passed[records.PCI_Email_Address]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Email_Address]={"Conditional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.PCI_Email_Address]["ENF"]= True #self.statuss.validate_field(records.PCI_Facsimile_Number)
                        else:
                            if(records.PCI_Email_Address):
                                if(len(records.PCI_Email_Address) <=50):
                                    self.passed[records.PCI_Email_Address]["FORMAT"]=checkformat.sub_alphanumeric(records.PCI_Email_Address)
                                else:
                                    self.passed[records.PCI_Email_Address]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Email_Address)]["FORMAT"]=True
                yield self.passed
                
            elif(f == "PCI_Web_site"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.PCI_Web_site):
                                self.passed[records.PCI_Web_site]={"Conditional":True}
                            else:
                                self.passed[records.PCI_Web_site]={"Conditional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.PCI_Web_site]["ENF"]= True #self.statuss.validate_field(records.PCI_Facsimile_Number)
                        else:
                            if(records.PCI_Web_site):
                                if(len(records.PCI_Web_site) <=50):
                                    self.passed[records.PCI_Web_site]["FORMAT"]=checkformat.sub_alphanumeric(records.PCI_Web_site)
                                else:
                                    self.passed[records.PCI_Web_site]["FORMAT"]=False
                            else:
                                self.passed[str(records.PCI_Web_site)]["FORMAT"]=True
                yield self.passed
        except Exception as e:
            # Log
            pass  
