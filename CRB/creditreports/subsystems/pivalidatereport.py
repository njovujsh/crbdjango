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
from validators.subsystems.datasets import ibvalidate
from branchcode import models as branchmodels

class ReportPIValidate(ibvalidate.IBValidate):
    def __init__(self, code="PI"):
        self.running = True
        self._model = models.PARTICIPATING_INSTITUTION
        self.all_records = models.PARTICIPATING_INSTITUTION.objects.all()
        self.all_count = models.PARTICIPATING_INSTITUTION.objects.all().count()
        self.code = code
        self.pi_c_code = picode.PICode(self._model, self.code)
        self.headers = branchmodels.RequiredHeader.objects.all()

        self.record_fields = 4 
        self.passed_by_id = {}
        self.real_passed = {}

        self.validated_values = 0
        self.failed_values = 0
        
        self.all_records_passed = {}
        self.begin_feel = {}
        self.global_list = []
        
        self.passed = {}
        self.passed_results = {}
        
    def begin_validation(self):
        try:
            self.all_fields = self.pi_c_code.extract()
            self.examine_field(self.all_fields)
        except Exception as e:
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
        self.dicts = {}
        try:
            self.validate_PI(f, rules)
            self.validate_IT(f, rules)
            self.validate_IN(f, rules)
            self.validate_DATE(f, rules)
            #print self.final_result
        except Exception as e:
            # Log
            pass
        else:
            yield self.final_result
            
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
                            if(records.PI_Identification_Code.pi_identification_code):
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                            else:
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(str(records.PI_Identification_Code.pi_identification_code))
                    else:
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata) == 6 or len(self.parseddata) <= 8):
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
            
    def validate_DATE(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "License_Issuing_Date"):
                self.pass_lidd = {}
                self.final_resultd = {}
                
                for r in rules:
                    if r == "M":
                        if(records.License_Issuing_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])

                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(str(records.License_Issuing_Date).replace("-", "", 10))
                                if(self.validation_first == True):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.License_Issuing_Date)

                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.License_Issuing_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.License_Issuing_Date, priority=r.get(key))

                                self.validation_first = self.vstatus.validate_field(records.License_Issuing_Date)
                                self.validation_second = self.sec_enf.validate_field(records.License_Issuing_Date, headers=self.headers)

                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            self.passed[records.id]["ENF"]=True
                        
                    else:
                        self.replaceddate = records.License_Issuing_Date.replace('-',"", 10)
                        if(len(self.replaceddate) == 8): 
                            self.passed[records.id]["FORMAT"]=checkformat.is_numeric(self.replaceddate)
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
        
    def validate_IN(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Institution_Name"):
                for r in rules:
                    if r == "M":
                        if(records.Institution_Name):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":True}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Institution_Name, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Institution_Name)
                    else:
                        if(len(records.Institution_Name) <= 100 or len(records.Institution_Name)  == 5):
                            self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Institution_Name)
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
        
    def validate_IT(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Institution_Type"):
                self.pass_it = {}
                self.final_result = {}
                #for records in self.all_records:
                for r in rules:
                    if r == "M":
                        if(records.Institution_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":True}
    
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Institution_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Institution_Type)
                    else:
                        if(records.Institution_Type):
                            if(len(records.Institution_Type) == 3 or len(records.Institution_Type) == 2):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Institution_Type)
                            else:
                                self.passed[records.id]["FORMAT"]=False
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
            
    def get_passed_records(self):
        """
        Return the total number of records passed.
        """
        return self.validated_values

    def get_failed_records(self):
        """
        Return the total number of records failed.
        """
        return self.failed_values

    def set_code(self, dc_code):
        self.pi_c_code = dc_code

    def merged_dict(self):
        return defaultdict(list)

    def add_dict_to_list(self, newdict):
        if(newdict):
            try:
                self.dict_list.append(newdict)
            except:
                pass
        else:
            return False

    def analysis_records(self):
        """
        Analyse and return faield records.
        """
        for keys in self.get_passed_by_id():
            #print ":", self.get_passed_by_id().get(keys)
            if(self.get_passed_by_id().get(keys).count(3) == self.get_num_fields()):
                self.validated_values +=1 
            else:
                self.failed_values += 1
            
    def get_num_fields(self):
        return self.record_fields
        
    def get_dict_list(self, in_tuple=False):
        if(in_tuple):
            return tuple(self.dict_list)
        else:
            return self.dict_list

    def get_real_dict(self):
        return self.real_passed

    def get_real_passed(self):
        return self.real_passed

    def get_passed_by_id(self):
       return self.passed_by_id
       
    def get_num_records(self):
        return self.all_records.count()
        
