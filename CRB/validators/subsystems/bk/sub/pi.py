from datasetrecords import models 
from validators.subsystems import enforcement

class ExtractPIFields(object):
    """
    Object for extracting the PI fields.
    """
    def __init__(self, pimodel):
        self.model = pimodel 
        self.field_list = [ ]
        
    def extract(self):
        """
        Extract the fields from the given models.
        """
        try:
            self.mfields = self.getModel()._meta.fields
            if(self.mfields):
                try:
                    for model_fields in self.mfields:
                        if(model_fields.name in self.field_list):
                            pass 
                        elif(model_fields.name == "id"):
                            pass 
                            
                        elif(model_fields.name == "pci"):
                            pass 
                        elif(model_fields.name == "sci"):
                            pass 
                        else:
                            self.field_list.append(model_fields.name)
                except:
                    raise 
            else:
                return None 
        except:
            raise 
        else:
            return self.field_list
            
    def getModel(self):
        return self.model 
    
    def field_rules(self, fields, rules):
        """
        Given the field, and optionally required argument
        build the rule and the validation against
        each field.
        """
        self.fields_with_rules = { }
        try:
            if(isinstance(fields, list)):
                try:
                    for field in fields:
                        self.fields_with_rules[field]=rules 
                except:
                    raise 
                else:
                    return self.fields_with_rules
            else:
                return False 
        except:
            raise 
    
    def search_field(self, fieldname):
        self.ret_code = { }
        for field in self.extract():
            self.field_info = [enforcement.data_status["mandatory"],"AI",
                                enforcement.construct_enforn[68]
                               ]
            self.field_stat = self.field_rules[field, self.field_info]
            
    def field_validation_requirement(self, field, status, formats, enforcements):
        try:
            return {"status":status, "format":formats, "enforcements":enforcements}
        except:
            raise 
        
    def construct_enforcement(self, enforcement, priorities):
        """
        return the given priorityes.
        """
        try:
            return {enforcement:priorities}
        except:
            raise     
    
    def dataset_code(self, datacode, compiled_rules):
        if(compiled_rules):
            return {datacode:compiled_rules}
        else:
            return None 
            
    def contruct_pi(self):
        for d in range(1, len(self.extract())+1):
            PI = "PI"
            formats = PI + "%03d" % (d,)
            yield formats
        
