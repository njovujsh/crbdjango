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
from branchcode import models as branchmodels 

class CCGValidate(ibvalidate.IBValidate):
    def __init__(self, code="CCG"):
        super(CCGValidate, self).__init__(code=code)
        self._model = models.COLLATERAL_CREDIT_GUARANTOR
        self.all_records  = self.filter_new_old_records(models.COLLATERAL_CREDIT_GUARANTOR)
        self.headers = branchmodels.RequiredHeader.objects.all()
        self.code = code 
        self.pi_c_code = ccgcode.CCGCode(self._model, self.code)
        
        self.set_code(self.pi_c_code)
        
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
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=True 
                                        else:
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False
                                    else:
                                        self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.PI_Identification_Code.pi_identification_code)
                                    self.validation_second = self.sec_enf.validate_field(records.PI_Identification_Code.pi_identification_code, headers=self.headers, compare_pi=True)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=True
                                        else:
                                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False
                                    else:
                                        self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=False 
                        else:
                            if(records.PI_Identification_Code):
                                self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                                if(len(self.parseddata) >= 2):
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                                else:
                                    self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
                            else:
                                self.passed[str(records.PI_Identification_Code.pi_identification_code)]["FORMAT"]=False
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
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=True 
                                        else:
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False 
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Branch_Identification_Code.branch_code)
                                    self.validation_second = self.sec_enf.validate_field(records.Branch_Identification_Code.Branch_Code, headers=records.Branch_Identification_Code.branch_code, compare_b=True)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=True
                                        else:
                                            self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False
                                    else:
                                        self.passed[records.Branch_Identification_Code.branch_code]["ENF"]=False 

                        else:
                            if(len(records.Branch_Identification_Code.branch_code) >= 2):
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=True #checkformat.is_numeric(records.Branch_Identification_Code)
                            else:
                                self.passed[records.Branch_Identification_Code.branch_code]["FORMAT"]=False
                yield self.passed 

            elif(f == "Borrowers_Client_Number"):
                self.pass_in = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Borrowers_Client_Number.Client_Number):
                                self.passed[records.Borrowers_Client_Number.Client_Number]={"Mandatory":True}
                            else:
                                self.passed[records.Borrowers_Client_Number.Client_Number]={"Mandatory":False}

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
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=True 
                                        else:
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False 
                                    else:
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False
                                else:
                                    self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                                    
                                    self.validation_first = self.vstatus.validate_field(records.Borrowers_Client_Number.Client_Number)
                                    self.validation_second = self.sec_enf.validate_field(records.Borrowers_Client_Number.Client_Number, headers=self.headers, b_client=True)
                                    
                                    if(self.validation_first == True):
                                        if(self.validation_second == True):
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=True
                                        else:
                                            self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False
                                    else:
                                        self.passed[records.Borrowers_Client_Number.Client_Number]["ENF"]=False 

                        else:
                            if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                                self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrowers_Client_Number.Client_Number)
                            else:
                                self.passed[records.Borrowers_Client_Number.Client_Number]["FORMAT"]=False
                yield self.passed 

            elif(f == "Borrower_Account_Reference"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Borrower_Account_Reference):
                                if(records.Borrower_Account_Reference.Credit_Account_Reference):
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]={"Mandatory":True}
                                else:
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]={"Mandatory":False}
                            else:
                                self.passed[records.Borrower_Account_Reference]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            if(records.Borrower_Account_Reference):
                                for key in r:
                                    self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrower_Account_Reference.Credit_Account_Reference, priority=r.get(key))
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["ENF"]=self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)
                            else:
                                self.passed[records.Borrower_Account_Reference]["ENF"]=False #self.statuss.validate_field(records.Borrower_Account_Reference.Credit_Account_Reference)

                        else:
                            if(records.Borrower_Account_Reference):
                                if(len(records.Borrower_Account_Reference.Credit_Account_Reference) <= 30):
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Borrower_Account_Reference)
                                else:
                                    self.passed[records.Borrower_Account_Reference.Credit_Account_Reference]["FORMAT"]=False
                            else:
                                self.passed[records.Borrower_Account_Reference]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Guarantor_Classification"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Guarantor_Classification):
                                self.passed[records.Guarantor_Classification]={"Mandatory":True}
                            else:
                                self.passed[records.Guarantor_Classification]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Guarantor_Classification, priority=r.get(key))
                                self.passed[records.Guarantor_Classification]["ENF"]=self.statuss.validate_field(records.Guarantor_Classification)

                        else:
                            if(len(records.Guarantor_Classification) == 1):
                                self.passed[records.Guarantor_Classification]["FORMAT"]=checkformat.is_numeric(records.Guarantor_Classification)
                            else:
                                self.passed[records.Guarantor_Classification]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Guarantee_Type"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            if(records.Guarantee_Type):
                                self.passed[records.Guarantee_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Guarantee_Type]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Guarantee_Type, priority=r.get(key))
                                self.passed[records.Guarantee_Type]["ENF"]=self.statuss.validate_field(records.Guarantee_Type)

                        else:
                            if(len(records.Guarantee_Type) == 1):
                                self.passed[records.Guarantee_Type]["FORMAT"]=checkformat.is_numeric(records.Guarantee_Type)
                            else:
                                self.passed[records.Guarantee_Type]["FORMAT"]=False
                yield self.passed 
                
            elif(f == "Guarantor_Type"):
                self.pass_lid = {}
                for records in self.all_records:
                    for r in rules:
                        if r == "M":
                            #print "Date ", records.License_Issuing_Date
                            if(records.Guarantor_Type):
                                self.passed[records.Guarantor_Type]={"Mandatory":True}
                            else:
                                self.passed[records.Guarantor_Type]={"Mandatory":False}

                        elif(isinstance(r, dict)):
                            for key in r:
                                self.statuss = checkenforcements.check_enforcements(key, self._model, records.Guarantor_Type, priority=r.get(key))
                                self.passed[records.Guarantor_Type]["ENF"]=self.statuss.validate_field(records.Guarantor_Type)

                        else:
                            if(len(records.Guarantor_Type) == 1):
                                self.passed[records.Guarantor_Type]["FORMAT"]=checkformat.is_numeric(records.Guarantor_Type)
                            else:
                                self.passed[records.Guarantor_Type]["FORMAT"]=False
                yield self.passed
        except Exception as e:
            # Log
            pass  
