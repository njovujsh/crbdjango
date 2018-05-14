#  bcvalidate.py
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

from validators.subsystems import bccode 
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import validationstatus
from creditreports.subsystems import pivalidatereport 
from branchcode import models as branchmodels

class ReportBCValidate(pivalidatereport.ReportPIValidate):
    def __init__(self, code="BC"):
        super(ReportBCValidate, self).__init__(code=code)
        self._model = models.BOUNCEDCHEQUES
        self.all_records  = models.BOUNCEDCHEQUES.objects.all()
        self.headers = branchmodels.RequiredHeader.objects.all()
        self.code = code 
        self.pi_c_code = bccode.BCCode(self._model, self.code)
        self.all_count = models.BOUNCEDCHEQUES.objects.all().count()
        
        self.set_code(self.pi_c_code)
        self.record_fields=14
        
    def check_data_in_field(self, f, rules):        
        self.passed = { }
        self.all_records_passed = {}
        self.final_result={}
        try:
            self.PI_Identification_Code(f, rules)
            self.Branch_Identification_Code(f, rules)
            self.Borrowers_Client_Number(f, rules)
            self.PI_Client_Classification(f, rules)
            self.Cheque_Account_Reference_Number(f, rules)
            self.Cheque_Account_Opened_Date(f, rules)
            self.Cheque_Account_Classification(f, rules)
            self.Cheque_Account_Type(f, rules)
            self.Cheque_Number(f, rules)
            self.Cheque_Amount(f, rules)
            self.Cheque_Currency(f, rules)
            self.Beneficiary_Name_Or_Payee(f, rules)
            self.Cheque_Bounce_Date(f, rules)
            self.Cheque_Account_Bounce_Reason(f, rules)
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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                    else:
                        if(records.PI_Identification_Code):
                            self.parseddata = records.PI_Identification_Code.pi_identification_code.replace("-", "", 10)
                            if(len(self.parseddata) <= 8):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.PI_Identification_Code.pi_identification_code.strip())
                            else:
                                self.passed[records.id]["FORMAT"]=False
                        else:
                            self.passed[str(records.id)]["FORMAT"]=False
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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Branch_Identification_Code.branch_code, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Branch_Identification_Code.branch_code)
                    else:
                        if(len(records.Branch_Identification_Code.branch_code) <= 15):
                            if(str(records.Branch_Identification_Code.branch_code).strip().lstrip().rstrip()):
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(records.Branch_Identification_Code.branch_code)
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
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Borrowers_Client_Number.Client_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Borrowers_Client_Number.Client_Number)

                    else:
                        if(records):
                            if(len(records.Borrowers_Client_Number.Client_Number) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Client_Number)
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
    
    def PI_Client_Classification(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "PI_Client_Classification"):
                for r in rules:
                    if r == "M":
                        if(records.PI_Client_Classification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Client_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.PI_Client_Classification)
                    else:
                        if(records):
                            if(records.PI_Client_Classification):
                                if(len(records.PI_Client_Classification) == 1):
                                    if(str(records.PI_Client_Classification).strip().lstrip().rstrip()):
                                        self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.PI_Client_Classification)))
                                    else:
                                        self.passed[records.id]["FORMAT"]=False
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
            
    def Cheque_Account_Reference_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Account_Reference_Number"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Account_Reference_Number):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Cheque_Account_Reference_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Cheque_Account_Reference_Number)

                    else:
                        if(records):
                            if(len(records.Cheque_Account_Reference_Number) <= 30):
                                self.passed[records.id]["FORMAT"]=True #checkformat.sub_alphanumeric(records.Cheque_Account_Reference_Number)
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
    
    def Cheque_Account_Opened_Date(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Account_Opened_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Account_Opened_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Account_Opened_Date)
                                
                                if(self.validation_first == True):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Cheque_Account_Opened_Date)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Account_Opened_Date, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Account_Opened_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Cheque_Account_Opened_Date, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False 
                    else:
                        if(records.Cheque_Account_Opened_Date):
                            self.formated = records.Cheque_Account_Opened_Date.replace("-", "", 50).replace("/", "", 50).strip().lstrip().rstrip()
                            if(len(records.Cheque_Account_Opened_Date) <= 18):
                                self.formated = records.Cheque_Account_Opened_Date.replace("-", "", 50).replace("/", "", 50).strip().lstrip().rstrip()
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.formated)))
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
                
    def Cheque_Account_Classification(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Account_Classification"):
                for r in rules:
                    if r == "M":
                        #print "Date ", records.License_Issuing_Date
                        if(records.Cheque_Account_Classification):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Cheque_Account_Classification, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Cheque_Account_Classification)

                    else:
                        if(records.Cheque_Account_Classification):
                            if(len(records.Cheque_Account_Classification) <= 100):
                                if(str(records.Cheque_Account_Classification).strip().lstrip().rstrip()):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(records.id)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
                
    def Cheque_Account_Type(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Account_Type"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Account_Type):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Cheque_Account_Type, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Cheque_Account_Type)

                    else:
                        if(records.Cheque_Account_Type):
                            if(len(records.Cheque_Account_Type) == 1):
                                self.striped = str(records.Cheque_Account_Type).strip().lstrip().rstrip()
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.striped)))
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
                
    def Cheque_Number(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Number"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Number):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Cheque_Number, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Cheque_Number)

                    else:
                        if(records):
                            if(len(records.Cheque_Number) <= 20):
                                self.stripped = str(records.Cheque_Number).strip().lstrip().rstrip()
                                self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.stripped)))
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
    
    def Cheque_Amount(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Amount"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Amount):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Cheque_Amount, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Cheque_Amount)

                    else:
                        if(records):
                            if(records.Cheque_Amount):
                                if(len(records.Cheque_Amount) <= 21):
                                    self.stripped = str(records.Cheque_Amount.strip()).lstrip().rstrip()
                                    if(self.stripped):
                                        self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.stripped)))
                                    else:
                                        self.passed[records.id]["FORMAT"]=False
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
                
    def Cheque_Currency(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Currency"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Currency):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Currency, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Currency)
                                
                                if(self.validation_first == True):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Currency, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Cheque_Currency)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Currency, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Currency, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Currency)
                                self.validation_second = self.sec_enf.validate_field(records.Cheque_Currency, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                    else:
                        if(records.Cheque_Currency):
                            if(len(records.Cheque_Currency) == 3):
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Cheque_Currency)
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
                
    def Beneficiary_Name_Or_Payee(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Beneficiary_Name_Or_Payee"):
                for r in rules:
                    if r == "M":
                        if(records.Beneficiary_Name_Or_Payee):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}
                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Beneficiary_Name_Or_Payee, priority=r.get(key))
                            self.passed[records.id]["ENF"]=self.statuss.validate_field(records.Beneficiary_Name_Or_Payee)

                    else:
                        if(records):
                            if(len(records.Beneficiary_Name_Or_Payee) <= 50):
                                #print "Passed ",records.Beneficiary_Name_Or_Payee.count(" ")
                                self.passed[records.id]["FORMAT"]=checkformat.sub_alphanumeric(records.Beneficiary_Name_Or_Payee)
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
    
    def Cheque_Bounce_Date(self, f, rules):
        for records in self.all_records:
            if(f == "Cheque_Bounce_Date"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Bounce_Date):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            #print "KEY ", key, r
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Bounce_Date, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Bounce_Date)
                                
                                if(self.validation_first == True):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Bounce_Date, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Cheque_Bounce_Date)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Bounce_Date, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Bounce_Date, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Bounce_Date)
                                self.validation_second = self.sec_enf.validate_field(records.Cheque_Bounce_Date, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                    else:
                        if(records):
                            if(len(records.Cheque_Bounce_Date) <= 12):
                                self.stripped_date = str(records.Cheque_Bounce_Date).strip().lstrip().rstrip()
                                if(self.stripped_date):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.stripped_date)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
    
    def Cheque_Account_Bounce_Reason(self, f, rules):
        self.passed = {}
        for records in self.all_records:
            if(f == "Cheque_Account_Bounce_Reason"):
                for r in rules:
                    if r == "M":
                        if(records.Cheque_Account_Bounce_Reason):
                            self.passed[records.id]={"Mandatory":True}
                        else:
                            self.passed[records.id]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.first_priority = self.check_dict_values(r.get(key)[0])
                            self.second_priority = self.check_dict_values(r.get(key)[1])
                            
                            if(self.first_priority == 1 or self.first_priority == 2):
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Account_Bounce_Reason, priority=r.get(key))
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Account_Bounce_Reason)
                                
                                if(self.validation_first == True):
                                    self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Account_Bounce_Reason, priority=r.get(key))
                                    self.validation_second = self.sec_enf.validate_field(records.Cheque_Account_Bounce_Reason)
                                    
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True 
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                            else:
                                self.vstatus = checkenforcements.check_enforcements(self.get_keys(r.get(key)[0]), self._model, records.Cheque_Account_Bounce_Reason, priority=r.get(key))
                                self.sec_enf = checkenforcements.check_enforcements(self.get_keys(r.get(key)[1]), self._model, records.Cheque_Account_Bounce_Reason, priority=r.get(key))
                                
                                self.validation_first = self.vstatus.validate_field(records.Cheque_Account_Bounce_Reason)
                                self.validation_second = self.sec_enf.validate_field(records.Cheque_Account_Bounce_Reason, headers=self.headers)
                                
                                if(self.validation_first == True):
                                    if(self.validation_second == True):
                                        self.passed[records.id]["ENF"]=True
                                    else:
                                        self.passed[records.id]["ENF"]=False
                                else:
                                    self.passed[records.id]["ENF"]=False
                    else:
                        if(records):
                            if(records.Cheque_Account_Bounce_Reason):
                                self.stripped_reason = str(records.Cheque_Account_Bounce_Reason)
                                if(len(self.stripped_reason) <= 12):
                                    self.passed[records.id]["FORMAT"]=checkformat.is_numeric(int(float(self.stripped_reason)))
                                else:
                                    self.passed[records.id]["FORMAT"]=False
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
