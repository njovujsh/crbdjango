#  ccgvalidate.py
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
from validators.subsystems import ccgcode 
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 
from branchcode import models as branchmodels

class ReportCCGValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="CCG"):
        super(ReportCCGValidate, self).__init__(code=code)
        self._model = models.COLLATERAL_CREDIT_GUARANTOR
        self.all_records  = models.COLLATERAL_CREDIT_GUARANTOR.objects.all()
        self.headers = branchmodels.RequiredHeader.objects.all()
        self.code = code 
        self.pi_c_code = ccgcode.CCGCode(self._model, self.code)
        self.all_count = models.COLLATERAL_CREDIT_GUARANTOR.objects.all().count()
        self.set_code(self.pi_c_code)
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }
        self.all_records_passed = {}
        self.final_result={}
        try:
            self.PI_Identification_Code(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Borrowers_Client_Number(f, rules)
            self.Borrower_Account_Reference(f, rules)
            self.Guarantor_Classification(f, rules)
            self.Guarantee_Type(f, rules)
            self.Guarantor_Type(f, rules)
        except Exception as e:
            pass 
        else:
            yield self.final_result
            
    
    def PI_Identification_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "PI_Identification_Code"):
                for r in rules:
                    if r == "M":
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                    else:
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata) >= 2):
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
    
    def Branch_Identification_Code(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Branch_Identification_Code"):
                for r in rules:
                    if r == "M":
                        if(records.Branch_Identification_Code.branch_code):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.branch_code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(len(records.Branch_Identification_Code.branch_code) >= 2):
                            self.passed[records.id]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
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
    
    def Borrowers_Client_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Borrowers_Client_Number"):
                for r in rules:
                    if r == "M":
                        if(records.Borrowers_Client_Number.Client_Number):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Borrowers_Client_Number.Client_Number)
                                
                                if(self.validation_first == True):
                                    #Perform the second validation
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False 
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Borrowers_Client_Number.Client_Number)
                                self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 

                    else:
                        if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                            self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrowers_Client_Number.Client_Number)
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
    
    def Borrower_Account_Reference(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Borrower_Account_Reference"):
                for r in rules:
                    if r == "M":
                        if(records.Borrower_Account_Reference):
                            if(records.Borrower_Account_Reference.Credit_Account_Reference):
                                self.passed[records.id]={"Mandatory":True}
                            else:
                                self.passed[records.id]={"Mandatory":False}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        if(records.Borrower_Account_Reference):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Account_Reference.Credit_Account_Reference, priority=r.get(key))
                                self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)
                        else:
                            self.passed[records.id]["ENF"]=True #self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)

                    else:
                        if(records.Borrower_Account_Reference):
                            if(len(records.Borrower_Account_Reference.Credit_Account_Reference) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrower_Account_Reference)
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
            
    def Guarantor_Classification(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Guarantor_Classification"):
                for r in rules:
                    if r == "M":
                        if(records.Guarantor_Classification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Guarantor_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Guarantor_Classification)
                    else:
                        if(records.Guarantor_Classification):
                            if(len(records.Guarantor_Classification) >= 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Guarantor_Classification)
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
            
    def Guarantee_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Guarantee_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Guarantee_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Guarantee_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Guarantee_Type)

                    else:
                        if(records.Guarantee_Type):
                            if(len(records.Guarantee_Type) >= 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Guarantee_Type)
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[records.id]["FORMAT"]=False
                self.final_result[records.id]=self.passed
                #print self.final_result
        if(not len(self.passed)):
            pass 
        elif(len(self.passed) == self.all_count):
            for keys in self.passed.iterkeys():
                self.passed_by_id.get(keys).append(self.passed.get(keys).values().count(True))
        else:
            pass 
            
    def Guarantor_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Guarantor_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Guarantor_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Guarantor_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Guarantor_Type)
                    else:
                        if(records.Guarantor_Type):
                            if(len(records.Guarantor_Type) >= 1):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Guarantor_Type)
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