class PCIValidate(ibvalidate.IBValidate):
    def __init__(self, code="PCI"):
        super(PCIValidate, self).__init__(code=code)

        self._model = models.PCI
        self.all_records = models.PARTICIPATING_INSTITUTION.objects.all()
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
                            if(records.pci.PCI_Building_Unit_Number):
                                self.passed[records.pci.PCI_Building_Unit_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Building_Unit_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Building_Unit_Number, priority=r.get(key))
                                self.passed[records.pci.PCI_Building_Unit_Number]["ENF"]=self.statuss.validate_field(records.pci.PCI_Building_Unit_Number)
                        else:
                            if(len(records.pci.PCI_Building_Unit_Number) <=10):
                                self.passed[records.pci.PCI_Building_Unit_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Building_Unit_Number)
                            else:
                                self.passed[records.pci.PCI_Building_Unit_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Building_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Building_Name):
                                self.passed[records.pci.PCI_Building_Name]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Building_Name]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Building_Name, priority=r.get(key))
                                self.passed[records.pci.PCI_Building_Name]["ENF"]=self.statuss.validate_field(records.pci.PCI_Building_Name)
                        else:
                            if(len(records.pci.PCI_Building_Name) <=50):
                                self.passed[records.pci.PCI_Building_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Building_Name)
                            else:
                                self.passed[records.pci.PCI_Building_Name]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Floor_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Floor_Number):
                                self.passed[records.pci.PCI_Floor_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Floor_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Floor_Number, priority=r.get(key))
                                self.passed[records.pci.PCI_Floor_Number]["ENF"]=self.statuss.validate_field(records.pci.PCI_Floor_Number)
                        else:
                            if(len(records.pci.PCI_Floor_Number) <=10):
                                self.passed[records.pci.PCI_Floor_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Floor_Number)
                            else:
                                self.passed[records.pci.PCI_Floor_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Plot_or_Street_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.pci.PCI_Plot_or_Street_Number):
                                self.passed[records.pci.PCI_Plot_or_Street_Number]={"Optional":True}
                            else:
                                self.passed[records.pci.PCI_Plot_or_Street_Number]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Plot_or_Street_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(len(records.pci.PCI_Plot_or_Street_Number) <=10):
                                self.passed[records.pci.PCI_Plot_or_Street_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Plot_or_Street_Number)
                            else:
                                self.passed[records.pci.PCI_Plot_or_Street_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_LC_or_Street_Name"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.pci.PCI_LC_or_Street_Name):
                                self.passed[records.pci.PCI_LC_or_Street_Name]={"Optional":True}
                            else:
                                self.passed[records.pci.PCI_LC_or_Street_Name]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_LC_or_Street_Name]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(len(records.pci.PCI_LC_or_Street_Name) <=50):
                                self.passed[records.pci.PCI_LC_or_Street_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_LC_or_Street_Name)
                            else:
                                self.passed[records.pci.PCI_LC_or_Street_Name]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Parish"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Parish):
                                self.passed[records.pci.PCI_Parish]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Parish]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_Parish, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.PCI_Parish)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_Parish, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.pci.PCI_Parish)

                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_Parish]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_Parish]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_Parish]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_Parish, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_Parish, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_Parish)
                                    self.validation_second = self.sec_enf.validate_field(records.pci.PCI_Parish)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_Parish]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_Parish]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_Parish]["ENF"]=False
                        else:
                            if(records.pci.PCI_Parish):
                                if(len(records.pci.PCI_Parish) <=50):
                                    self.passed[records.pci.PCI_Parish]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Parish)
                                else:
                                    self.passed[records.pci.PCI_Parish]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Parish]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Suburb"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.pci.PCI_Suburb):
                                self.passed[records.pci.PCI_Suburb]={"Optional":True}
                            else:
                                self.passed[records.pci.PCI_Suburb]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Suburb]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(len(records.pci.PCI_Suburb) <=50):
                                self.passed[records.pci.PCI_Suburb]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Suburb)
                            else:
                                self.passed[records.pci.PCI_Suburb]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Village"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "O":
                            if(records.pci.PCI_Village):
                                self.passed[records.pci.PCI_Village]={"Optional":True}
                            else:
                                self.passed[records.pci.PCI_Village]={"Optional":True}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Plot_or_Street_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Village]["ENF"]= True #self.statuss.validate_field(records.PCI_Plot_or_Street_Number)
                        else:
                            if(len(records.pci.PCI_Village) <=50):
                                self.passed[records.pci.PCI_Village]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Village)
                            else:
                                self.passed[records.pci.PCI_Village]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_County_or_Town"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_County_or_Town):
                                self.passed[records.pci.PCI_County_or_Town]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_County_or_Town]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_County_or_Town, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_County_or_Town)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_County_or_Town, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.pci.PCI_County_or_Town)

                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_County_or_Town]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_County_or_Town]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_County_or_Town]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_County_or_Town, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_County_or_Town, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_County_or_Town)
                                    self.validation_second = self.sec_enf.validate_field(records.pci.PCI_County_or_Town)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_County_or_Town]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_County_or_Town]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_County_or_Town]["ENF"]=False
                        else:
                            if(records.pci.PCI_County_or_Town):
                                if(len(records.pci.PCI_County_or_Town) <=50):
                                    self.passed[records.pci.PCI_County_or_Town]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_County_or_Town)
                                else:
                                    self.passed[records.pci.PCI_County_or_Town]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_County_or_Town]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_District"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_District):
                                self.passed[records.pci.PCI_District]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_District]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_District, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_District)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_District, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.pci.PCI_District)

                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_District]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_District]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_District]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_District, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_District, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_District)
                                    self.validation_second = self.sec_enf.validate_field(records.pci.PCI_District)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_District]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_District]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_District]["ENF"]=False
                        else:
                            if(records.pci.PCI_District):
                                if(len(records.pci.PCI_District) <=50):
                                    self.passed[records.pci.PCI_District]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_District)
                                else:
                                    self.passed[records.pci.PCI_District]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_District]["FORMAT"]=False

                yield self.passed

            elif(f == "PCI_Region"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Region):
                                self.passed[records.pci.PCI_Region]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Region]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_Region, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.PCI_Region)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_Region, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.pci.PCI_Region)

                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_Region]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_Region]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_Region]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_Region, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_Region, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_Region)
                                    self.validation_second = self.sec_enf.validate_field(records.pci.PCI_Region)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_Region]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_Region]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_Region]["ENF"]=False
                        else:
                            if(records.pci.PCI_Region):
                                if(len(records.pci.PCI_Region) <=5):
                                    self.passed[records.pci.PCI_Region]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Region)
                                else:
                                    self.passed[records.pci.PCI_Region]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Region]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_PO_Box_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_PO_Box_Number):
                                self.passed[records.pci.PCI_PO_Box_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_PO_Box_Number]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_PO_Box_Number, priority=r.get(key))
                                self.passed[records.pci.PCI_PO_Box_Number]["ENF"]=self.statuss.validate_field(records.pci.PCI_PO_Box_Number)
                        else:
                            if(len(records.pci.PCI_PO_Box_Number) <=10):
                                self.passed[records.pci.PCI_PO_Box_Number]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_PO_Box_Number)
                            else:
                                self.passed[records.pci.PCI_PO_Box_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Post_Office_Town"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Post_Office_Town):
                                self.passed[records.pci.PCI_Post_Office_Town]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Post_Office_Town]={"Conditional":True}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Post_Office_Town, priority=r.get(key))
                                self.passed[records.pci.PCI_Post_Office_Town]["ENF"]=self.statuss.validate_field(records.pci.PCI_Post_Office_Town)
                        else:
                            if(len(records.pci.PCI_Post_Office_Town) <=20):
                                self.passed[records.pci.PCI_Post_Office_Town]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Post_Office_Town)
                            else:
                                self.passed[records.pci.PCI_Post_Office_Town]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Country_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.pci.PCI_Country_Code):
                                self.passed[records.pci.PCI_Country_Code]={"Mandatory":True}
                            else:
                                self.passed[records.pci.PCI_Country_Code]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.first_priority = self.check_dict_values(r.get(key)[0])
                                self.second_priority = self.check_dict_values(r.get(key)[1])

                                if(self.first_priority == 1 or self.first_priority == 2):
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_Country_Code, priority=r.get(key))
                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_Country_Code)

                                    if(self.validation_first == True):
                                        self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_Country_Code, priority=r.get(key))
                                        self.validation_second = self.sec_enf.validate_field(records.pci.PCI_Country_Code)

                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_Country_Code]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_Country_Code]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_Country_Code]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.pci.PCI_Country_Code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.pci.PCI_Country_Code, priority=r.get(key))

                                    self.validation_first = self.vstatus.validate_field(records.pci.PCI_Country_Code)
                                    self.validation_second = self.sec_enf.validate_field(records.pci.PCI_Country_Code)

                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.pci.PCI_Country_Code]["ENF"]=True
                                        else:
                                            self.passed[records.pci.PCI_Country_Code]["ENF"]=False
                                    else:
                                        self.passed[records.pci.PCI_Country_Code]["ENF"]=False
                        else:
                            if(records.pci.PCI_Country_Code):
                                if(len(records.pci.PCI_Country_Code) <=5):
                                    self.passed[records.pci.PCI_Country_Code]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Country_Code)
                                else:
                                    self.passed[records.pci.PCI_Country_Code]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Country_Code]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Period_At_Address"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.pci.PCI_Period_At_Address):
                                self.passed[records.pci.PCI_Period_At_Address]={"Mandatory":True}
                            else:
                                self.passed[records.pci.PCI_Period_At_Address]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Period_At_Address, priority=r.get(key))
                                self.passed[records.pci.PCI_Period_At_Address]["ENF"]=self.statuss.validate_field(records.pci.PCI_Period_At_Address)
                        else:
                            if(len(records.pci.PCI_Period_At_Address) <=3):
                                self.passed[records.pci.PCI_Period_At_Address]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Period_At_Address)
                            else:
                                self.passed[records.pci.PCI_Period_At_Address]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Flag_of_Ownership"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.pci.PCI_Flag_of_Ownership):
                                self.passed[records.pci.PCI_Flag_of_Ownership]={"Mandatory":True}
                            else:
                                self.passed[records.pci.PCI_Flag_of_Ownership]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Flag_of_Ownership, priority=r.get(key))
                                self.passed[records.PCI_Flag_of_Ownership]["ENF"]=self.statuss.validate_field(records.pci.PCI_Flag_of_Ownership)
                        else:
                            if(records.pci.PCI_Flag_of_Ownership):
                                if(len(records.pci.PCI_Flag_of_Ownership) <=5):
                                    self.passed[records.pci.PCI_Flag_of_Ownership]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Flag_of_Ownership)
                                else:
                                    self.passed[records.pci.PCI_Flag_of_Ownership]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Flag_of_Ownership]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Primary_Number_Country_Dialling_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Primary_Number_Country_Dialling_Code):
                                self.passed[records.pci.PCI_Primary_Number_Country_Dialling_Code]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Primary_Number_Country_Dialling_Code]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Primary_Number_Country_Dialling_Code, priority=r.get(key))
                                self.passed[records.pci.PCI_Primary_Number_Country_Dialling_Code]["ENF"]=self.statuss.validate_field(records.pci.PCI_Primary_Number_Country_Dialling_Code)
                        else:
                            if(records.pci.PCI_Primary_Number_Country_Dialling_Code):
                                if(len(records.pci.PCI_Primary_Number_Country_Dialling_Code) <=5):
                                    self.passed[records.pci.PCI_Primary_Number_Country_Dialling_Code]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Primary_Number_Country_Dialling_Code)
                                else:
                                    self.passed[records.pci.PCI_Primary_Number_Country_Dialling_Code]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Primary_Number_Country_Dialling_Code]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Primary_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Primary_Number_Telephone_Number):
                                self.passed[records.pci.PCI_Primary_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Primary_Number_Telephone_Number]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Primary_Number_Telephone_Number, priority=r.get(key))
                                self.passed[records.pci.PCI_Primary_Number_Telephone_Number]["ENF"]=self.statuss.validate_field(records.pci.PCI_Primary_Number_Telephone_Number)
                        else:
                            if(len(records.pci.PCI_Primary_Number_Telephone_Number) <=10):
                                self.passed[records.pci.PCI_Primary_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Primary_Number_Telephone_Number)
                            else:
                                self.passed[records.pci.PCI_Primary_Number_Telephone_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Other_Number_Country_Dialling_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Other_Number_Country_Dialling_Code):
                                self.passed[records.pci.PCI_Other_Number_Country_Dialling_Code]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Other_Number_Country_Dialling_Code]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Other_Number_Country_Dialling_Code, priority=r.get(key))
                                self.passed[records.pci.PCI_Other_Number_Country_Dialling_Code]["ENF"]=self.statuss.validate_field(records.pci.PCI_Other_Number_Country_Dialling_Code)
                        else:
                            if(records.pci.PCI_Other_Number_Country_Dialling_Code):
                                if(len(records.pci.PCI_Other_Number_Country_Dialling_Code) <=5):
                                    self.passed[records.pci.PCI_Other_Number_Country_Dialling_Code]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Other_Number_Country_Dialling_Code)
                                else:
                                    self.passed[records.pci.PCI_Other_Number_Country_Dialling_Code]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Other_Number_Country_Dialling_Code]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Other_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Other_Number_Telephone_Number):
                                self.passed[records.pci.PCI_Other_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Other_Number_Telephone_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Other_Number_Telephone_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Other_Number_Telephone_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Other_Number_Telephone_Number)
                        else:
                            if(len(records.pci.PCI_Other_Number_Telephone_Number) <=5):
                                self.passed[records.pci.PCI_Other_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Other_Number_Telephone_Number)
                            else:
                                self.passed[records.pci.PCI_Other_Number_Telephone_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Mobile_Number_Country_Dialling_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Mobile_Number_Country_Dialling_Code):
                                self.passed[records.pci.PCI_Mobile_Number_Country_Dialling_Code]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Mobile_Number_Country_Dialling_Code]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Mobile_Number_Country_Dialling_Code, priority=r.get(key))
                                self.passed[records.pci.PCI_Mobile_Number_Country_Dialling_Code]["ENF"]=self.statuss.validate_field(records.pci.PCI_Mobile_Number_Country_Dialling_Code)
                        else:
                            if(records.pci.PCI_Mobile_Number_Country_Dialling_Code):
                                if(len(records.pci.PCI_Mobile_Number_Country_Dialling_Code) <=5):
                                    self.passed[records.pci.PCI_Mobile_Number_Country_Dialling_Code]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Mobile_Number_Country_Dialling_Code)
                                else:
                                    self.passed[records.pci.PCI_Mobile_Number_Country_Dialling_Code]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Mobile_Number_Country_Dialling_Code]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Mobile_Number_Telephone_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Mobile_Number_Telephone_Number):
                                self.passed[records.pci.PCI_Mobile_Number_Telephone_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Mobile_Number_Telephone_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Mobile_Number_Country_Dialling_Code, priority=r.get(key))
                            self.passed[records.pci.PCI_Mobile_Number_Telephone_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Mobile_Number_Country_Dialling_Code)
                        else:
                            if(records.pci.PCI_Mobile_Number_Telephone_Number):
                                if(len(records.pci.PCI_Mobile_Number_Telephone_Number) <=5):
                                    self.passed[records.pci.PCI_Mobile_Number_Telephone_Number]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Mobile_Number_Telephone_Number)
                                else:
                                    self.passed[records.pci.PCI_Mobile_Number_Telephone_Number]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Mobile_Number_Telephone_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Facsimile_Country_Dialling_Code"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Facsimile_Country_Dialling_Code):
                                self.passed[records.pci.PCI_Facsimile_Country_Dialling_Code]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Facsimile_Country_Dialling_Code]={"Conditional":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.pci.PCI_Facsimile_Country_Dialling_Code, priority=r.get(key))
                                self.passed[records.pci.PCI_Facsimile_Country_Dialling_Code]["ENF"]=self.statuss.validate_field(records.pci.PCI_Facsimile_Country_Dialling_Code)
                        else:
                            if(records.pci.PCI_Facsimile_Country_Dialling_Code):
                                if(len(records.pci.PCI_Facsimile_Country_Dialling_Code) <=5):
                                    self.passed[records.pci.PCI_Facsimile_Country_Dialling_Code]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Facsimile_Country_Dialling_Code)
                                else:
                                    self.passed[records.pci.PCI_Facsimile_Country_Dialling_Code]["FORMAT"]=False
                            else:
                                self.passed[records.pci.PCI_Facsimile_Country_Dialling_Code]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Facsimile_Number"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Facsimile_Number):
                                self.passed[records.pci.PCI_Facsimile_Number]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Facsimile_Number]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Facsimile_Number]["ENF"]= True #self.statuss.validate_field(records.PCI_Facsimile_Number)
                        else:
                            if(len(records.pci.PCI_Facsimile_Number) <=10):
                                self.passed[records.pci.PCI_Facsimile_Number]["FORMAT"]=checkformat.is_numeric(records.pci.PCI_Facsimile_Number)
                            else:
                                self.passed[records.pci.PCI_Facsimile_Number]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Email_Address"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Email_Address):
                                self.passed[records.pci.PCI_Email_Address]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Email_Address]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Email_Address]["ENF"]= True #self.statuss.validate_field(records.PCI_Facsimile_Number)
                        else:
                            if(len(records.pci.PCI_Email_Address) <=50):
                                self.passed[records.pci.PCI_Email_Address]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Email_Address)
                            else:
                                self.passed[records.pci.PCI_Email_Address]["FORMAT"]=False
                yield self.passed

            elif(f == "PCI_Web_site"):
                self.pass_pi = {}
                self.by_id = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "C":
                            if(records.pci.PCI_Web_site):
                                self.passed[records.pci.PCI_Web_site]={"Conditional":True}
                            else:
                                self.passed[records.pci.PCI_Web_site]={"Conditional":False}

                        elif(isinstance(r, bool)):
                            #for key in r:
                            #    self.statuss = checkenforcements.check_enforcements(key, self._model, records.PCI_Facsimile_Number, priority=r.get(key))
                            self.passed[records.pci.PCI_Web_site]["ENF"]= True #self.statuss.validate_field(records.PCI_Facsimile_Number)
                        else:
                            if(len(records.PCI_Web_site) <=50):
                                self.passed[records.pci.PCI_Web_site]["FORMAT"]=checkformat.sub_alphanumeric(records.pci.PCI_Web_site)
                            else:
                                self.passed[records.pci.PCI_Web_site]["FORMAT"]=False
                yield self.passed
        except:
            pass
