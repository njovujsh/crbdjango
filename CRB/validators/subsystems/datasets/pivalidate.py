#  pivalidate.py
#  
#  Copyright 2015 Wangolo Joel <wangolo@developer>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from validators.subsystems import picode 
from datasetrecords import models 
from validators.subsystems import checkstatus 
from validators.subsystems import checkformat 
from validators.subsystems import checkenforcements 
from validators.subsystems.csvwriters  import writers 
from validators.subsystems.datasets import validationstatus 
from collections import defaultdict 
#from validators.subsystems.datasets import pcivalidate 
from branchcode import models as branchmodels
from datasetrecords import searchfilters

class PIValidate(object):
    def __init__(self, code="PI"):
        self.running = True 
        self._model = models.PARTICIPATING_INSTITUTION
        self.all_records = self.filter_new_old_records(models.PARTICIPATING_INSTITUTION)
        self.code = code 
        self.pi_c_code = picode.PICode(self._model, self.code)
        self.headers = branchmodels.RequiredHeader.objects.all()
        self.dict_list = []
        self.real_passed = {}        
    
    def begin_validation(self):
        try:
            self.all_fields = self.pi_c_code.extract()
            self.examine_field(self.all_fields)
        except Exception as e:
            # Log 
            pass  
            
    def examine_field(self, field):
        try:
            for f in field:
                try:
                    self.ret_require = self.get_field_requirement(f).next()
                except StopIteration as error:
                    pass 
                else:
                    self.checked_data = self.check_data_in_field(f, self.ret_require)
                    if(self.checked_data):
                        try:
                            self.real_passed[f]=self.checked_data.next()
                        except StopIteration as error:
                            pass 
                    else:
                        print "No data is found"
        except:
            pass 
            
                        
    def get_field_requirement(self, field):
        try:
            for all_field in self.pi_c_code.join_field_rule():
                for v_field in all_field.values():
                    f = v_field.get(field)
                    if(f == None):
                        pass 
                    else:
                        yield f
        except:
            pass 
    
    def check_data_in_field(self, f, rules):
        self.passed = { }
        
        try:
            if(f == "PI_Identification_Code"):
                self.pass_pi = {}
                self.final_result = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.PI_Identification_Code):
                                if(records.PI_Identification_Code.pi_identification_code):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]={"Mandatory":True}
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]={"Mandatory":False} 
                            else:
                                self.passed[str(records.PI_Identification_Code)]={"Mandatory":False} 
                            
                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.PI_Identification_Code):
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                                else:
                                    self.passed[str(records.PI_Identification_Code)]["ENF"]=self.statuss.validate_field(str(records.PI_Identification_Code))
                        else:
                            if(records.PI_Identification_Code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                                if(len(self.parseddata) == 6 or len(self.parseddata) <= 8):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code)]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Institution_Type"):
                self.pass_it = { }
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Institution_Type):
                                if(records.Institution_Type):
                                    self.passed[records.Institution_Type]={"Mandatory":True}
                                else:
                                    self.passed[records.Institution_Type]={"Mandatory":False} 
                            else:
                                self.passed[str(records.Institution_Type)]={"Mandatory":False} 
                                
                        elif(isinstance(r, dict)):
                            for key in r:
                                if(records.Institution_Type):
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Institution_Type, priority=r.get(key))
                                    self.passed[records.Institution_Type]["ENF"]=self.statuss.validate_field(records.Institution_Type)
                                else:
                                    self.passed[str(records.Institution_Type)]["ENF"]=self.statuss.validate_field(str(records.Institution_Type))
                        else:
                            if(records.Institution_Type):
                                if(len(records.Institution_Type) == 3 or len(records.Institution_Type) == 2):
                                    self.passed[records.Institution_Type]["FORMAT"]=checkformat.sub_alphanumeric(records.Institution_Type)
                                else:
                                    self.passed[records.Institution_Type]["FORMAT"]=False
                            else:
                                self.passed[str(records.Institution_Type)]["FORMAT"]=False 
                #print self.passed
                yield self.passed 
                
            elif(f == "Institution_Name"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Institution_Name):
                                self.passed[records.Institution_Name]={"Mandatory":True}
                            else:
                                self.passed[records.Institution_Name]={"Mandatory":True}
                                
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Institution_Name, priority=r.get(key))
                                self.passed[records.Institution_Name]["ENF"]=self.statuss.validate_field(records.Institution_Name)
                        else:
                            if(len(records.Institution_Name) <= 100 or len(records.Institution_Name)  == 5):
                                self.passed[records.Institution_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.Institution_Name)  
                            else:
                                self.passed[records.Institution_Name]["FORMAT"]=False 
                            
                yield self.passed 
                
            elif(f == "License_Issuing_Date"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.License_Issuing_Date):
                                self.passed[records.License_Issuing_Date]={"Mandatory":True}
                            else:
                                self.passed[records.License_Issuing_Date]={"Mandatory":True}
                                
                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])
                                
                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.License_Issuing_Date)
                                    
                                    if(self.validation_first == True):
                                        #Perform the second validation
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.License_Issuing_Date)
                                        
                                        if(self.validation_second == True):
                                            self.passed[records.License_Issuing_Date]["ENF"]=True 
                                        else:
                                            self.passed[records.License_Issuing_Date]["ENF"]=False
                                    else:
                                        self.passed[records.License_Issuing_Date]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.License_Issuing_Date)
                                    self.validation_second = self.sec_enf.validate_field(records.License_Issuing_Date, headers=self.headers)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.License_Issuing_Date]["ENF"]=True
                                        else:
                                            self.passed[records.License_Issuing_Date]["ENF"]=False
                                    else:
                                        self.passed[records.License_Issuing_Date]["ENF"]=False 
                            
                        else:
                            if(len(records.License_Issuing_Date.replace("-", "", 10)) == 8):
                                self.passed[records.License_Issuing_Date]["FORMAT"]=checkformat.is_numeric(records.License_Issuing_Date.replace("-", "",10))
                            else:
                                self.passed[records.License_Issuing_Date]["FORMAT"]=False
                yield self.passed 
                
            else:
                print "Uknown FIELD ", f
        except Exception as e:
            # Log
            pass 
        else:
            print "FINAL ", self.dict_list
        
    def set_code(self, dc_code):
        self.pi_c_code = dc_code
    
    def check_dict_values(self, s):
        for value in s.values():
            return value.get("P")
            
    def merged_dict(self):
        return defaultdict(list) 
        
    def get_keys(self, key_list):
        for k in key_list.keys():
            return k
            
    def add_dict_to_list(self, newdict):
        if(newdict):
            try:
                self.dict_list.append(newdict)
            except:
                pass 
        else:
            return False 
            
    def merged_dictionary(self, dictlist):
        self.merged = self.merged_dict()
        try:
            if(dictlist):
                for dict_items in dictlist:
                    if(isinstance(dict_items, int)):
                        pass 
                    else:
                        for k, v in dict_items.items():
                            self.merged[k].append(v)
            else:
                return None
        except:
            pass 
        else:
            return self.merged 
                
    def get_dict_list(self, in_tuple=False):
        if(in_tuple):
            return tuple(self.dict_list)
        else:
            return self.dict_list
        
    def get_real_dict(self):
        return self.real_passed
        
    def add_dict_to_list(self, dic, in_tuple=False):
        if(in_tuple):
            return tuple([dic])
        else:
            return [dic]

    def filter_new_old_records(self, model_db_records, get_new=True):
        """
        Filter and return new or old records.
        """
        if(get_new):
            test_all = model_db_records.objects.all()
            if(test_all):
                return model_db_records.objects.filter(date__gte=searchfilters.get_first_filter_date(), date__lte=searchfilters.get_last_filter_date())
            else:
                return test_all
        else:
            return model_db_records.objects.filter(date__gte=searchfilters.get_first_filter_date())
