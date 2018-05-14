from datasetrecords import models 
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode 


class EICode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(EICode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True
        
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode) 
        
        for field in self.extract():
            try:
                if(field == "EI_Employment_Type"):
                    self.ret_field = [enfs.data_status()["conditional"], "A1",
                                           {"ENF":[enfs.get_enf_by_number(35), enfs.get_enf_by_number(85)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field,field)
                
                
                elif(field == "EI_Primary_Occupation"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS100",
                                           enfs.get_enf_by_number(66)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "EI_Employer_Name"):
                    self.ret_field =[enfs.data_status()["conditional"], "AS100",
                                           enfs.get_enf_by_number(66)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field,field)
                    
                elif(field == "EI_Employee_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS20",
                                           True
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "EI_Employment_Date"):
                    self.ret_field = [enfs.data_status()["conditional"], "N8",
                                           enfs.get_enf_by_number(5)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "EI_Income_Band"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                           {"ENF":[enfs.get_enf_by_number(66), enfs.get_enf_by_number(53)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "EI_Salary_Frequency"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                           {"ENF":[enfs.get_enf_by_number(66), enfs.get_enf_by_number(59)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                else:
                    pass 
                if (ret_all == False):
                    yield self.results 
            except:
                raise 
