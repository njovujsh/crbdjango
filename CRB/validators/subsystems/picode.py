#  picode.py
#  
#  Copyright 2015 Wangolo Joel <wangolo@developer>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty o
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from validators.subsystems import enforcement
from validators.subsystems import enforcement as enfs

class PICode(object):
    def __init__(self, models, datacode):
        self.model = models 
        self.enforce = enforcement.get_enforcement()
        self.datacode = datacode
        
    def extract(self):
        """
        Extract the fields from the given models.
        """
        self.field_list = []
        
        try:
            self.mfields = self.getModel()._meta.fields
            if(self.mfields):
                try:
                    for model_fields in self.mfields:
                        if(model_fields.name == "id"):
                            pass 
                            
                        elif(model_fields.name == "pci"):
                            pass 
                        elif(model_fields.name == "sci"):
                            pass 
                        elif(model_fields.name == "validated"):
                            pass 
                        else:
                            self.field_list.append(model_fields.name)
                    return self.field_list
                except:
                    raise 
            else:
                return None 
        except:
            raise 
        
    def make_code(self, datasetname):
        """
        Given the dataset name return the picode.
        """
        try:
            if(datasetname):
                for i in range(1, len(self.extract()) + 1):
                    self.formated = datasetname + "%03d" % (i,)
                    yield self.formated 
        except:
            raise 

    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field=None
        
        self.pi_code = self.make_code(self.datacode)
   
        for field in self.extract():
            if(field == "PI_Identification_Code"):
                self.ret_field = [enforcement.data_status()["mandatory"], "A6",
                                       enfs.get_enf_by_number(68)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field,field)
                
            elif(field == "Institution_Type"):
                self.ret_field = [enforcement.data_status()["mandatory"], "A3",
                                       enfs.get_enf_by_number(69)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                
            elif(field == "Institution_Name"):
                self.ret_field =[enforcement.data_status()["mandatory"], "AS100",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field,field)
                
            elif(field == "License_Issuing_Date"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            else:
                pass 
            if (ret_all == False):
                yield self.results 
                
        yield self.results
        
    def update_result(self,result, picode_r, rules, field):
        if(field in result):
            pass 
        else:
            result[picode_r]={field:rules}
            
    def getModel(self):
        return self.model
        
    def find_rules_by_code(self, code):
        """
        Given the code return the
        corresponding rules.
        """
        try:
            if(len(code)):
                self.all_result = self.join_field_rule(ret_all=True).next()
                if(self.all_result):
                    try:
                        return self.all_result.get(code)
                    except KeyError as error:
                        return str(code) + str("Not found")
                    except:
                        return 'error looking for records'
            else:
                return "Code is Required"
        except:
            raise 
            
    def get_rule_by_field(self, field):
        """
        Given the field return the rule.
        """
        try:
            if(len(field)):
                self.all_result = self.join_field_rule(ret_all=True).next()
                if(self.all_result):
                    for code in self.all_result.values():
                        try:
                            return code.get(field)
                        except KeyError as error:
                            return str(field) + str("Not found")
                        except:
                            return "Error looking for code."
            else:
                return "Code is Required"
        except:
            raise 
                                    
    def validate_field(self, field_record):
        """
        Beging data validation.
        """
        try:
            self.fields = self.join_field_rule(ret_all=True).next()
            for value in self.fields.values():
                for key in value.keys():
                    print key
        except:
            raise 
            
    def examine_requirement(self, field_record, field, rules):
        """
        Examine and return the requirement status.
        """
        try:
            for record in field_record:
                
                if(field == "PI_Identification_Code"):
                    for r in rules:
                        if(r == "M"):
                            if(getattr(record, field)):
                                print "Field Found ", field 
                            else:
                                print False, field 
                        elif(r == "A6"):
                            if(len(getattr(record, field)) == int(r[1])):
                                print "Alpha Numeric: ", field 
                            else:
                                print "Failed ", record, len(getattr(record, field)), False 
                            
        except:
            raise 
    
    def query_all_records(self):
        if(self.getModel()):
            self.all_rect = self.getModel().objects.all()
            return self.all_rect
        else:
            return False 
            
    def handle_validation(self, rec):
        if(rect.PI_Identification_Code):
            pass 
