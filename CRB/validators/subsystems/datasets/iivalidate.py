from validators.subsystems import iicode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus

class IIValidate(ibvalidate.IBValidate):
    def __init__(self, code="II"):
        super(IIValidate, self).__init__()
        self._model = models.IDENTIFICATION_INFORMATION
        self.all_records = models.IDENTIFICATION_INFORMATION.objects.all()
        self.code = code 
        self.pi_c_code = iicode.IICode(self._model, self.code)
        
        self.all_records = models.CREDIT_APPLICATION.objects.all()
        
    def check_data_in_field(self, f, rules):        
        self.passed = {}

        try:
            if(f == "II_Registration_Certificate_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Registration_Certificate_Number):
                                self.passed[records.idi.II_Registration_Certificate_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Registration_Certificate_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Registration_Certificate_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Registration_Certificate_Number, records)
                                    ##print "FIST V STATUS ", self.vst
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Registration_Certificate_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Registration_Certificate_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Registration_Certificate_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Registration_Certificate_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Registration_Certificate_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Registration_Certificate_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Registration_Certificate_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Registration_Certificate_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Registration_Certificate_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Registration_Certificate_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Registration_Certificate_Number]["ENF"]=False
                        else:
                            if(len(records.idi.II_Registration_Certificate_Number) <= 20):
                                self.passed[records.idi.II_Registration_Certificate_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Registration_Certificate_Number)
                            else:
                                self.passed[records.idi.II_Registration_Certificate_Number]["FORMAT"]=False
                yield self.passed  
                
            elif(f == "II_Tax_Identification_Number"):
                self.pass_it = { }
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Tax_Identification_Number):
                                self.passed[records.idi.II_Tax_Identification_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Tax_Identification_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.third_priority = self.check_dict_values(r.get(key)[2])
                                
                                if(self.first_priority == 1 or self.first_priority == 2): 
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Tax_Identification_Number, records)
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Tax_Identification_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.idi.II_Tax_Identification_Number, records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False 
                                    else:
                                        self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False 
                                
                                elif(self.second_priority == 1 or self.second_priority == 2):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Tax_Identification_Number, records)

                                    if(self.validation_second == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.idi.II_Tax_Identification_Number, records)

                                        if(self.validation_first == True):
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                            
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records.idi.II_Tax_Identification_Number, records)
                                        
                                        if(self.validation_third == True):
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                            
                                    else:
                                        self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                        
                                elif(self.third_priority == 1 or self.third_priority == 2):
                                    self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                    self.validation_third = self.third_ef.validate_field(records.idi.II_Tax_Identification_Number, records)
                                    
                                    if(self.validation_third == True):
                                        #Perform the second validation given the first enforcements
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.idi.II_Tax_Identification_Number, records)

                                        if(self.validation_first == True):
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                            
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Tax_Identification_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Tax_Identification_Number, records)
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False
                                else:
                                    self.passed[records.idi.II_Tax_Identification_Number]["ENF"]=False

                        else:
                            if(records):
                                if(len(records.idi.II_Tax_Identification_Number) <= 20):
                                    tax = str(records.idi.II_Tax_Identification_Number).strip().lstrip().rstrip()
                                    if(tax):
                                        self.passed[records.idi.II_Tax_Identification_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Tax_Identification_Number)
                                    else:
                                        self.passed[records.idi.II_Tax_Identification_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Tax_Identification_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Tax_Identification_Number]["FORMAT"]=False
                yield self.passed 

            elif(f == "II_Value_Added_Tax_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Value_Added_Tax_Number):
                                self.passed[records.idi.II_Value_Added_Tax_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Value_Added_Tax_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Value_Added_Tax_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Value_Added_Tax_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Value_Added_Tax_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Value_Added_Tax_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Value_Added_Tax_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Value_Added_Tax_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Value_Added_Tax_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Value_Added_Tax_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Value_Added_Tax_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Value_Added_Tax_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Value_Added_Tax_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Value_Added_Tax_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Value_Added_Tax_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Value_Added_Tax_Number]["ENF"]=False

                        else:
                            if(records):
                                if(len(records.idi.II_Value_Added_Tax_Number) <= 20):
                                    II_value = records.idi.II_Value_Added_Tax_Number
                                    if(II_value):
                                        self.passed[records.idi.II_Value_Added_Tax_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Value_Added_Tax_Number)
                                    else:
                                        self.passed[records.idi.II_Value_Added_Tax_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Value_Added_Tax_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Value_Added_Tax_Number]["FORMAT"]=False
                yield self.passed 

            elif(f == "II_FCS_Number"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_FCS_Number):
                                self.passed[records.idi.II_FCS_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_FCS_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                self.three_priority = self.check_dict_values(r.get(key)[2])
                                self.four_priority = self.check_dict_values(r.get(key)[3])
                                self.five_priority = self.check_dict_values(r.get(key)[4])
                                self.six_priority = self.check_dict_values(r.get(key)[5])
                                self.seven_priority = self.check_dict_values(r.get(key)[6])
                                self.eight_priority = self.check_dict_values(r.get(key)[7])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_1 = self.first.validate_field(records)
                                    
                                    if(self.validation_1 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                elif(self.second_priority == 1 or self.second_priority ==2):
                                    self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                    
                                    if(self.validation_2 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                        
                                elif(self.three_priority == 1 or self.three_priority == 2):
                                    self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                                                     
                                    if(self.validation_3 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                         
                                elif(self.four_priority == 1 or self.four_priority == 2):
                                    self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                                                     
                                    if(self.validation_4 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                         
                                elif(self.five_priority == 1 or self.five_priority == 2):
                                    self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number, priority=r.get(key))
                                    self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                                                     
                                    if(self.validation_5 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                         
                                elif(self.six_priority == 1 or self.six_priority == 2):
                                    self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                                                     
                                    if(self.validation_6 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                         
                                elif(self.seven_priority == 1 or self.seven_priority == 2):
                                    self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                                                     
                                    if(self.validation_7 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(self.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_8 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                         
                                elif(self.eight_priority == 1 or self.eight_priority == 2):
                                    self.eight = checkenforcements.check_enforcements(self.get_keys(r.get(key)[7]), self._model, records.idi.II_FCS_Number, priority=r.get(key)) 
                                    self.validation_8 = self.eight.validate_field(records.idi.II_FCS_Number, records)
                                                                     
                                    if(self.validation_8 == True):
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        
                                        self.first = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_1 = self.first.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_1 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                            
                                        self.second = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_2 = self.second.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_2 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.third = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_3 = self.third.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_3 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.four = checkenforcements.check_enforcements(self.get_keys(r.get(key)[3]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_4 = self.four.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_4 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.five = checkenforcements.check_enforcements(self.get_keys(r.get(key)[4]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_5 = self.five.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_5 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                            
                                        self.six = checkenforcements.check_enforcements(records.idi.II_FCS_Number, records.get_keys(r.get(key)[5]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_6 = self.six.validate_field(records)
                                        if(self.validation_6 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                        
                                        self.seven = checkenforcements.check_enforcements(self.get_keys(r.get(key)[6]), self._model, records.idi.II_FCS_Number,  priority=r.get(key))
                                        self.validation_7 = self.seven.validate_field(records.idi.II_FCS_Number, records)
                                        if(self.validation_7 == True):
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_FCS_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_FCS_Number]["ENF"]=False 
                                else:
                                    pass 
                        else:
                            if(len(str(records.idi.II_FCS_Number)) >= 5):
                                self.passed[records.idi.II_FCS_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_FCS_Number)
                            else:
                                self.passed[records.idi.II_FCS_Number]["FORMAT"]=False
                #print self.passed 
                yield self.passed 

            elif(f == "II_Passport_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Passport_Number):
                                self.passed[records.idi.II_Passport_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Passport_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Passport_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Passport_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Passport_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Passport_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Passport_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Passport_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Passport_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Passport_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Passport_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records)
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Passport_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Passport_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Passport_Number]["ENF"]=False

                        else:
                            if(records):
                                if(len(records.idi.II_Passport_Number) <= 20):
                                    passport = str(records.idi.II_Passport_Number).strip().lstrip().rstrip()
                                    if(passport):
                                        self.passed[records.idi.II_Passport_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_Passport_Number)
                                    else:
                                        self.passed[records.idi.II_Passport_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Passport_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Passport_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Drivers_Licence_ID_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Drivers_Licence_ID_Number):
                                self.passed[records.idi.II_Drivers_Licence_ID_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Drivers_Licence_ID_Number]={"Conditional":False}

                        elif(isinstance(r, dict)): #92 99
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Drivers_Licence_ID_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Drivers_Licence_ID_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Drivers_Licence_ID_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Drivers_Licence_ID_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Drivers_Licence_ID_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Drivers_Licence_ID_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Drivers_Licence_ID_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Drivers_Licence_ID_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Drivers_Licence_ID_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records)
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Drivers_Licence_ID_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Drivers_Licence_ID_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Drivers_Licence_ID_Number]["ENF"]=False

                        else:
                            if(len(records.idi.II_Drivers_Licence_ID_Number) <= 20):
                                self.passed[records.idi.II_Drivers_Licence_ID_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Drivers_Licence_ID_Number)
                            else:
                                self.passed[records.idi.II_Drivers_Licence_ID_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Voters_PERNO"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Voters_PERNO):
                                self.passed[records.idi.II_Voters_PERNO]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Voters_PERNO]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Voters_PERNO, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Voters_PERNO, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Voters_PERNO, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Voters_PERNO, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Voters_PERNO]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Voters_PERNO]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Voters_PERNO]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Voters_PERNO, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Voters_PERNO, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records)
                                    self.validation_second = self.sec_enf.validate_field(records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Voters_PERNO]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Voters_PERNO]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Voters_PERNO]["ENF"]=False

                        else:
                            if(len(records.idi.II_Voters_PERNO) <= 20):
                                self.passed[records.idi.II_Voters_PERNO]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Voters_PERNO)
                            else:
                                self.passed[records.idi.II_Voters_PERNO]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Drivers_License_Permit_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Drivers_License_Permit_Number):
                                self.passed[records.idi.II_Drivers_License_Permit_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Drivers_License_Permit_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Drivers_License_Permit_Number, priority=r.get(key))
                                    #print self.vstatus
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Drivers_License_Permit_Number, records)
                                    #print "First Permission ", self.vstatus.validate_field(records.idi.II_Drivers_License_Permit_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Drivers_License_Permit_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Drivers_License_Permit_Number, records)
                                        #print "Second permit", self.sec_enf.validate_field(records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Drivers_License_Permit_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Drivers_License_Permit_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Drivers_License_Permit_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Drivers_License_Permit_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Drivers_License_Permit_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Drivers_License_Permit_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Drivers_License_Permit_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Drivers_License_Permit_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Drivers_License_Permit_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Drivers_License_Permit_Number]["ENF"]=False

                        else:
                            if(len(records.idi.II_Drivers_License_Permit_Number) <= 20):
                                self.passed[records.idi.II_Drivers_License_Permit_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Drivers_License_Permit_Number)
                            else:
                                self.passed[records.idi.II_Drivers_License_Permit_Number]["FORMAT"]=False
                #print "PERMIT ", self.passed
                yield self.passed 
                
            elif(f == "II_NSSF_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_NSSF_Number):
                                self.passed[records.idi.II_NSSF_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_NSSF_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_NSSF_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_NSSF_Number, records)
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_NSSF_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_NSSF_Number, records)
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_NSSF_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_NSSF_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_NSSF_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_NSSF_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_NSSF_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_NSSF_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_NSSF_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_NSSF_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_NSSF_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_NSSF_Number]["ENF"]=False

                        else:
                            if(records):
                                if(len(records.idi.II_NSSF_Number) <= 20):
                                    nssf = records.idi.II_NSSF_Number
                                    if(nssf):
                                        self.passed[records.idi.II_NSSF_Number]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_NSSF_Number)
                                    else:
                                        self.passed[records.idi.II_NSSF_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_NSSF_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_NSSF_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Country_ID"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Country_ID):
                                self.passed[records.idi.II_Country_ID]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Country_ID]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Country_ID, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Country_ID, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Country_ID, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Country_ID, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Country_ID]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Country_ID]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_NSSF_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Country_ID, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Country_ID, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Country_ID, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Country_ID, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Country_ID]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Country_ID]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Country_ID]["ENF"]=False

                        else:
                            if(records):
                                if(len(records.idi.II_Country_ID) <= 20):
                                    ii_country_id = str(records.idi.II_Country_ID).strip().lstrip().rstrip()
                                    if(ii_country_id):
                                        self.passed[records.idi.II_Country_ID]["FORMAT"]=checkformat.has_numerics_re(records.idi.II_Country_ID)
                                    else:
                                        self.passed[records.idi.II_Country_ID]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Country_ID]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Country_ID]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Country_Issuing_Authority"):
                    self.pass_it = { }
                    for records in self.all_records:
                        for r in rules:
                            if r == "C":
                                if(records.idi.II_Country_Issuing_Authority):
                                    self.passed[records.idi.II_Country_Issuing_Authority]={"Conditional":True}
                                else:
                                    self.passed[records.idi.II_Country_Issuing_Authority]={"Conditional":True} 
                                    
                            elif(isinstance(r, dict)):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.idi.II_Country_Issuing_Authority, priority=r.get(key))
                                    self.passed[records.idi.II_Country_Issuing_Authority]["ENF"]=self.statuss.validate_field(records.idi.II_Country_Issuing_Authority,records)
                            else:
                                if(records):
                                    if(len(records.idi.II_Country_Issuing_Authority) >= 1):
                                        country_issue = str(records.idi.II_Country_Issuing_Authority).strip().lstrip().rstrip()
                                        if(country_issue):
                                            self.passed[records.idi.II_Country_Issuing_Authority]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_Country_Issuing_Authority)
                                        else:
                                            #print "Failed record test 1"
                                            self.passed[records.idi.II_Country_Issuing_Authority]["FORMAT"]=False
                                    else:
                                        #print "Filed record test 2", records.idi.II_Country_Issuing_Authority, len(records.idi.II_Country_Issuing_Authority)
                                        self.passed[records.idi.II_Country_Issuing_Authority]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Country_Issuing_Authority]["FORMAT"]=False
                    #print "II_Country_Issuing_Authority ", self.passed     
                    yield self.passed 
                    
            elif(f == "II_Nationality"):
                    self.pass_it = { }
                    for records in self.all_records:
                        for r in rules:
                            if r == "C":
                                if(records.idi.II_Nationality):
                                    self.passed[records.idi.II_Nationality]={"Conditional":True}
                                else:
                                    self.passed[records.idi.II_Nationality]={"Conditional":True} 
                                    
                            elif(isinstance(r, dict)):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    self.third_priority = self.check_dict_values(r.get(key)[2])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2): 
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.idi.II_Nationality, records)
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.idi.II_Nationality]["ENF"]=True 
                                            else:
                                                self.passed[records.idi.II_Nationality]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.idi.II_Nationality]["ENF"]=True
                                            else:
                                                self.passed[records.idi.II_Nationality]["ENF"]=False 
                                        else:
                                            self.passed[records.idi.II_Nationality]["ENF"]=False 
                                    
                                    elif(self.second_priority == 1 or self.second_priority == 2):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records)

                                        if(self.validation_second == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records)

                                            if(self.validation_first == True):
                                                self.passed[records.idi.II_Nationality]["ENF"]=True 
                                            else:
                                                self.passed[records.II_Nationality]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.idi.II_Nationality]["ENF"]=True
                                            else:
                                                self.passed[records.idi.II_Nationality]["ENF"]=False
                                                
                                        else:
                                            self.passed[records.idi.II_Nationality]["ENF"]=False
                                            
                                    elif(self.third_priority == 1 or self.third_priority == 2):
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records)
                                        
                                        if(self.validation_third == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records)

                                            if(self.validation_first == True):
                                                self.passed[records.idi.II_Nationality]["ENF"]=True 
                                            else:
                                                self.passed[records.idi.II_Nationality]["ENF"]=False
                                                
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Nationality, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records)
                                            if(self.validation_second == True):
                                                self.passed[records.idi.II_Nationality]["ENF"]=True
                                            else:
                                                self.passed[records.idi.II_Nationality]["ENF"]=False
                                        else:
                                            self.passed[records.idi.II_Nationality]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Nationality]["ENF"]=False
                            else:
                                if(len(records.idi.II_Nationality) >= 2):
                                    self.passed[records.idi.II_Nationality]["FORMAT"]=True #checkformat.has_numerics_re(records.idi.II_Nationality)
                                else:
                                    self.passed[records.idi.II_Nationality]["FORMAT"]=False
                    yield self.passed 
            
            elif(f == "II_Police_ID_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Police_ID_Number):
                                self.passed[records.idi.II_Police_ID_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Police_ID_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Police_ID_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Police_ID_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Police_ID_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Police_ID_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Police_ID_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Police_ID_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Police_ID_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Police_ID_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Police_ID_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Police_ID_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Police_ID_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Police_ID_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Police_ID_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Police_ID_Number]["ENF"]=False
                        else:
                            if(records):
                                if(len(records.idi.II_Police_ID_Number) <= 20):
                                    police_id = str(records.idi.II_Passport_Number).strip().lstrip().rstrip()
                                    if(police_id):
                                        self.passed[records.idi.II_Police_ID_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_Police_ID_Number)
                                    else:
                                        self.passed[records.idi.II_Police_ID_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Police_ID_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Police_ID_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_UPDF_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_UPDF_Number):
                                self.passed[records.idi.II_UPDF_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_UPDF_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_UPDF_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_UPDF_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_UPDF_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_UPDF_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_UPDF_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_UPDF_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_UPDF_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_UPDF_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_UPDF_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_UPDF_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_UPDF_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_UPDF_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_UPDF_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_UPDF_Number]["ENF"]=False
                        else:
                            if(records):
                                if(len(records.idi.II_UPDF_Number) <= 20):
                                    updf_number = str(records.idi.II_UPDF_Number).strip().lstrip().rstrip()
                                    if(updf_number):
                                        self.passed[records.idi.II_UPDF_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_UPDF_Number)
                                    else:
                                        self.passed[records.idi.II_UPDF_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_UPDF_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_UPDF_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_KACITA_License_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_KACITA_License_Number):
                                self.passed[records.idi.II_KACITA_License_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_KACITA_License_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_KACITA_License_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_KACITA_License_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_KACITA_License_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_KACITA_License_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_KACITA_License_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_KACITA_License_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_KACITA_License_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_KACITA_License_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_KACITA_License_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_KACITA_License_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_KACITA_License_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_KACITA_License_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_KACITA_License_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_KACITA_License_Number]["ENF"]=False
                        else:
                            if(records):
                                if(len(records.idi.II_KACITA_License_Number) <= 20):
                                    kacita = str(records.idi.II_KACITA_License_Number).strip().lstrip().rstrip()
                                    if(kacita):
                                        self.passed[records.idi.II_KACITA_License_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_KACITA_License_Number)
                                    else:
                                        self.passed[records.idi.II_KACITA_License_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_KACITA_License_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_KACITA_License_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Public_Service_Pension_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Public_Service_Pension_Number):
                                self.passed[records.idi.II_Public_Service_Pension_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Public_Service_Pension_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Public_Service_Pension_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Public_Service_Pension_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Public_Service_Pension_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Public_Service_Pension_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Public_Service_Pension_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Public_Service_Pension_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Public_Service_Pension_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Public_Service_Pension_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Public_Service_Pension_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Public_Service_Pension_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Public_Service_Pension_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Public_Service_Pension_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Public_Service_Pension_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Public_Service_Pension_Number]["ENF"]=False
                        else:
                            if(records):
                                if(len(records.idi.II_Public_Service_Pension_Number) <= 20):
                                    pension = str(records.idi.II_Public_Service_Pension_Number).strip().lstrip().rstrip()
                                    if(pension):
                                        self.passed[records.idi.II_Public_Service_Pension_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_Public_Service_Pension_Number)
                                    else:
                                        self.passed[records.idi.II_Public_Service_Pension_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Public_Service_Pension_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Public_Service_Pension_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Teacher_Registration_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.idi.II_Teacher_Registration_Number):
                                self.passed[records.idi.II_Teacher_Registration_Number]={"Conditional":True}
                            else:
                                self.passed[records.idi.II_Teacher_Registration_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Teacher_Registration_Number, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Teacher_Registration_Number, records)
                                    
                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Teacher_Registration_Number, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.idi.II_Teacher_Registration_Number, records)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Teacher_Registration_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.idi.II_Teacher_Registration_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Teacher_Registration_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Teacher_Registration_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Teacher_Registration_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.idi.II_Teacher_Registration_Number, records)
                                    self.validation_second = self.sec_enf.validate_field(records.idi.II_Teacher_Registration_Number, records)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.idi.II_Teacher_Registration_Number]["ENF"]=True
                                        else:
                                            self.passed[records.idi.II_Teacher_Registration_Number]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Teacher_Registration_Number]["ENF"]=False
                        else:
                            if(records):
                                if(len(records.idi.II_Teacher_Registration_Number) <= 20):
                                    teachers_reg = str(records.idi.II_Teacher_Registration_Number).strip().lstrip().rstrip()
                                    if(teachers_reg):
                                        self.passed[records.idi.II_Teacher_Registration_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_Teacher_Registration_Number)
                                    else:
                                        self.passed[records.idi.II_Teacher_Registration_Number]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Teacher_Registration_Number]["FORMAT"]=False
                            else:
                                self.passed[records.idi.II_Teacher_Registration_Number]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "II_Country_Of_Issue"):
                    self.pass_it = { }
                    for records in self.all_records:
                        for r in rules:
                            if r == "C":
                                if(records.idi.II_Country_Of_Issue):
                                    self.passed[records.idi.II_Country_Of_Issue]={"Conditional":True}
                                else:
                                    self.passed[records.idi.II_Country_Of_Issue]={"Conditional":True} 
                                    
                            elif(isinstance(r, dict)):
                                for key in r:
                                    self.first_priority = self.check_dict_values(r.get(key)[0])
                                    self.second_priority = self.check_dict_values(r.get(key)[1])
                                    self.third_priority = self.check_dict_values(r.get(key)[2])
                                    
                                    if(self.first_priority == 1 or self.first_priority == 2): 
                                        self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                        self.validation_first = self.vstatus.validate_field(records.idi.II_Country_Of_Issue, re_enfor=None)
                                        if(self.validation_first == True):
                                            #Perform the second validation
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records.idi.II_Country_Of_Issue ,records)
                                            
                                            if(self.validation_second == True):
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=True 
                                            else:
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get(key)[2]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records.idi.II_Country_Of_Issue,records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=True
                                            else:
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False 
                                        else:
                                            self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False 
                                    
                                    elif(self.second_priority == 1 or self.second_priority == 2):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records, re_enfor=records)

                                        if(self.validation_second == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(records.idi.II_Country_Of_Issue,re_enfor=records)

                                            if(self.validation_first == True):
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=True 
                                            else:
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                                
                                            self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                            self.validation_third = self.third_ef.validate_field(records,re_enfor=records)
                                            
                                            if(self.validation_third == True):
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=True
                                            else:
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                                
                                        else:
                                            self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                            
                                    elif(self.third_priority == 1 or self.third_priority == 2):
                                        self.third_ef = checkenforcements.check_enforcements(self.get_keys(r.get.key()[2]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                        self.validation_third = self.third_ef.validate_field(records,re_enfor=records)
                                        
                                        if(self.validation_third == True):
                                            #Perform the second validation given the first enforcements
                                            self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                            self.validation_first = self.vstatus.validate_field(record.idi.II_Country_Of_Issue, re_enfor=records)

                                            if(self.validation_first == True):
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=True 
                                            else:
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                                
                                            self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.idi.II_Country_Of_Issue, priority=r.get(key))
                                            self.validation_second = self.sec_enf.validate_field(records,re_enfor=records)
                                            if(self.validation_second == True):
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=True
                                            else:
                                                self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                        else:
                                            self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                                    else:
                                        self.passed[records.idi.II_Country_Of_Issue]["ENF"]=False
                            else:
                                if(records):
                                    if(len(records.idi.II_Country_Of_Issue) >= 2):
                                        country_of_issue = str(records.idi.II_Country_Of_Issue).strip().lstrip().rstrip()
                                        if(country_of_issue):
                                            self.passed[records.idi.II_Country_Of_Issue]["FORMAT"]=True #checkformat.sub_alphanumeric(records.idi.II_Country_Of_Issue)
                                        else:
                                            self.passed[records.idi.II_Country_Of_Issue]["FORMAT"]=False
                                    else:
                                        self.passed[records.idi.II_Country_Of_Issue]["FORMAT"]=False
                                else:
                                    self.passed[records.idi.II_Country_Of_Issue]["FORMAT"]=False
                    yield self.passed
        except Exception as e:
            # Log
            print e
            pass  
